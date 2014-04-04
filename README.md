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

There is a makefile in the root directory. Running `make venv` will
build a virtualenv in the `.env` folder, download the App Engine SDK,
build the appropriate .pth files for your machine and install all
requirements from the `resources/requirements.txt` file. If you wish to
use a Python environment you provide yourself, you can make the
virtualenv youself and run `make libraries` with VENV pointing to your
virtualenv (as in `VENV=.my_env make libraries`)

Please check the makefile before using it. It may not make sense for
your environment. It was tested on both Ubuntu, Fedora and OSX (10.7+,
provided you have functional pip and virtualenv utilities). It should
work on Windows under [Cygwin](http://www.cygwin.com/), but it was never
tested that way.

When done, you can activate your virtualenv with the usual `source
.env/bin/activate` or your favorite virtualenv tool. The tests will not
function outside the local virtualenv. From the virtualenv, invoking
dev_appserver.py and appcfg.py will use the versions in the SDK
downloaded during install (check the `Makefile` for current version).

Your app should go in the `src` folder. Run your application using the
dev_appserver.py script from within the virtualenv, as in
`dev_appserver.py src`. Always deploy from the `src` folder so your
tests don't end up on the server.

Tests
-----

There are tests in the tests folder. The sanity_test.py checks whether
everything is sane after you set up the environment.

Contributing
------------

File a bug report (enhancement suggestions are fine too), fork it, PEP-8
it, test it, and, if it works, send a pull request. When in doubt, get
in touch. We'll figure out what needs to be done.
