from __future__ import annotations

import asyncio
import contextlib
import logging
import subprocess
import sys
from pathlib import Path
from unittest.mock import patch

import pytest

from pglift import cmd
from pglift.exceptions import CommandError, SystemError
from pglift.types import Status


def test_execute_program(caplog: pytest.LogCaptureFixture, tmp_path: Path) -> None:
    command = ["/c", "m", "d"]
    with patch("os.execve", autospec=True) as execve, patch(
        "os.execv", autospec=True
    ) as execv:
        cmd.execute_program(command, env={"X": "Y"})
        execve.assert_called_once_with("/c", command, {"X": "Y"})
        assert not execv.called
    with patch("os.execve", autospec=True) as execve, patch(
        "os.execv", autospec=True
    ) as execv, caplog.at_level(logging.DEBUG, logger="pglift.cmd"):
        cmd.execute_program(command)
        execv.assert_called_once_with("/c", command)
        assert not execve.called
    assert "executing program '/c m d'" in caplog.records[0].message


def test_start_program_terminate_program_status_program(
    caplog: pytest.LogCaptureFixture, tmp_path: Path
) -> None:
    pidfile = tmp_path / "sleep" / "pid"
    p = cmd.Program(["sleep", "10"], pidfile, timeout=0.01, env={"X_DEBUG": "1"})
    assert p.pidfile == pidfile
    with pidfile.open() as f:
        pid = f.read()

    assert p.proc.pid == int(pid)

    proc = Path("/proc") / pid
    assert proc.exists()
    assert "sleep\x0010\x00" in (proc / "cmdline").read_text()
    assert "X_DEBUG" in (proc / "environ").read_text()

    assert cmd.status_program(pidfile) == Status.running

    with pidfile.open("a") as f:
        f.write("\nextra\ninformation\nignored")
    assert cmd.status_program(pidfile) == Status.running

    with pytest.raises(SystemError, match="running already"):
        cmd.Program(["sleep", "10"], pidfile)

    cmd.terminate_program(pidfile)
    r = subprocess.run(["pgrep", pid], check=False)
    assert r.returncode == 1

    assert not pidfile.exists()
    assert cmd.status_program(pidfile) == Status.not_running

    pidfile = tmp_path / "invalid.pid"
    pidfile.write_text("innnnvaaaaaaaaaaliiiiiiiiiiid")
    assert cmd.status_program(pidfile) == Status.not_running
    caplog.clear()
    with pytest.raises(CommandError) as excinfo, caplog.at_level(
        logging.DEBUG, logger=__name__
    ):
        cmd.Program(["sleep", "well"], pidfile, env={"LANG": "C", "LC_ALL": "C"})
    assert not pidfile.exists()
    assert "sleep is supposed to be running" in caplog.records[0].message
    assert "sleep: invalid time interval 'well'" in caplog.records[2].message
    assert "sleep: invalid time interval 'well'" in excinfo.value.stderr

    pidfile = tmp_path / "notfound"
    caplog.clear()
    with caplog.at_level(logging.WARNING, logger="pglift.cmd"):
        cmd.terminate_program(pidfile)
    assert f"program from {pidfile} not running" in caplog.records[0].message


def test_program_context(tmp_path: Path, caplog: pytest.LogCaptureFixture) -> None:
    pidfile = tmp_path / "pid"
    pyprog = tmp_path / "prog.py"
    pyprog.write_text(
        "\n".join(
            [
                "import logging, time, signal, sys",
                "signal.signal(",
                "   signal.SIGTERM,",
                "   lambda signum, frame: logging.error('got signal %d', signum),",
                ")",
                "s = float(sys.argv[1])",
                "logging.warning('sleeping %.1fs', s)",
                "time.sleep(s)",
            ]
        )
    )
    with pytest.raises(ValueError, match="expected"), caplog.at_level(
        logging.DEBUG, logger="pglift.cmd"
    ):
        with cmd.Program(
            [sys.executable, str(pyprog), "0.2"], pidfile, timeout=0.1
        ) as prog:
            assert pidfile.exists()
            assert prog.proc.returncode is None
            raise ValueError("expected")
    messages = caplog.messages
    startuplog, pylog, termlog, signallog = messages
    assert startuplog.startswith("starting program '")
    assert "sleeping 0.2s" in pylog
    assert "terminating program" in termlog
    assert "got signal 15" in signallog
    assert not pidfile.exists()

    class SomeError(Exception):
        pass

    loop = asyncio.get_event_loop()
    program = sys.executable
    with contextlib.suppress(SomeError), caplog.at_level(
        logging.DEBUG, logger="pglift.cmd"
    ):
        with cmd.Program([program, "--version"], pidfile=None, timeout=0) as prog:
            loop.run_until_complete(prog.proc.wait())
            raise SomeError
    terminating_msg, terminated_msg = caplog.messages[-2:]
    assert terminating_msg == f"terminating program '{program} --version'"
    assert terminated_msg == f"program {program} already terminated"
