PostgreSQL authentication
=========================

In site settings, the ``postgresql.auth`` field allows to configure PostgreSQL
authentication. Default values are:

.. code-block:: yaml

    auth:
      local: trust
      host: trust
      hostssl: trust
      passfile: $HOME/.pgpass
      password_command: []

For a production cluster it is recommended to set ``local``, ``host`` and
``hostssl`` authentication to one of the supported `authentication methods`_.

In addition, a site administrator may provide templates for ``pg_hba.conf``
and ``pg_ident.conf`` (as documented in
:ref:`configuration templates <configuration_templates>` section). The defaults
contain:

.. literalinclude:: ../../../src/pglift/postgresql/pg_hba.conf
   :caption: postgresql/pg_hba.conf

.. literalinclude:: ../../../src/pglift/postgresql/pg_ident.conf
   :caption: postgresql/pg_ident.conf

Many `pglift` operations require a database access to the target instance using
the super-user role (``postgres`` by default). Unless the authentication policy
is set to ``trust`` a password would then be required for each operations.

In site settings, the ``postgresql.surole.pgpass`` configuration option, when
set to ``true``, will write a `password file`_ (``pgpass``) entry for the
super-user role. This assumes that the ``postgresql.auth.passfile`` option is
non-``null``.

At instance creation, one can define a password for the super-user role
(``postgres`` by default), using ``--surole-password`` option to ``pglift
instance create`` or similarly through the Ansible interface.

When the password file is used, nothing special is required for authentication
as all libpq operations would use it.

Otherwise, the password is read from ``PGPASSWORD`` environment variable so
this should be set in the environment running interactive commands.

Alternatively, one can use the ``password_command`` setting, with a value
defining a user-managed shell command as a list of strings. At runtime, the
command is templated with the instance object (which string representation
would be something like ``14/main``) and the role name (e.g. ``postgres``,
``backup``). It must return the role password as stdout.

Examples:

.. code-block:: yaml

    auth:
      password_command:
        - jq
        - -r
        - .["{instance}"]["{role}"]
        - /mnt/secrets/pglift.json

.. code-block:: yaml

    auth:
      password_command:
        - gpg
        - -d
        - /var/lib/pgsql/{instance.version}-{instance.name}_{role}_pgpassword.gpg



Setting up "peer" authentication
--------------------------------

The `peer authentication`_ is convenient but it needs additional setup when
the local user name does not match role name, typically when not using the ``postgres``
or ``backup`` system user in default configuration. In that case, a mapping_
is usually needed.

Such a setup can be achieved by providing template files (as documented in
:ref:`configuration templates <configuration_templates>` section)
in order to map the local user running pglift (referred to as the `sysuser`)
to PostgreSQL super-user role (typically ``postgres``), identified by
``{surole}`` template variable or backup user, identified by ``{backuprole}``
template variable:

.. code-block:: none
   :caption: pg_hba.conf

    local    all    {surole}       peer    map=mymap
    local    all    {backuprole}  peer    map=mymap
    [...]

.. code-block:: none
   :caption: pg_ident.conf

    # MAPNAME       SYSTEM-USERNAME         PG-USERNAME
    mymap           {sysuser}               {surole}
    mymap           {sysuser}               {backuprole}


Available template variables are:

* ``{sysuser}``: the local user running pglift
* ``{surole}``: the PostgreSQL super-user role
* ``{replrole}``: the PostgreSQL replication role
* ``{backuprole}``: the PostgreSQL backup role


.. _`password file`: https://www.postgresql.org/docs/current/libpq-pgpass.html
.. _`authentication methods`: https://www.postgresql.org/docs/current/auth-methods.html
.. _`peer authentication`: https://www.postgresql.org/docs/current/auth-peer.html
.. _`mapping`: https://www.postgresql.org/docs/current/auth-username-maps.html
