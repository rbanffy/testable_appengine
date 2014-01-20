testable_appengine
==================

A testable Python skeleton application for Google App Engine and
AppScale environments

Why?
----

Being unable to properly unit-test my App Engine applications has been a
major annoyance for me and a big turn-off for the platform. With these
in place, running tests is as trivial as running nose. This tree was
extracted from a larger project that makes use of it.

Setting up your development environment
---------------------------------------

There is a setup.sh script in the root directory. Running it will build
a virtualenv in the `.env` folder, download the App Engine SDK, build
the appropriate .pth files for your machine and install all requirements
from the `resources/requirements.txt` file.

Please check it before running. It may not make sense for your machine.

When done, you can activate your virtualenv with the usual `source
.env/bin/activate` or your favorite virtualenv tool.

Tests
-----

There are tests in the tests folder. The sanity_test.py checks whether
everything is sane after you set up the environment.

Contributing
------------

File a bug report, fork it, PEP-8 it, test it, and, if it works, send a
pull request. When in doubt, get in touch. We'll figure out what needs
to be done.
