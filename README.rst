The Qogecoin docs
=================

This repository contains the documentation for the Qogecoin project.

Building the docs
-----------------

Install the requirements:

.. code-block:: bash

   pip install -r requirements.txt
   pre-commit install

Remove the entire build folder:

.. code-block:: bash

   rm -rd build

Rebuild the docs:

.. code-block:: bash

   sphinx-build -b html source build

We run formatters as part of the pre-commit hooks, so it is recommended to run
the hooks manually before commiting.

.. code-block:: bash

   pre-commit run --all-files

Changing dependencies
---------------------

We currently do not use bazel to generate the docs, but we use ``rules_python``
to generate hash-locked requirement files.

If you change dependencies in ``requirements.in``, rebuild ``requirements.txt``:

.. code-block:: bash

   bazel run @docs//:requirements.update
