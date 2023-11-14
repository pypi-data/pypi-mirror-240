Access instance shell (psql)
----------------------------

Command ``pglift instance exec`` can be used to enter a ``psql`` shell on
target instance or to execute any program in PostgreSQL binary directory.

.. code-block:: console

    $ pglift instance exec 14/main -- psql
    psql (14.1 (Debian 14.1-1.pgdg110+1))
    Type "help" for help.

    [14/main] postgres@~=# \q

    $ pglift instance exec 14/main -- psql "dbname=test" -c '\x' -c 'SELECT * FROM foo;'
    Expanded display is on.
    -[ RECORD 1 ]
    x | 1
    -[ RECORD 2 ]
    x | 2

    $ pglift instance exec test -- pg_isready
    /home/dba/.local/share/pglift/run/postgresql:5432 - no response

Each instance gets specific ``.psqlrc`` and ``.psql_history`` files located
in their base directory.

``.psqlrc`` is templated and can be overridden by providing a ``psqlrc`` file in
either ``$XDG_CONFIG_HOME/pglift`` [#xdgconfighome]_ or ``/etc/pglift`` (by
order of precedence). ``{instance}`` is substituted by instance name.

.. [#xdgconfighome]
   Where ``$XDG_CONFIG_HOME`` would be ``$HOME/.config`` unless configured
   differently.
