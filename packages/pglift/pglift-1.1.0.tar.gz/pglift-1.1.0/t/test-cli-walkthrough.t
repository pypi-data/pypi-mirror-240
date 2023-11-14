Site settings:

  $ cat > $TMPDIR/passwords.json << 'EOF'
  > {
  >   "main": {
  >     "postgres": "s3per"
  >   }
  > }
  > EOF
  $ cat > $TMPDIR/temboard-signing.key << EOF
  > -----BEGIN PUBLIC KEY-----
  > MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQChaZFhzRuFgNDLgAJ2+WQsVQ75
  > G9UswuVxTfltxP4mc+ou8lyj7Ck73+M3HkFE2r623g6DZcNYCXqpyNpInsBo68kD
  > IDgwHKaQBTPyve0VhNjkJyqoKIC6AJKv/wixEwsHUm/rNU8cXnY7WCNGjCV+JrEm
  > ekHBWP1X4hFfPKcvvwIDAQAB
  > -----END PUBLIC KEY-----
  > EOF
  $ mkdir $TMPDIR/temboard-ssl
  $ python -m trustme -q -d $TMPDIR/temboard-ssl
  $ cat > $TMPDIR/config.json <<EOF
  > {
  >   "cli": {
  >     "log_format": "%(levelname)-4s %(message)s"
  >   },
  >   "prefix": "$TMPDIR",
  >   "run_prefix": "$TMPDIR/run",
  >   "postgresql": {
  >     "auth": {
  >       "local": "scram-sha-256",
  >       "passfile": "$TMPDIR/.pgpass",
  >       "password_command": [
  >         "jq",
  >         "-r",
  >         ".{instance.name}.{role}",
  >         "$TMPDIR/passwords.json"
  >       ]
  >     },
  >     "backuprole": {
  >       "name": "pgbackrest"
  >     }
  >   },
  >   "pgbackrest": {
  >     "repository": {
  >       "mode": "path",
  >       "path": "$TMPDIR/pgbackrest",
  >       "retention": {
  >         "archive": 3
  >       }
  >     }
  >   },
  >   "powa": {
  >     "role": "pwa"
  >   },
  >   "prometheus": {
  >     "execpath": "/usr/bin/prometheus-postgres-exporter"
  >   },
  >   "temboard": {
  >     "ui_url": "http://localhost:9999",
  >     "signing_key": "$TMPDIR/temboard-signing.key",
  >     "certificate": {
  >       "ca_cert": "$TMPDIR/temboard-ssl/client.pem",
  >       "cert": "$TMPDIR/temboard-ssl/server.pem",
  >       "key": "$TMPDIR/temboard-ssl/server.key"
  >     },
  >     "execpath": "$(which temboard-agent)"
  >   }
  > }
  > EOF

Make sure password_command works:
  $ jq -r ".main.postgres" $TMPDIR/passwords.json
  s3per

  $ export SETTINGS="@$TMPDIR/config.json"
  $ pglift site-settings -o json \
  >   | jq '.postgresql.auth, .prometheus, .run_prefix, .prefix'
  {
    "local": "scram-sha-256",
    "host": "trust",
    "hostssl": "trust",
    "passfile": "$TMPDIR/.pgpass",
    "password_command": [
      "jq",
      "-r",
      ".{instance.name}.{role}",
      "$TMPDIR/passwords.json"
    ]
  }
  {
    "execpath": "/usr/bin/prometheus-postgres-exporter",
    "role": "prometheus",
    "configpath": "$TMPDIR/etc/prometheus/postgres_exporter-{name}.conf",
    "queriespath": null,
    "pid_file": "$TMPDIR/run/prometheus/{name}.pid"
  }
  "$TMPDIR/run"
  "$TMPDIR"

  $ alias pglift="pglift --non-interactive --log-level=info"

  $ pglift site-configure install
  INFO creating temboard log directory
  INFO installing base pgbackrest configuration
  INFO creating pgbackrest include directory
  INFO creating pgbackrest repository path
  INFO creating common pgbackrest directories
  INFO creating postgresql log directory

  $ trap "pglift --non-interactive instance drop main; \
  >   port-for -u postgres; \
  >   port-for -u temboard; \
  >   port-for -u prometheus" \
  >   EXIT

Define ports:

  $ PGPORT=$(port-for postgres)
  $ PGEPORT=$(port-for prometheus)
  $ TBPORT=$(port-for temboard)

Create an instance

  $ pglift instance create main \
  >   --port=$PGPORT --surole-password=s3per \
  >   --pgbackrest-stanza=main --pgbackrest-password='b@ck up!' \
  >   --prometheus-port=$PGEPORT \
  >   --temboard-port=$TBPORT --temboard-password='t3Mb0@rd'
  INFO initializing PostgreSQL
  INFO configuring PostgreSQL authentication
  INFO configuring PostgreSQL
  INFO starting PostgreSQL 1\d-main (re)
  INFO creating role 'temboardagent'
  INFO creating role 'pwa'
  INFO creating role 'prometheus'
  INFO creating role 'pgbackrest'
  INFO altering role 'pgbackrest'
  INFO creating 'powa' database in 1\d\/main (re)
  INFO creating extension 'btree_gist' in database powa
  INFO creating extension 'pg_qualstats' in database powa
  INFO creating extension 'pg_stat_statements' in database powa
  INFO creating extension 'pg_stat_kcache' in database powa
  INFO creating extension 'powa' in database powa
  INFO configuring temboard agent 1\d-main (re)
  INFO configuring Prometheus postgresql 1\d-main (re)
  INFO configuring pgBackRest stanza 'main' for pg1-path=\$TMPDIR\/srv\/pgsql\/1\d\/main\/data (re)
  INFO creating pgBackRest stanza main
  INFO starting temboard-agent 1\d-main (re)
  INFO starting Prometheus postgres_exporter 1\d-main (re)

List instances

  $ pglift instance list -o json | jq '.[] | .name, .status'
  "main"
  "running"

Get the status of an instance:

  $ pglift --debug instance status main
  DEBUG instance 'main' not found in version 1\d (re)
  DEBUG instance 'main' not found in version 1\d (re)
  DEBUG instance 'main' not found in version 1\d (re)
  DEBUG instance 'main' not found in version 1\d (re)
  DEBUG logging command at \$TMPDIR/log/\d+.\d+.log (re)
  DEBUG looking for 'temboard_agent@1\d-main' service status by its PID at \$TMPDIR\/run\/temboard-agent\/temboard-agent-1\d-main.pid (re)
  DEBUG looking for 'postgres_exporter@1\d-main' service status by its PID at \$TMPDIR\/run\/prometheus\/1\d-main.pid (re)
  DEBUG get status of PostgreSQL instance 1\d\/main (re)
  DEBUG \/usr\/lib\/postgresql\/1\d\/bin\/pg_ctl status -D \$TMPDIR\/srv\/pgsql\/1\d\/main\/data (re)
  PostgreSQL: running
  prometheus: running
  temBoard: running

Alter an instance:

  $ pglift instance stop
  INFO stopping PostgreSQL 1\d-main (re)
  INFO stopping temboard-agent 1\d-main (re)
  INFO stopping Prometheus postgres_exporter 1\d-main (re)
  $ pglift instance alter --data-checksums
  INFO configuring PostgreSQL
  INFO enabling data checksums
  $ pglift instance start
  INFO starting PostgreSQL 1\d-main (re)
  INFO starting temboard-agent 1\d-main (re)
  INFO starting Prometheus postgres_exporter 1\d-main (re)
  $ pglift instance get -o json \
  >   | jq '.data_checksums, .port, .prometheus, .settings.unix_socket_directories, .state'
  true
  \d+ (re)
  {
    "port": \d+ (re)
  }
  "$TMPDIR/run/postgresql"
  "started"

PostgreSQL configuration

  $ pglift pgconf show port logging_collector
  port = \d+ (re)
  logging_collector = on
  $ pglift --non-interactive pgconf set log_statement=all
  INFO configuring PostgreSQL
  INFO instance 1\d\/main needs reload due to parameter changes: log_statement (re)
  INFO reloading PostgreSQL configuration for 1\d-main (re)
  log_statement: None -> all
  $ pglift pgconf show log_statement
  log_statement = 'all'
  $ pglift --non-interactive pgconf remove log_statement
  INFO configuring PostgreSQL
  INFO instance 1\d\/main needs reload due to parameter changes: log_statement (re)
  INFO reloading PostgreSQL configuration for 1\d-main (re)
  log_statement: all -> None
  $ pglift pgconf show log_statement
  # log_statement = 'all'


Roles

Add and manipulate roles:

  $ pglift role -i main create dba --login --pgpass --password=qwerty
  INFO creating role 'dba'
  INFO adding an entry for 'dba' in \$TMPDIR\/.pgpass \(port=\d+\) (re)

  $ cat $TMPDIR/.pgpass
  \*:\d+:\*:dba:qwerty (re)

  $ pglift role get dba -o json
  {
    "name": "dba",
    "has_password": true,
    "inherit": true,
    "login": true,
    "superuser": false,
    "createdb": false,
    "createrole": false,
    "replication": false,
    "connection_limit": null,
    "validity": null,
    "in_roles": [],
    "pgpass": true
  }

  $ PGDATABASE=postgres PGUSER=dba PGPASSWORD= \
  >   pglift instance exec main -- psql -c "SELECT current_user;"
   current_user 
  --------------
   dba
  (1 row)
  

  $ pglift role alter dba --connection-limit=10 --inherit --no-pgpass
  INFO altering role 'dba'
  INFO removing entry for 'dba' in \$TMPDIR\/.pgpass \(port=\d+\) (re)

  $ pglift role get dba -o json
  {
    "name": "dba",
    "has_password": true,
    "inherit": true,
    "login": true,
    "superuser": false,
    "createdb": false,
    "createrole": false,
    "replication": false,
    "connection_limit": 10,
    "validity": null,
    "in_roles": [],
    "pgpass": false
  }

Databases

  $ pglift database create myapp --owner dba --schema app
  INFO creating 'myapp' database in 1\d\/main (re)
  INFO creating schema 'app' in database myapp

  $ pglift database get myapp -o json
  {
    "name": "myapp",
    "owner": "dba",
    "settings": null,
    "schemas": [
      {
        "name": "app",
        "owner": "postgres"
      },
      {
        "name": "public",
        "owner": "pg_database_owner"
      }
    ],
    "extensions": [],
    "publications": [],
    "subscriptions": [],
    "tablespace": "pg_default"
  }

  $ pglift database run -d myapp \
  >     "CREATE SCHEMA hollywood CREATE TABLE films (title text, release date, awards text[]) CREATE VIEW winners AS SELECT title, release FROM films WHERE awards IS NOT NULL;"
  INFO running "CREATE SCHEMA hollywood CREATE TABLE films \(title text, release date, awards text\[\]\) CREATE VIEW winners AS SELECT title, release FROM films WHERE awards IS NOT NULL;" on myapp database of 1\d\/main (re)
  INFO CREATE SCHEMA

  $ pglift database run -d myapp \
  >     "ALTER DEFAULT PRIVILEGES IN SCHEMA hollywood GRANT ALL ON TABLES TO dba"
  INFO running "ALTER DEFAULT PRIVILEGES IN SCHEMA hollywood GRANT ALL ON TABLES TO dba" on myapp database of 1\d\/main (re)
  INFO ALTER DEFAULT PRIVILEGES

  $ pglift instance privileges main --default -o json
  [
    {
      "database": "myapp",
      "schema": "hollywood",
      "object_type": "TABLE",
      "role": "dba",
      "privileges": [
        "DELETE",
        "INSERT",
        "REFERENCES",
        "SELECT",
        "TRIGGER",
        "TRUNCATE",
        "UPDATE"
      ]
    }
  ]

  $ pglift database run -d myapp \
  >     "INSERT INTO hollywood.films VALUES ('Blade Runner', 'June 25, 1982', '{\"Hugo Award\", \"Saturn Award\"}');"
  INFO running "INSERT INTO hollywood.films VALUES \('Blade Runner', 'June 25, 1982', '{"Hugo Award", "Saturn Award"}'\);" on myapp database of 1\d\/main (re)
  INFO INSERT 0 1
  $ PGDATABASE=myapp pglift instance exec main -- \
  >     psql -c "SELECT * FROM hollywood.winners ORDER BY release ASC;"
      title     |  release   
  --------------+------------
   Blade Runner | 1982-06-25
  (1 row)
  

  $ pglift database dump myapp
  INFO backing up database 'myapp' on instance 1\d\/main (re)

  $ pglift database drop myapp
  INFO dropping 'myapp' database

Cleanup.
  INFO dropping instance 1\d\/main (re)
  INFO stopping PostgreSQL 1\d-main (re)
  INFO stopping temboard-agent 1\d-main (re)
  INFO stopping Prometheus postgres_exporter 1\d-main (re)
  INFO deconfiguring temboard agent
  INFO deconfiguring Prometheus postgres_exporter 1\d-main (re)
  INFO deconfiguring pgBackRest
  INFO removing entries matching port=\d+ from \$TMPDIR\/.pgpass (re)
  INFO removing now empty $TMPDIR/.pgpass
  INFO deleting PostgreSQL cluster (no-eol)
