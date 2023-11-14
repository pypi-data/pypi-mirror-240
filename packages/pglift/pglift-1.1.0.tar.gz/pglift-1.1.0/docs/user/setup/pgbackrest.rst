pgBackRest site configuration
=============================

pgBackRest satellite component can be enabled through site settings by
defining a ``pgbackrest`` key, e.g.:

.. code-block:: yaml
   :name: pgbackrest-settings
   :caption: settings.yaml

    pgbackrest:
      execpath: /usr/local/bin/pgbackrest
      repository:
        mode: path
        path: /backups

.. note::
   The ``repository`` key is required, along with the ``mode`` one underneath.

.. note::
   See :ref:`settings schema <settings-schema>` for further information about
   available configuration and their model.

pgBackRest integration in pglift supports two *repository* modes:

1. a *local* repository, configured with a ``path`` key as in the above
   example, and,
2. a *remote* repository.

.. _pgbackrest-base-site-configuration:

Site configuration
------------------

In any repository mode, running the ``site-configure`` command is required
after settings definition in order to (at least) install base pgbackrest
configuration file and directories.

The base pgBackRest configuration is installed site-wise from a template
(which may be :ref:`overridden <configuration_templates>`). The default
``pgbackrest.conf`` template file contains:

.. literalinclude:: ../../../src/pglift/pgbackrest/pgbackrest.conf
   :language: ini
   :caption: pgbackrest/pgbackrest.conf

PostgreSQL configuration is handled through parameters set in
``postgresql.conf`` file as documented in :ref:`PostgreSQL site
configuration <postgresql-site-configuration>`. The default values for those
parameters are:

.. literalinclude:: ../../../src/pglift/postgresql/pgbackrest.conf

and can be overridden by providing a ``postgresql/pgbackrest.conf`` template
file in site configuration directory (see :ref:`configuration templates
<configuration_templates>`).

Local repository mode
---------------------

In this mode, site settings must contain a ``repository.path`` key and
``repository.mode`` must have ``path`` as value as in the
:ref:`above example <pgbackrest-settings>`.

Upon instance creation, pgBackRest is set up by:

* adding some configuration to PostgreSQL,
* writing a pgBackRest configuration file for this instance, and,
* initializing the pgBackRest stanza in the repository.

Remote repository mode
----------------------

In this mode, you can either use `TLS with client certificates` or
`passwordless SSH` to enable communication between the hosts.

TLS
~~~

To enable TLS support, ``repository.mode`` must be set to ``host-tls``. And
a few more information must be provided.

.. code-block:: yaml
   :name: pgbackrest-repo-host-tls-settings
   :caption: settings.yaml

    pgbackrest:
      configpath: /conf/pgbackrest
      repository:
        mode: host-tls
        host: backup-srv.pginfra.dalibo.com
        cn: backup-srv
        certificate:
          ca_cert: /etc/ssl/certs/my-ca.crt
          cert: /etc/ssl/certs/local.crt
          key: /etc/ssl/private/local.key

Upon site configuration, through invocation of the ``site-configure`` command,
in addition to the :ref:`base site configuration
<pgbackrest-base-site-configuration>`, a pgBackRest TLS server is configured
and started. This server will be consumed by pgBackRest client commands such
as ``pgbackrest backup``, typically run on configured ``repository.host``. The
``certificate`` key in :ref:`above settings <pgbackrest-repo-host-tls-settings>`
will be used to configure this (on site) server.

.. warning::
   The process started during ``site-configure`` should be kept running
   alongside all instances on site and thus probably get started on boot. As
   such, it is best to use a service manager such as :ref:`systemd
   <systemd-setup>` in this context.

Upon instance creation, in addition to WAL archiving configuration on
PostgreSQL side, the local stanza configuration is written on site.

Typically, further configuration will be needed on the *remote* repository
host to:

* add or extend the stanza configuration, typically at least (where emphasized
  lines are to be determined from the database host server, managed by pglift):

  .. code-block:: ini
     :caption: /etc/pgbackrest/conf.d/my-stanza.conf
     :emphasize-lines: 2,3,4,8,9,10

     [my-stanza]
     pg1-host = pghost1
     pg1-host-type = tls
     pg1-host-config-path = /conf/pgbackrest
     pg1-host-ca-file = ...
     pg1-host-cert-file = ...
     pg1-host-key-file = ...
     pg1-path = /srv/pgsql/15/main/data
     pg1-user = backup
     pg1-socket-path = /run/user/100/pglift/postgresql

* run ``pgbackrest stanza-create``, in case of a new stanza, or ``pgbackrest
  stanza-upgrade`` if upgrading, and

* run a ``pgbackrest check`` to make sure things are working as expected.

Finally, it's usually a good idea to run a ``pgbackrest check`` on the
database host as well:

.. code-block:: bash

    $ export $(pglift instance env main)
    $ pgbackrest check

Passwordless SSH
~~~~~~~~~~~~~~~~

To enable SSH support, the repository mode must be set to ``host-ssh``.

.. code-block:: yaml
   :caption: settings.yaml

    pgbackrest:
      configpath: /conf/pgbackrest
      repository:
        mode: host-ssh
        host: backup-srv.pginfra.dalibo.com


For it to work, ``pgbackrest`` user needs to be able to connect from the
repository host to the database host via SSH. And the user running ``pglift``
needs to be able to do the same from database host to repository host.
Basically, this needs SSH keys to be exchanged between database host and
repository host.

Please refer to ``pgBackRest`` `documentation
<https://pgbackrest.org/user-guide.html#repo-host/setup-ssh>`_.
