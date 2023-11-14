Changelog
---------

.. towncrier release notes start

v1.1.0 - 2023-11-13
~~~~~~~~~~~~~~~~~~~

Features
++++++++

- When dumping a database, through ``database dump`` command, we now forward the
  role password (that would possibly be prompted for upon database existence
  check) to dump commands (such as ``pg_dump`` or ``pg_back``).
- Limit ``pg_ctl status`` invocations in most operations for better performance.
- Return the runtime status of Patroni API as part of ``pglift instance status``
  result.


Bug fixes
+++++++++

- Remove ``gss`` from local authentication methods, as it's only available for
  TCP/IP connections.
- Fix bug preventing instance creation when setting a custom surole name.
- Retrieve super-user role's password from environment or ``password_command``
  setting when dumping a database.
- Improve previously misleading errors and tracebacks when something got wrong
  at instance initialization by not showing unrelated errors (fixing a bad
  programming pattern).
- Handle possibly absence of PostgreSQL log file during Patroni bootstrap
  "retry" logic, resolving a crash possibly due to a race condition.
- Log an ``INFO`` message when the PostgreSQL instance has been successfully
  created by Patroni.
- Improve log message about "Patroni log file" not being found during bootstrap
  to make it less misleading by indicating that this is transient (by nature of
  the bootstrap) and eventually logging a successful message.
- Log a ``DEBUG`` message when checking for Patroni "readiness" during
  bootstrap.


Documentation
+++++++++++++

- Remove "pgbackrest" and "Prometheus postgres_exporter" pages from the Python
  API section, as they fail to build with up-to-date dependencies.
- Mention upfront in the installation documentation that Python 3.9 (or higher)
  is required.


Misc.
+++++

- Build the `pglift` binary using latest PyOxidizer version (0.24 or higher).
- Use Python 3.10 to build the binary.


v1.0.0 - 2023-10-17
~~~~~~~~~~~~~~~~~~~

Features
++++++++

- The ``owner`` of a schema can now be specified.
- Log the target database name when creating an extension.


Bug fixes
+++++++++

- Avoid reconfiguring pgBackRest upon PostgreSQL configuration changes when it's
  not needed but only check if respective changes would need a reconfiguration
  of this service (e.g. the socket path).
- Only invoke ``pgbackrest stanza-create`` upon instance creation, not when
  modifying it.
- Avoid reconfiguring Prometheus postgres_exporter upon PostgreSQL configuration
  changes when it's not needed but only check if respective changes would need a
  reconfiguration of this service (e.g. the socket path).
- Avoid reconfiguring temBoard agent upon PostgreSQL configuration changes when
  it's not needed but only check if respective changes would need a
  reconfiguration of this service (e.g. the port).


Deprecations and Removals
+++++++++++++++++++++++++

- In the declarative API (Ansible), the ``clone_from`` field of database object,
  deprecated in previous release, got removed.
- The ``passfile`` and ``use_pg_rewind`` settings under ``patroni`` section,
  deprecated in previous release, are removed; use eponymous fields under the
  ``patroni.postgresql`` section.
- In the declarative API (Ansible), the ``patroni.postgresql_connect_host``
  field of instance object, deprecated in previous release, got removed.
- Set the default value of ``prometheus.queriespath`` site setting to ``null``,
  following its deprecation in version 0.38.0. As a consequence, the "queries"
  file will no longer be installed at instance creation.


Documentation
+++++++++++++

- Document how to configure the managed node with Ansible in the Ansible
  tutorial.
- The documentation has been reviewed overall, fixing examples (previously
  invalid due to "recent" changes), adjusting incomplete instructions,
  clarifying things here and there.


Misc.
+++++

- Set the development status to "Production/Stable".


v0.40.0 - 2023-10-03
~~~~~~~~~~~~~~~~~~~~

Features
++++++++

- Allow to clone a database by restoring only the schema (data definitions)
  through ``--clone-schema-only`` command-line flag or the equivalent
  declarative API.
- Add support for database ``PUBLICATION`` and ``SUBSCRIPTION`` objects through
  the declarative API.
- Allow to configure ``hostssl`` authentication method at instance creation.
- Add support for ``ctl.{keyfile,certfile}}`` for Patroni in site settings.
  This is now required after a `breaking change in version 3.1.0 of Patroni
  <https://github.com/zalando/patroni/blob/master/docs/releases.rst#version-310>`_.
- Add support for basic-authentication (username/password) to etcd from
  instances managed by Patroni.
- Client connection options for the ``replication`` and ``rewind`` users of
  Patroni-managed instances can be specified through
  ``--patroni-postgresql-{replication|rewind}-ssl-{cert,key,password}`` options
  when creating an instance (or similar fields in the declarative API) along
  with ``patroni.postgresql.connection.ssl.{mode,crl,crldir,rootcert}`` site
  settings.
- Stream PostgreSQL log messages to our logger (at DEBUG level) during Patroni
  bootstrap.
- Honour ``postgresql.waldir`` setting when deploying Patroni instances; also,
  when pgBackRest is used, and a backup is available to create a replica from,
  ``pgbackrest restore`` is now invoked with ``--link-map pg_wal=...``.
- Add support for passwordless SSH connection for pgbackrest remote repository
  mode.
- Add support for PostgreSQL version 16.


Bug fixes
+++++++++

- Disallow extra fields, previously ignored, in interface models such as
  ``patroni.restapi`` or ``postgresql.auth`` fields.
- Remove the invalid ``cert`` value for ``--auth-local`` or ``--auth-host``
  options at instance creation as it only applies to ``hostssl``.
- Run local ``pgbackrest server`` with the ``PGPASSFILE`` environment variable
  so that connections made by pgbackrest (through the libpq) can use the
  passfile when it's not in the default location.
- In Patroni REST API settings, fix the validator of ``verify_client`` to only
  require that ``certfile`` is set when the former is.


Deprecations and Removals
+++++++++++++++++++++++++

- In the declarative API (Ansible), the ``clone_from`` field of database object
  is deprecated; instead the new ``clone`` field (especially its ``dsn`` option)
  should be used. E.g. in JSON, replace ``"clone_from": "<your connection
  string>"`` by ``"clone": {"dsn": "<your connection string>"}``.
- Remove the ``clone_from`` field in ``database get`` return value, as it was
  always ``null`` (not preserved from user input).
- Commands ``database dumps`` and ``database restore``, deprecated in version
  0.38.0, are removed.
- In the declarative API (the ``instance`` Ansible module), the
  ``patroni.postgresql_connect_host`` field is deprecated. Instead
  ``patroni.postgresql.connect_host`` can be used for the same purpose.
- Add a new ``patroni.postgresql`` setting field, holding ``passfile`` and
  ``use_pg_rewind`` fields, previously under the top-level ``patroni`` key.
- A ``mode`` option (with value in ``['path', 'host-tls', 'host-ssh']``) now
  needs to be explicitly provided for ``pgbackrest.repository`` in site
  settings. This is a BREAKING CHANGE for which installed site-settings will
  need an update.
- Remove support for PostgreSQL version 11.


Documentation
+++++++++++++

- Improve Patroni settings descriptions, especially concerning TLS certificates.
- Add a "how to" perform major online upgrade of a database through Ansible.
- Clarify and extend security notes about etcd and Patroni.
- Add missing entry in 0.38.0 changelog about the deprecation of ``database
  dumps|restore`` commands.


Misc.
+++++

- Run functional tests under Debian bookworm in CI.
- Use ``pg_dump --format=custom`` and ``pg_restore`` (instead of plain ``psql``)
  when cloning a database.
- In tests, run etcd with HTTPS and let Patroni verify server certificates.


v0.39.0 - 2023-08-25
~~~~~~~~~~~~~~~~~~~~

Bug fixes
+++++++++

- Forbid extra (unknown) keys in site settings by issuing a validation error
  instead of silently ignoring them previously.
- Use ``WantedBy=default.target`` in systemd units instead of
  ``multi-user.target``, which is not generally available in user mode. This
  makes user services starts properly at boot.


Deprecations and Removals
+++++++++++++++++++++++++

- The default value for ``pgbackrest.repository.path`` got removed; this setting
  needs an explicit value.


Documentation
+++++++++++++

- Mention how to install pglift with pipx.


v0.38.0 - 2023-08-03
~~~~~~~~~~~~~~~~~~~~

Features
++++++++

- Add a confirmation to ``pglift database run`` to warn about the databases that will
  be affected by the sql command.
- Add ability to provide a ``.psqlrc`` template as file ``postgresql/psqlrc``
  in site configuration.
- Setting ``replrole: null`` (or not providing it) disables the creation
  of the ``replication`` role.


Bug fixes
+++++++++

- No longer create pgbackrest's lock-path directory during ``site-configure``
  but let pgbackrest handle this itself. This makes the configure remain valid
  upon reboot, by not requiring this directory to be present whereas it might
  have been removed if set to a volatile system like ``/run``.


Deprecations and Removals
+++++++++++++++++++++++++

- Setting ``prometheus.queriespath`` is deprecated and will be removed in the
  next release.

  This follows from the deprecation of ``extend.query-path`` option in
  `postgres_exporter 0.13
  <https://github.com/prometheus-community/postgres_exporter/releases/tag/v0.13.0>`_.
  In the future, support for a dedicated sql_exporter will be added to provide
  equivalent features.
- The default value for ``replrole`` is now ``null``. Users relying on this role
  for replication now have to provide it explicitly in the settings. Also
  entries for replication are not part of the default ``pg_hba.conf`` file
  anymore. Administrators may have to provide a template for this.
- Due to their fragile implementation, especially when custom commands are
  defined in site settings, ``database dumps`` and ``database restore``
  commands are deprecated and will be removed in a future release.


Misc.
+++++

- Improve code quality by using `flake8-bugbear
  <https://pypi.org/project/flake8-bugbear/>`_.


v0.37.0 - 2023-07-18
~~~~~~~~~~~~~~~~~~~~

Features
++++++++

- Validate ``postgresql.bindir`` setting to make sure it contains the
  ``{version}`` template placeholder.
- Validate that ``postgresql.default_version`` setting has a value within
  ``postgresql.versions``.
- If setting ``postgresql.default_version`` is undefined, guess the default
  version from the latest PostgreSQL version available as defined in
  ``postgresql.versions`` setting.
- Check pgBackRest configuration upon instance promotion.
- Skip the check of pgBackRest configuration for standby instances on sites
  using the ``repository.path`` mode for pgbackrest. A warning is emitted
  instead, but this should unblock the creation of standby instances in this
  mode.
- Validate that ``postgresql.versions`` setting is a non-empty list, possibly
  after having inferred values from ``bindir`` template.
- Validate that path-like settings only contain expected template variables:
  e.g, a validation error will be raised if a settings field contains
  ``{version}`` or ``{name}`` placeholders whereas none is allowed.


Bug fixes
+++++++++

- Also add a password file entry for the *backup* role upon standby instances
  creation.
- Consider only the first item of ``unix_socket_directories`` PostgreSQL setting
  to determine the ``host`` part of libpq connection string.
- No longer return ``PGHOST=localhost`` in ``instance env`` command when no
  ``unix_socket_directories`` configuration entry is defined in order to let
  PostgreSQL use the default value.
- Set the default answer to *No* in prompt asking for deletion of pgBackRest
  backups upon instance drop.


Removals
++++++++

- The "default version" is no longer guessed from ``pg_config`` executable
  available in ``$PATH``; only site settings are used from now on.


Documentation
+++++++++++++

- Fix first item of ``restore_commands`` example with `pg_back` missing the
  ``{conninfo}``.


v0.36.1 - 2023-06-20
~~~~~~~~~~~~~~~~~~~~

Misc.
+++++

- Switch to `hatch <https://hatch.pypa.io/>`_ build system.


v0.36.0 - 2023-06-15
~~~~~~~~~~~~~~~~~~~~

Features
++++++++

- Check installation before performing any operation: when the ``site-configure
  install`` has not been run or the installation is broken, any operational
  command will fail fast suggesting to perform a proper installation while
  installation issues are logged at ``ERROR`` level.
- Improve the command-line interface with respect to the ``-i/--instance``
  option. The option is no longer required to display the help of a subcommand
  (e.g. ``pglift database create --help``). Also, a more accurate error message
  is displayed when no instance is found or when several ones are found.
- Validate ``postgresql.{dump,restore}_commands`` settings to that the programs
  used by each command exist. This only applies to commands using non-PostgreSQL
  binaries (e.g. ``pg_dump``) as these are typically defined relative to
  instance's binary directory (e.g. ``{bindir}/pg_dump``).


Bug fixes
+++++++++

- Report failure to start a child process (e.g. the database dump command) with
  a user error instead of throwing a traceback.
- Command ``pglift instance exec INSTANCE COMMAND...`` now exits with status 2
  when no command got specified.
- Fix ``instance exec`` command to make it clear that the ``INSTANCE`` argument
  is not optional.


Documentation
+++++++++++++

- Document the need for ``--`` in ``instance exec`` command.


v0.35.0 - 2023-05-17
~~~~~~~~~~~~~~~~~~~~

Bug fixes
+++++++++

- Implicitly convert ``None`` value to the default value for ``patroni.node``
  and ``patroni.restapi`` fields when using Ansible modules.


v0.34.0 - 2023-04-21
~~~~~~~~~~~~~~~~~~~~

Features
++++++++

- The ``instance status`` command has been extended to return the status of
  all satellite components. It will exit with code 3 if any service is not
  running.
  The prometheus and temBoard agent statuses have been implemented in addition to
  the existing PostgreSQL status.
- When creating a standby instance, if a pgbackrest backup for target stanza
  exists, it will be used instead of ``pg_basebackup``.
- Upon deletion of an instance, do not prompt for possible deletion of its
  pgbackrest stanza when another instance is using it.
- Upon deletion of an instance, delete its pgbackrest configuration even if
  stanza deletion was not confirmed.
- Remove log, spool and lock paths for pgbackrest upon ``site-configure
  uninstall``.
- Remove, after confirmation, the backup directory for pgbackrest upon
  ``site-configure uninstall``.
- Add a default value for ``pgbackrest.repository.path`` setting with value
  ``$prefix/pgbackrest``.


Bug fixes
+++++++++

- Fix deletion of pgbackrest include directory upon ``site-configure
  uninstall``: the command previously emitted a warning and the directory was
  left empty; now it is correctly removed.


Removals
++++++++

- The ``{version}`` template variable is once again required in
  ``postgresql.datadir`` and ``postgresql.waldir`` settings.
- Option ``--pgbackrest-restore-stanza`` got removed as it is confusing now
  that ``--pgbackrest-stanza`` option is required.


Misc.
+++++

- Set project's development status to *beta*.


v0.33.0 - 2023-04-14
~~~~~~~~~~~~~~~~~~~~

Features
++++++++

- Attributes CREATEROLE and CREATEDB can now be set when creating or altering
  roles.
- The ``version`` of an extension can now be specified.
- The temBoard logging can be configured via site settings with ``logpath``,
  ``logmethod`` and ``loglevel``.
  By default ``logmethod`` is set to ``stderr``. If ``file`` is selected, a
  logfile for each instance will be created in the ``logpath`` folder named
  ``temboard_agent_{qualname}.log``. ``loglevel`` can be set to ``DEBUG``,
  ``INFO``, ``WARNING``, ``ERROR`` or ``CRITICAL``.
- The option ``--pgbackrest-restore-stanza`` is now taken into account when
  using Patroni.
  Using this option will try to provision new standby from pgbackrest backups
  using `create_replica_methods
  <https://patroni.readthedocs.io/en/latest/replica_bootstrap.html#building-replicas>`_


Bug fixes
+++++++++

- Do not fail upon socket creation error while checking for port availability;
  emit a ``DEBUG`` log message instead in that case.
- Let the user-defined ``port`` take precedence over what's defined in
  postgresql.conf site template.


Removals
++++++++

- Change the ``completion`` command into a ``--completion=SHELL`` option to
  ``pglift``. This is now implemented as an eager callback which does not load
  site settings or any user data and can thus be safely used by any user (e.g.
  ``root``).
- After being marked as required extension schema field is optional again.


v0.32.0 - 2023-03-29
~~~~~~~~~~~~~~~~~~~~

Features
++++++++

- Add the ``logpath`` setting within PostgreSQL settings section.

  This new field allows to determine the directory containing log for our
  instances.

  The postgresql.conf template distributed with pglift now sets
  ``log_directory`` based on this field, along with a ``log_filename`` value
  that includes the instance qualified name (i.e. ``<version>-<name>``) as a
  prefix.
- Add ``cli.log_format`` and ``cli.date_format`` settings to control the format
  of log messages when writing to a file from the command-line interface.
- Add a ``--defaults/--no-defaults`` options to ``site-settings`` command to
  control whether default settings values should be shown, possibly along with
  site configuration.
- Add support for handling database schemas.
- Allow ``postgresql.datadir`` and ``postgresql.waldir`` settings to not contain
  the ``{version}`` template variable; only the ``{name}`` is required by now.
- Allow to set already encrypted password to a Role using
  ``--encrypted-password`` instead of ``--password``.
- A new rsyslog configuration option has been added to generate rsyslog
  config when running ``pglift site-configure install``.
- Logrotate configuration is now handled at site-configure step and no
  longer when creating/dropping an instance. The logorate configuration
  is now shared among the PostgreSQL instances and satellites components.
- The required ``ca_cert`` field has been added to the temBoard settings, it's part
  of the ``certificate`` field and must be defined as ``temboard.certificate.ca_cert``.
  This makes the use of ssl more consistent. It's used in the temBoard agent
  configuration file.


Bug fixes
+++++++++

- Fix crash upon early pglift command invocation when the creation of (CLI) log
  directory fails.
- Avoid starting a stopped instance when no role or database changes are needed.
- Do not override environment from parent process in ``instance exec``.
- Fix logrotate configuration file for Patroni, which was missing templating.
- Patroni ``postgresql.pgpass`` configuration item is now configurable with
  ``patroni.passfile`` site setting and defaults to ``etc/patroni/<instance
  qualname>.pgpass``. This passfile is deleted when instance is deleted.
- Fix a validation error when patroni watchdog device setting was not a file but a
  character device.


Removals
++++++++

- Remove possibility to template ``logpath`` setting for Patroni

  We remove the placeholder ``{name}`` from default value for patroni
  ``logpath`` setting. Using the ``{name}`` within the patroni logpath is no
  longer supported, we now always append the instance name at the end of the
  logpath.
- Extension schema field is now required. As a consequence, it's not possible to
  provide a list of extensions to install upon database creation in the CLI.
- Extensions now have a "state" field. To drop an extension from a database
  users now have to explicitly use "state: absent".
- ``log_directory`` for PostgreSQL is no longer created (automatically) by
  pglift.

  We remove the portion of code parsing the postgresql.conf and creating
  the corresponding log_directory. User should make sure the log_directory
  is present when they change this setting on postgresql.conf.
- In pgBackRest settings, ``ca_cert`` is now a part of certificate field.
  ``pgbackrest.repository.ca_cert`` should now be defined as
  ``pgbackrest.repository.certificate.ca_cert``.
- Pglift usage as root user is now prevented.

  According to PostgreSQL documentation, ``initdb`` or ``pg_ctl`` commands cannot
  be run as root.


Documentation
+++++++++++++

- The documentation explaining the steps to configure the site when using systemd
  in system mode has been changed to avoid calling pglift commands with ``sudo``.


Misc.
+++++

- Move command-line specific settings (``lock_file`` and ``logpath``) to a new
  ``cli`` field.


v0.31.0 - 2023-02-28
~~~~~~~~~~~~~~~~~~~~

Features
++++++++

- A new logrotate service has been added to generate logrotate configuration
  file for each instance.
- The ``passfile`` site setting, under ``postgresql.auth`` section now accepts a
  ``null`` value in order to completely disable support for the password file.
  When disabled, ``--pgpass`` option to ``role`` commands are no longer
  available.
- Validate existence of ``bindir`` fields set in ``postgresql.versions``
  setting.


Bug fixes
+++++++++

- Define the ``cluster_name`` in ``postgresql.conf`` template file, thus
  allowing to create instances without the value (which used to be hard-coded
  from instance name).


Removals
++++++++

- The ``pgpass`` field in ``roles`` items for an ``Instance`` is no longer
  supported (in Ansible or the declarative API). The field can still be
  specified on ``Role`` objects.
- To enable SSL in PostgreSQL configuration file, in addition to setting
  ``ssl`` to ``true``, providing ``ssl_cert_file`` and ``ssl_key_file`` is
  required. The previous self-signed certificate is no longer generated.
- No longer output the ``pgpass`` field when listing roles.


Documentation
+++++++++++++

- The commands for exporting the Ansible doc fragments have been simplified for
  the release workflow. Now it is only a copy of the data files already
  generated for the tests.
- Add a note about the ability for devs to run systemd jobs on sourcehut.
- Document sudo pre-requisites for systemd "system" mode with a sudoers entry example.


v0.30.0 - 2023-02-06
~~~~~~~~~~~~~~~~~~~~

Features
++++++++

- Make it possible to specify the schema in which a database extension would be installed.

  Until now, when an extension was added to a database, the extension's objects were
  installed by default on the current schema of the database (usually ``public``
  schema).

  Now, the name of the ``schema`` in which to install the extension's objects can be
  specified when adding or altering extensions, by specifying it in the manifest.
- Add a ``-f/--follow`` option to ``instance logs`` command to follow log output
  and log file change.
- Log create/alter/delete operations on database extensions.
- Add support for TLS encryption settings for patroni REST API.
- Log messages from pgBackRest commands: ``pgbackrest`` commands are now invoked
  with ``--log-level-stderr=info`` and respective messages are forwarded to
  pglift's logger at ``DEBUG`` level (as are all ``stderr`` messages from
  subprocesses).
- Configure pgBackRest on standby instances, even in ``repository.path``
  mode, removing a previous limitation from the implementation.

  In addition, when calling ``instance backup <instance>`` with ``<instance>``
  being a standby, ``pgbackrest`` is now invoked with ``--backup-standby``
  option.
- Setup pgbackrest on standby instances when using a remote repository.
- Add support for TLS for Etcd for HA with Patroni via site-settings.
- Make ``host_port`` and ``host_config`` item of pgbackrest's repo-host settings
  optional.
- Separate server from client pgbackrest configuration in remote repository
  mode.
- temboard-agent V8 is now needed for pglift, older versions are no longer supported.


Bug fixes
+++++++++

- Do not write the ``port`` value in ``postgresql.conf`` if it has the default
  value.
- If any change in the configuration files is detected for prometheus or temboard,
  we now perform a restart of the services for the changes to take effect.
- Fix possibly not working ``Exec`` command in postgresql systemd unit file.


Removals
++++++++

- If pgbackrest is enabled, the stanza name must now be provided upon instance
  creation.
- Temboard-agent SSL files are no longer auto-generated, their path must be provided
  in site-settings. The ``certificate`` field containing ``cert`` and ``key`` is
  required in temboard section.
- CLI option ``--extension`` of ``database alter`` command has been removed.
- CLI option ``--in-role`` of ``role alter`` command has been removed.
- Patroni etcd ``host`` setting has been replaced by ``hosts``.
- Configuration for etcd for HA with patroni is now managed in site settings.

  Etcd host can no longer be provided by user when creating an instance.


Documentation
+++++++++++++

- Update the Ansible tutorial to refer to the collection and simplify
  installation steps.
- Warn about the prerequisites for using ``systemctl --user``.
- Document patroni etcd ``hosts`` setting usage
- Document Patroni security (TLS support)
- Recommend to use systemd as a service manager when operating with pgBackRest
  in remote repository mode.


Misc.
+++++

- Add ``--pg1-path`` option to ``pgbackrest archive-push`` command set in
  PostgreSQL ``archive_command``.


v0.29.0 - 2022-12-30
~~~~~~~~~~~~~~~~~~~~

Features
++++++++

- Improve warning message when failing to connect to primary instance in
  ``instance get``.
- Make `replication` role a member of ``pg_read_all_stats``.
- Add WAL sender state (from `pg_stat_replication
  <https://www.postgresql.org/docs/current/monitoring-stats.html#MONITORING-PG-STAT-REPLICATION-VIEW>`_
  view) to standby information (as available in ``instance get`` command).
- Export paths to PostgreSQL data and WAL directories when getting an Instance
  (e.g. through ``instance get -o json`` command).
- Introduce ``$PGLIFT_CONFIG_PATH`` environment variable.

  This new variable allows users to provide a path to site configuration files
  to be taken into account prior to ``$XDG_CONFIG_HOME/pglift`` or
  ``/etc/pglift``.
- Preserve user edits of Patroni configuration file.
- Add support for pgbackrest remote host repository.


Bug fixes
+++++++++

- Catch JSON decode exception when parsing ``SETTINGS`` environment variable.

  This prevents showing a traceback when the json provided for ``SETTINGS``
  environment variable is invalid.
- Catch :class:`~pglift.exceptions.SettingsError` when loading site settings
  in CLI.

  Prevents displaying a traceback if there's an error when parsing the site
  settings YAML file.
- Fix path to pglift in systemd service when using pre-built binary

  `ExecPath` in ``pglift-postgresql@`` systemd service which was wrongly set
  to an inexistent path.


Removals
++++++++

- Require pgbackrest>=2.41

  ``pglift instance backups`` now runs ``pgbackrest info --set=<backup set>
  --output=json`` which only works since pgbackrest 2.41.
- Hide ``standby.status`` field from ``instance get`` output: this field is
  not very useful since it will only appear on standby instances, which are by
  definition in *demoted* state.
- Change priority order of site config files. Order is now xdg > etc > dist.
- Improve instance privileges command help message
- Drop `archive-push` section in global pgbackrest configuration.
- Replace ``pgbackrest.repopath`` setting by ``pgbackrest.repository``, now an
  object with keys ``path`` and ``retention`` (see ``pglift site-settings
  --schema`` for details). The ``path`` field is now required and has no default
  value, in contrast with ``repopath`` previously.
- The ``site-settings`` command output format is now YAML by default.


Documentation
+++++++++++++

- Add a section in docs for site configuration templates.
- Explain how base pgBackRest configuration is installed, and how to override
  it.
- Improve and clarify documentation about systemd in `system` mode.


Misc.
+++++

- Use pgbackrest's `recovery-option
  <https://pgbackrest.org/configuration.html#section-restore/option-recovery-option>`_
  when restoring a standby from a backup.
- Only restart PostgreSQL upon configuration changes, not all satellite
  services.


v0.28.0 - 2022-12-02
~~~~~~~~~~~~~~~~~~~~

Features
++++++++

- If pgbackrest is enabled, log install and uninstall operations at
  ``site-configure``.
- Configure systemd timer for instance backup with a randomized delay.
- Add a ``--dry-run`` option to `apply` commands.
- Add support for "force" option for database drop.
- Improve logging when starting/stopping Prometheus `postgres_exporter` and
  `temboard-agent`.
- Allow to pass any command to ``instance exec`` (not just Postgres commands
  or absolute ones as previously).
- Make it possible to operate normal instances even when `patroni` is enabled
  in site settings.
- Add support for PostgreSQL 15.
- Make check for port availability more robust.
- Improve `systemd` unit template for PostgreSQL. It is now defined as a
  ``Type=notify`` service and does not use a ``PIDFile`` anymore, following
  more closely what's suggested in `PostgreSQL documentation
  <https://www.postgresql.org/docs/current/server-start.html>`_.


Bug fixes
+++++++++

- pglift 0.27.0 is now the minimum required version for the Ansible
  collection.
- Fixed error during enabling/disabling temboard service with systemd caused by a
  bad service name.
- Fix error in ``instance env`` command for a standby instance with pgbackrest
  enabled.
- Only start Patroni once at instance creation (avoid a stop and a start).
  This should make concurrent setups (e.g. from Ansible targeting different
  hosts in parallel) work without dead-locking Patroni.
- Avoid starting / stopping PostgreSQL many times at instance creation.


Removals
++++++++

- The Ansible collection got moved to its `own repository
  <https://gitlab.com/dalibo/pglift-ansible>`_.
- Avoid useless ``pgbackrest start`` invocation after stanza creation.
- Separate management of shared_preload_libraries and database extensions.

  The ``extensions`` key in instance's model has been dropped. To install
  extensions in an instance, you now need to provide the
  ``shared_preload_libraries`` in instance settings.
- No longer error out, but simply warn, upon invalid Patroni configuration as
  reported by ``patroni --validate-config``.
- Only validate generated Patroni configuration for Patroni version higher than
  2.1.5.



Documentation
+++++++++++++

- Extend how to about standby management with Ansible to illustrate promote
  operation.
- Add some details about `site configuration` in installation documentation.


Misc.
+++++

- Add a hidden ``--debug`` command-line flag to set log level to ``DEBUG`` and
  eventually get tracebacks displayed.
- Unconditionally call ``pgbackrest stanza-create`` upon instance.
  re-configuration whereas this was previously only done at instance creation.
  Conversely, the ``--no-online`` option is used to avoid superfluous instance
  startup. On the other hand the ``pgbackrest check`` command is still only
  emitted at instance creation.
- Add ``--output=json`` option to ``postgres_exporter apply`` command.
- Rework systemd installation through site-configure hook.
- Use pglift CLI in systemd unit for PostgreSQL.
- Use `towncrier <https://towncrier.readthedocs.io/>`_ to manage news
  fragments.


v0.27.0 - 2022-11-02
~~~~~~~~~~~~~~~~~~~~

Features
++++++++

- Support for RockyLinux 9
- Ability to provide a name for pgbackrest stanza
- Handling of ``REASSIGN OWNED`` and ``DROP OWNED`` when dropping a role
- Better handling of model validation errors in the CLI
- Ability to create a database as a clone of an existing one
- JSON output to ``instance env`` command
- JSON output to ``apply`` sub-commands
- Prometheus password change upon ``instance alter``
- Prometheus password kept upon instance upgrade
- Raise a specific error if role being dropped has dependent database objects
- Raise a specific error when Postgres binary directory for requested version
  does not exist

Bug fixes
+++++++++

- ``SETTINGS`` environment variable takes precedence over YAML setting file
- Fix systemd service name for Patroni-managed instances
- Fix service name inconsistency for temboard-agent
- Entries of ``postgresql.conf``, set by ``initdb``, no longer commented
- Fix a type error when retrieve instance environment from Ansible module
- Replication password passed through environment when invoking
  ``pg_basebackup``

Removals
++++++++

- Field ``pgbackrest_restore`` excluded from ``instance get`` command output
- Database auto discover in default postgres_exporter configuration
- CLI option ``--json``, replaced by ``--output-format=json``
- Instance model's ``configuration``, renamed as ``settings``, to be
  consistent with eponymous field on Database objects
- Standby's ``for`` field renamed as ``primary_conninfo`` in the declarative
  API

Documentation
+++++++++++++

- Added an example playbook for a standby instance
- Fix settings in Ansible tutorial (``pgpass`` fields missing for ``surole``
  and ``backuprole``)

Misc.
+++++

- Limit database connection openings in ``instance get``
- Installation of global pgbackrest configuration through ``site-configure``
  command
- Setting ``postgresql.versions`` now defined as a list
- Use pglift CLI in Ansible modules, instead of the Python API
- PyOxidizer configuration to build a binary version of pglift
