Sample init scripts and service configuration for qogecoind
===========================================================

Sample scripts and configuration files for systemd, Upstart and OpenRC
can be found in the contrib/init folder.

* ``contrib/init/qogecoind.service``
   ``systemd`` service unit configuration.
* ``contrib/init/qogecoind.openrc``
   OpenRC compatible SysV style init script.
* ``contrib/init/qogecoind.openrcconf``
   OpenRC conf.d file.
* ``contrib/init/qogecoind.conf``
   Upstart service configuration file.

1. Service User
---------------

All three Linux startup configurations assume the existence of a ``qogecoin``
user and group.  They must be created before attempting to use these scripts.

2. Configuration
---------------------------------

At a bare minimum, ``qogecoind`` requires that the rpcpassword setting be set
when running as a daemon.  If the configuration file does not exist or this
setting is not set, ``qogecoind`` will shutdown promptly after startup.

This password does not have to be remembered or typed as it is mostly used
as a fixed token that ``qogecoind`` and client programs read from the
configuration file, however it is recommended that a strong and secure password
be used as this password is security critical to securing the wallet should the
wallet be enabled.

If ``qogecoind`` is run with the ``-server`` flag (set by default), and no
``rpcpassword`` is set, it will use a special cookie file for authentication.
The cookie is generated with random content when the daemon starts, and deleted
when it exits. Read access to this file controls who can access it through RPC.

By default the cookie is stored in the data directory, but it's location can be
overridden with the option ``-rpccookiefile``.

This allows for running ``qogecoind`` without any custom configurations.

``conf``, ``pid``, and ``wallet`` accept relative paths which are interpreted
as relative to the data directory. ``wallet`` only supports relative paths.

For an example configuration file that describes the configuration settings,
see ``contrib/debian/examples/qogecoin.conf``.

3. Paths
--------

All three configurations assume several paths that might need to be adjusted.

Binary:              ``/usr/bin/qogecoind``
Configuration file:  ``/etc/qogecoin/qogecoin.conf``
Data directory:      ``/var/lib/qogecoind``
PID file (OpenRC):   ``/var/run/qogecoind/qogecoind.pid``
PID file (systemc):  ``/var/lib/qogecoind/qogecoind.pid``

The configuration file, PID directory (if applicable) and data directory
should all be owned by the ``qogecoin`` user and group.  It is advised for
security reasons to make the configuration file and data directory only readable
by the ``qogecoin`` user and group.  Access to ``qogecoin-cli`` and other
``qogecoind`` rpc clients can then be controlled by group membership.

4. Installing Service Configuration
-----------------------------------

* ``systemd``
   Installing this .service file consists of just copying it to
   ``/usr/lib/systemd/system`` directory, followed by the command
   ``systemctl daemon-reload`` in order to update running systemd configuration.

   To test, run ``systemctl start qogecoind`` and to enable for system startup
   run ``systemctl enable qogecoind``.

* ``OpenRC``
   Rename qogecoind.openrc to qogecoind and drop it in ``/etc/init.d``.  Double
   check ownership and permissions and make it executable.  Test it with
   ``/etc/init.d/qogecoind start`` and configure it to run on startup with
   ``rc-update add qogecoind``
