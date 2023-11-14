.. _pgconf:

PostgreSQL configuration
========================

The PostgreSQL configuration of instances created by pglift is *managed* as
explained in respective section about :ref:`site configuration
<postgresql-site-configuration>`. This means that the overall configuration of
an instance is built from several sources:

- actual ``postgresql.conf`` present in instance data directory,
- the site-wise ``postgresql.conf`` template file,
- any configuration items that satellite components might define (e.g.
  pgBackRest would set ``archive_command`` etc.),
- user-supplied configuration items.

This process applies at instance creation, but also happens anytime the
instance is updated through pglift's API (be it ``instance alter`` command,
the ``pgconf`` command set described below, or the declarative Ansible
interface).

Accordingly:

- when a change is passed through user-supplied configuration items (either
  from the declarative API or from ``pgconf set|edit`` commands), these take
  precedence;

- when removing a configuration item (either through the declarative API or
  from ``pgconf remove`` command), this will apply only if the same
  setting is not defined in a previous source (e.g. ``postgresql.conf``
  template);

- so, to effectively remove a configuration item, one needs to *reset* it to its
  default value (e.g. if the site template sets ``work_mem`` to 32MB but you
  want to set it back to its default value of 4MB, then you would have to
  override the template value with ``pglift pgconf [...] set work_mem=4MB``).

.. warning::
   Editing ``postgresql.conf`` file in data directory directly might result in
   surprising effects upon further instance change: typically, a setting
   removed from the configuration file through direct edition might come back
   after applying back the instance state.

``pgconf`` commands
-------------------

The ``pglift pgconf`` command line entry point exposes commands to manage
configuration of a PostgreSQL instance.

.. code-block:: console

    $ pglift pgconf --help
    Usage: pglift pgconf [OPTIONS] COMMAND [ARGS]...

      Manage configuration of a PostgreSQL instance.

    Options:
      -i, --instance <version>/<name>
                                      Instance identifier; the <version>/ prefix
                                      may be omitted if there's only one instance
                                      matching <name>. Required if there is more
                                      than one instance on system.
      --help                          Show this message and exit.

    Commands:
      edit    Edit managed configuration.
      remove  Remove configuration items.
      set     Set configuration items.
      show    Show configuration (all parameters or specified ones).

It operates only on configuration files and does not assume that the instance
is started. To make changes effective, the user may need to restart or reload
the instance, see :doc:`/user/ops/instance`.

.. warning:: Some configuration settings should not be modified through this
   command as they may be needed for other satellite services to work.
   Typically, the ``port`` setting is one of them. Similarly, the selected
   backup system may assume that some parameter are set to particular values.

Show the configuration
^^^^^^^^^^^^^^^^^^^^^^

View parameters:

.. code-block:: console

    $ pglift pgconf -i main show log_connections log_disconnections
    # log_connections = off
    # log_disconnections = off

View all parameters:

.. code-block:: console

    $ pglift pgconf -i main show
    archive_command = '/usr/bin/pgbackrest --config-path=/etc/pgbackrest --stanza=14-main archive-push %p'
    archive_mode = on
    wal_level = 'replica'
    cluster_name = 'main'
    shared_buffers = '128MB'
    effective_cache_size = '5 GB'
    unix_socket_directories = '/var/run/postgresql'
    log_destination = 'stderr'
    logging_collector = on
    port = 5454
    max_connections = 100
    dynamic_shared_memory_type = 'posix'
    max_wal_size = '1GB'
    min_wal_size = '80MB'
    log_timezone = 'Europe/Paris'
    datestyle = 'iso, mdy'
    timezone = 'Europe/Paris'
    lc_messages = 'C'
    lc_monetary = 'C'
    lc_numeric = 'C'
    lc_time = 'C'
    default_text_search_config = 'pg_catalog.english'

Change the configuration
^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: console

    $ pglift pgconf -i main set log_connections=on log_disconnections=on
    INFO     configuring PostgreSQL
    INFO     instance 14/main needs reload due to parameter changes: log_connections, log_disconnections
    INFO     reloading PostgreSQL configuration for 14-main
    log_connections: None -> True
    log_disconnections: None -> True

.. note::
    To directly edit the configuration file, use:

    .. code-block:: console

        $ pglift pgconf -i main edit

    this will open your text editor with the configuration.

Remove parameters configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: console

  $ pglift pgconf -i main remove log_connections log_disconnections
  INFO     configuring PostgreSQL
  INFO     instance 14/main needs reload due to parameter changes: log_connections, log_disconnections
  INFO     reloading PostgreSQL configuration for 14-main
  log_connections: True -> None
  log_disconnections: True -> None
