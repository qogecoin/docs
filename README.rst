The Qogecoin docs
=================

This repository contains the documentation for the Qogecoin project, available
at `<https://www.qogecoin.org>`_.

Building the docs
-----------------

Install the requirements::

   pip install -r requirements.txt
   pre-commit install

Remove the entire build folder::

   rm -rd docs

Rebuild the docs::

   sphinx-build -b html source docs

We run formatters as part of the pre-commit hooks, so it is recommended to run
the hooks manually before commiting::

   pre-commit run --all-files

Changing dependencies
---------------------

We currently do not use bazel to generate the docs, but we use ``rules_python``
to generate hash-locked requirement files.

If you change dependencies in ``requirements.in``, rebuild
``requirements.txt``::

   bazel run @docs//:requirements.update
