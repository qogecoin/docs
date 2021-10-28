Building on Linux
=================

Some notes on how to build Qogecoin Core in Unix.

.. note::
   Always use absolute paths to configure and compile qogecoin and the
   dependencies, for example, when specifying the path of the dependency:

   .. code-block:: bash

      ../dist/configure \
           --enable-cxx \
           --disable-shared \
           --with-pic \
           --prefix=$BDB_PREFIX

   Here ``BDB_PREFIX`` must be an absolute path - it is defined using ``$(pwd)``
   which ensures the usage of the absolute path.

To Build
--------

.. code-block:: bash

   ./autogen.sh
   ./configure
   make
   make install # optional

This will build qogecoin-qt as well if the dependencies are met.

Dependencies
------------

These dependencies are required:

+-------------+-----------------+----------------------------------------------+
| Library     | Purpose         | Description                                  |
+=============+=================+==============================================+
| ``libssl``  | Crypto          | Random Number Generation, Elliptic Curve     |
|             |                 | Cryptography                                 |
+-------------+-----------------+----------------------------------------------+
| ``libboost``| Utility         | Library for threading, data structures, etc  |
+-------------+-----------------+----------------------------------------------+
| ``libevent``| Networking      | OS independent asynchronous networking       |
+-------------+-----------------+----------------------------------------------+

Optional dependencies:

+---------------+------------------+-------------------------------------------+
|Library        | Purpose          | Description                               |
+===============+==================+===========================================+
|``miniupnpc``  | UPnP Support     | Firewall-jumping support                  |
+---------------+------------------+-------------------------------------------+
|``libdb4.8``   | Berkeley DB      | Wallet storage (only needed when wallet   |
|               |                  | enabled)                                  |
+---------------+------------------+-------------------------------------------+
|``qt``         | GUI              | GUI toolkit (only needed when GUI enabled)|
+---------------+------------------+-------------------------------------------+
|``protobuf``   | Payments in GUI  | Data interchange format used for payment  |
|               |                  | protocol (only needed when GUI enabled)   |
+---------------+------------------+-------------------------------------------+
|``libqrencode``| QR codes in GUI  | Optional for generating QR codes (only    |
|               |                  | needed when GUI enabled)                  |
+---------------+------------------+-------------------------------------------+
|``univalue``   | Utility          | JSON parsing and encoding (bundled version|
|               |                  | will be used unless --with-system-univalue|
|               |                  | passed to configure)                      |
+---------------+------------------+-------------------------------------------+
|``libzmq3``    | ZMQ notification | Optional, allows generating ZMQ           |
|               |                  | notifications (requires ZMQ version       |
|               |                  | >= 4.x)                                   |
+---------------+------------------+-------------------------------------------+

Memory Requirements
--------------------

C++ compilers are memory-hungry. It is recommended to have at least 1.5 GB of
memory available when compiling Qogecoin Core. On systems with less, gcc can be
tuned to conserve memory with additional CXXFLAGS:

.. code-block:: bash

   ./configure \
        CXXFLAGS="--param ggc-min-expand=1 --param ggc-min-heapsize=32768"

Dependency Build Instructions: Ubuntu & Debian
----------------------------------------------

Build requirements:

.. code-block:: bash

   sudo apt-get install \
        build-essential \
        libtool \
        autotools-dev \
        automake \
        pkg-config \
        libssl-dev \
        libevent-dev \
        bsdmainutils

Options when installing required Boost library files:

1. On at least Ubuntu 14.04+ and Debian 7+ there are generic names for the
   individual boost development packages, so the following can be used to only
   install necessary parts of boost:

.. code-block:: bash

   sudo apt-get install \
        libboost-system-dev \
        libboost-filesystem-dev \
        libboost-chrono-dev \
        libboost-program-options-dev \
        libboost-test-dev \
        libboost-thread-dev

2. If that doesn't work, you can install all boost development packages with:

.. code-block:: bash

   sudo apt-get install libboost-all-dev

BerkeleyDB is required for the wallet.

**For Ubuntu only:** ``db4.8`` packages are available at
`launchpad <https://launchpad.net/~bitcoin/+archive/bitcoin>`_.

You can add the repository and install using the following commands:

.. code-block:: bash

   sudo apt-get install software-properties-common
   sudo add-apt-repository ppa:bitcoin/bitcoin
   sudo apt-get update
   sudo apt-get install libdb4.8-dev libdb4.8++-dev

Ubuntu and Debian have their own ``libdb-dev`` and ``libdb++-dev`` packages, but
these will install BerkeleyDB 5.1 or later, which break binary wallet
compatibility with the distributed executables which are based on BerkeleyDB
4.8. If you do not care about wallet compatibility, pass
``--with-incompatible-bdb`` to configure.

See the section "Disable-wallet mode" to build Qogecoin Core without wallet.

Optional (see ``--with-miniupnpc`` and ``--enable-upnp-default``):

.. code-block:: bash

    sudo apt-get install libminiupnpc-dev

ZMQ dependencies (provides ZMQ API 4.x):

.. code-block:: bash

   sudo apt-get install libzmq3-dev

Dependencies for the GUI: Ubuntu & Debian
-----------------------------------------

If you want to build Qogecoin-Qt, make sure that the required packages for Qt
development are installed. Either Qt 5 or Qt 4 are necessary to build the GUI.
If both Qt 4 and Qt 5 are installed, Qt 5 will be used. Pass ``--with-gui=qt4``
to configure to choose Qt4. To build without GUI pass ``--without-gui``.

To build with Qt 5 (recommended) you need the following:

.. code-block:: bash

   sudo apt-get install \
        libqt5gui5 \
        libqt5core5a \
        libqt5dbus5 \
        qttools5-dev \
        qttools5-dev-tools \
        libprotobuf-dev \
        protobuf-compiler

Alternatively, to build with Qt 4 you need the following:

.. code-block:: bash

   sudo apt-get install libqt4-dev libprotobuf-dev protobuf-compiler

``libqrencode`` (optional) can be installed with:

.. code-block:: bash

   sudo apt-get install libqrencode-dev

Once these are installed, they will be found by configure and a ``qogecoin-qt``
executable will be built by default.

Dependency Build Instructions: Fedora
-------------------------------------

Build requirements:

.. code-block:: bash

   sudo dnf install \
        gcc-c++ \
        libtool \
        make \
        autoconf \
        automake \
        openssl-devel \
        libevent-devel \
        boost-devel \
        libdb4-devel \
        libdb4-cxx-devel

Optional:

.. code-block:: bash

   sudo dnf install miniupnpc-devel

To build with Qt 5 (recommended) you need the following:

.. code-block:: bash

   sudo dnf install qt5-qttools-devel qt5-qtbase-devel protobuf-devel

``libqrencode`` (optional) can be installed with:

.. code-block:: bash

   sudo dnf install qrencode-devel

.. note::
   The release is built with GCC and then ``strip qogecoind`` to strip the debug
   symbols, which reduces the executable size by about 90%.

miniupnpc
---------

`miniupnpc <http://miniupnp.free.fr/>`_ may be used for UPnP port mapping. It
can be downloaded from `here <http://miniupnp.tuxfamily.org/files/>`_.
UPnP support is compiled in and turned off by default.
See the configure options for upnp behavior desired:


* ``--without-miniupnpc``: No UPnP support miniupnp not required

* ``--disable-upnp-default`` (the default) UPnP support turned off by default at
  runtime

* ``--enable-upnp-default`` UPnP support turned on by default at runtime

Berkeley DB
-----------
It is recommended to use Berkeley DB 4.8. If you have to build it yourself:

.. code-block:: bash

   QOGECOIN_ROOT=$(pwd)

   # Pick some path to install BDB to,
   # here we create a directory within the qogecoin directory
   BDB_PREFIX="${QOGECOIN_ROOT}/db4"
   mkdir -p $BDB_PREFIX

   # Fetch the source and verify that it is not tampered with
   wget 'http://download.oracle.com/berkeley-db/db-4.8.30.NC.tar.gz'
   echo '12edc0df75bf9abd7f82f821795bcee50f42cb2e5f76a6a281b85732798364ef  db-4.8.30.NC.tar.gz' | sha256sum -c
   # -> db-4.8.30.NC.tar.gz: OK
   tar -xzvf db-4.8.30.NC.tar.gz

   # Build the library and install to our prefix
   cd db-4.8.30.NC/build_unix/

   # Do a static build so that it can be embedded into the executable,
   # instead of having to find a .so at runtime
   ../dist/configure \
      --enable-cxx \
      --disable-shared \
      --with-pic \
      --prefix=$BDB_PREFIX
   make install

   # Configure Qogecoin Core to use our own-built instance of BDB
   cd $QOGECOIN_ROOT
   ./autogen.sh
   ./configure \
      LDFLAGS="-L${BDB_PREFIX}/lib/" \
      CPPFLAGS="-I${BDB_PREFIX}/include/"  # (other args...)

.. note::
   You only need Berkeley DB if the wallet is enabled (see the section
   :ref:`disable-wallet <disable-wallet>` mode below).

Security
--------

To help make your qogecoin installation more secure by making certain attacks
impossible to exploit even if a vulnerability is found, binaries are hardened by
default. This can be disabled with:

.. code-block:: bash

   ./configure --enable-hardening
   ./configure --disable-hardening

Hardening enables the following features:

* **Position Independent Executable**

   Build position independent code to take advantage of Address Space Layout
   Randomization offered by some kernels. Attackers who can cause execution of
   code at an arbitrary memory location are thwarted if they don't know where
   anything useful is located. The stack and heap are randomly located by
   default but this allows the code section to be randomly located as well.

   On an AMD64 processor where a library was not compiled with ``-fPIC``, this
   will cause an error such as:

   .. code-block::

      relocation R_X86_64_32 against `......' can not be used when making a shared object;

   To test that you have built PIE executable, install ``scanelf``, part of
   ``paxutils``, and use:

   .. code-block:: bash

      scanelf -e ./qogecoin

   The output should contain:

   .. code-block:: bash

      TYPE
      ET_DYN

* **Non-executable Stack**

   If the stack is executable then trivial stack based buffer overflow exploits
   are possible if vulnerable buffers are found. By default, qogecoin should be
   built with a non-executable stack but if one of the libraries it uses asks
   for an executable stack or someone makes a mistake and uses a compiler
   extension which requires an executable stack, it will silently build an
   executable without the non-executable stack protection.

   To verify that the stack is non-executable after compiling use:

   .. code-block:: bash

      scanelf -e ./qogecoin

   the output should contain:

   .. code-block:: bash

      STK/REL/PTL
      RW- R-- RW-

   The ``STK RW-`` means that the stack is readable and writeable but not
   executable.


.. _disable-wallet:

Disable-wallet mode
-------------------

When the intention is to run only a P2P node without a wallet, qogecoin may be
compiled in disable-wallet mode with:

.. code-block:: bash

   ./configure --disable-wallet

In this case there is no dependency on Berkeley DB 4.8.

Mining is also possible in disable-wallet mode, but only using the
``getblocktemplate`` RPC call instead of ``getwork``.

Additional Configure Flags
--------------------------
A list of additional configure flags can be displayed with:

.. code-block:: bash

   ./configure --help

Setup and Build Example: Arch Linux
-----------------------------------

This example lists the steps necessary to setup and build a command line only,
non-wallet distribution of the latest changes on Arch Linux:

.. code-block:: bash

   pacman -S git base-devel boost libevent python
   git clone https://github.com/qogecoin-project/qogecoin.git
   cd qogecoin/
   ./autogen.sh
   ./configure --disable-wallet --without-gui --without-miniupnpc
   make check

.. note::

   Enabling wallet support requires either compiling against a Berkeley DB newer
   than 4.8 (package ``db``) using ``--with-incompatible-bdb``, or building and
   depending on a local version of Berkeley DB 4.8. The readily available Arch
   Linux packages are currently built using ``--with-incompatible-bdb``
   according to the `Arch Wiki <https://projects.archlinux.org/svntogit/community.git/tree/bitcoin/trunk/PKGBUILD>`_.
   As mentioned above, when maintaining portability of the wallet between the
   standard Qogecoin Core distributions and independently built node software is
   desired, Berkeley DB 4.8 must be used.


ARM Cross-compilation
---------------------

These steps can be performed on, for example, an Ubuntu VM. The depends system
will also work on other Linux distributions, however the commands for installing
the toolchain will be different.

Make sure you install the build requirements mentioned above.
Then, install the toolchain and curl:

.. code-block:: bash

   sudo apt-get install g++-arm-linux-gnueabihf curl

To build executables for ARM:

.. code-block:: bash

   cd depends
   make HOST=arm-linux-gnueabihf NO_QT=1
   cd ..
   ./configure \
      --prefix=$PWD/depends/arm-linux-gnueabihf \
      --enable-glibc-back-compat \
      --enable-reduce-exports \
      LDFLAGS=-static-libstdc++
   make

For further documentation on the depends system see ``../depends/README.rst``
in the depends directory.
