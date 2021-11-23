======================
Backing up your wallet
======================

.. note::
   Qogecoin alongside other descendants of Bitcoin have similar commands.
   Keep that in mind when you need to google how something is done.
   If there is something missing from these docs and you are stuck, ask on the Discord.


To back up your wallet, here are some steps you can take.

To get a copy of your ``wallet.dat``, you can either:
 - Manually copy the file from your Qogecoin data folder
 - Run the ``backupwallet`` command.

The Qogecoin folder on Windows is:
``C:\Users\YOUR_USERNAME\AppData\Roaming\Qogecoin``

and Linux: ``$HOME/.qogecoin``

Once you have located your ``wallet.dat``, copy the file to another location.

An easier method to backup the wallet is to use the command ``backupwallet``,
alongside the file location to save the file in.

For example, using the qt wallet console:

.. code-block:: powershell
   :caption: Copying your wallet using ``backupwallet`` on Windows.

   backupwallet C:\Users\Jacob\Downloads\wallet.dat

If you are using qogecoind, prefix the command with qogecoin-cli.
