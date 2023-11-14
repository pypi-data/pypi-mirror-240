======
pglift
======

Welcome to pglift's documentation.

pglift provides a command-line interface and an Ansible collection to deploy
and manage production-ready instances of PostgreSQL.

An "instance", in pglift terminology, is composed of a PostgreSQL cluster
complemented by a number of satellite components providing additional services
such as backup or monitoring. By default, pglift simply deploys and manage
PostgreSQL and all supported components are optional.

pglift is configurable on site thus making instance management uniform across
an infrastructure.

Get started with :ref:`Installation <install>` and then get an overview
with the :ref:`Quickstart <quickstart>`.


For more, head out to more in-depth tutorials and user guides below.

.. toctree::
    :titlesonly:
    :caption: Getting started
    :hidden:

    install
    quickstart

.. toctree::
    :maxdepth: 1
    :caption: Tutorials

    tutorials/cli
    tutorials/ansible

.. toctree::
    :maxdepth: 1
    :caption: User guides

    user/setup/index
    user/ops/index

.. toctree::
    :maxdepth: 1
    :caption: Reference

    explanation/settings-vs-interface-model
    api/index

.. toctree::
    :maxdepth: 1
    :caption: How to guides

    howto/instance-shell
    howto/instance-env
    howto/instance-logs
    howto/database-backup-restore
    howto/database-maintenance
    howto/standby-setup
    howto/major-online-upgrade
    howto/shell-completion
    dev

.. toctree::
    :maxdepth: 1
    :caption: About

    news


.. rubric:: Indices and tables

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
