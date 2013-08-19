======================================
Setting up the Development Environment
======================================

Clone The Repository
====================
::

  $ git clone git@github.com:wehaveweneed/whwn.git

This will clone the repository to your local machine for the virtual machine to
run the code.


Setup the VM
============

The easiest way to get set up is with the virtual machine. Mostly.

install virtual box & vagrant
-----------------------------
How to setup VM:
On Windows:

On Linus/OSx/Ubuntu

installing it locally
^^^^^^^^^^^^^^^^^^^^^
how to install locally

Start Django
============
::

  $ vagrant up
  $ fab bootstrap

In a browser, go to localhost:8000/
profit

TODO: seeding & fab file

Recompiling CSS files
=====================
::

	$ fab guard


Stopping Vagrant
================
::

	$ vagrant halt

