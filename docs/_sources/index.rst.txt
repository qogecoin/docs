Qogecoin Core 0.14.2
=====================

.. figure:: _static/qoge.png
   :width: 256
   :align: center

Qogecoin Core is the original Qogecoin client and it builds the backbone of the
network. However, it downloads and stores the entire history of Qogecoin
transactions; depending on the speed of your computer and network connection,
the synchronization process can take anywhere from a few hours to a day or more.

Precompiled binaries are available at `<https://github.com/qogecoin/qogecoin/releases>`_.

Discord: `<https://discord.gg/T8uYSDmtde>`_.

Running
---------------------
The following are some helpful notes on how to run Qogecoin on your native
platform.

Unix
----

Unpack the files into a directory and run ``bin/qogecoin-qt`` (GUI) or
``bin/qogecoind`` (headless).

Windows
-------

Unpack the files into a directory, and then run qogecoin-qt.exe.

Need Help?
----------

* See the documentation at the `Qogecoin Wiki <https://qogecoin.org>`_ for help
   and more information.
* Ask for help on `BitcoinTalk <https://qogecointalk.io/>`_ forums.

Building
--------
The following are developer notes on how to build Qogecoin for your native
platform. They are not complete guides, but include notes on the necessary
libraries, compile flags, etc.

.. toctree::
   :maxdepth: 1

   build-unix
   build-windows

Development
-----------

The `Qogecoin docs <https://qogecoin.org>`_ contains relevant
information on the development process and automated testing.

.. - [Source Code Documentation (External Link)](https://dev.visucore.com/qogecoin/doxygen/)

.. toctree::
   :maxdepth: 1

   REST-interface
   dnsseed-policy
   benchmarking


Miscellaneous
-------------

.. toctree::
   :maxdepth: 1

   files
   fuzzing
   reduce-traffic
   tor
   init
   zmq

Guides
------

.. toctree::
   :maxdepth: 1

   back-up-wallet


License
-------

Distributed under the `MIT software license
<https://github.com/qogecoin/qogecoin/blob/main/COPYING>`_.
This product includes software developed by the OpenSSL Project for use in the
`OpenSSL Toolkit <https://www.openssl.org/>`_. This product includes
cryptographic software written by Eric Young
(`eay@cryptsoft.com <mailto:eay@cryptsoft.com>`_), and UPnP software written by
Thomas Bernard.
