testable_appengine
==================

A testable Python skeleton application for Google App Engine and
AppScale environments

Why?
----

The difficulty of properly testing Python applications written for the
Google App Engine platform was always a problem to me. I always wanted
something that would be comfortable to use, "pythonic" and that didn't
depend on changes to the application you are trying to test, much less
forcing you to deploy your tests to the production environment. I am
also very fond of "convention over configuration" and wanted something
that would make it easy to build upon rather than something that
requires figuring out documentation written by insanely smart people for
insanely smart people. With testable_appengine in place, running tests
is as trivial as running `nosetests` with no additional plugins and no
tweaks to your test programs. This tree was extracted from a larger
project that makes use of it and further evolved on its own, with the
enhancements ported back.

![nosetests running]
(https://raw.githubusercontent.com/wiki/rbanffy/testable_appengine/screenshot.png)

Setting up your development environment
---------------------------------------

There is a makefile in the root directory. Running `make venv` will
build a virtualenv in the `.env` folder, download the App Engine SDK,
build the appropriate .pth files for your machine and install all
requirements from the `resources/requirements.txt` file. If you wish to
use a Python environment you provide yourself, you can make the
virtualenv youself and run `make libraries` with VENV pointing to your
virtualenv (as in `VENV=.my_env make libraries`)

The actual makefile is under resources. Your own makefile (with your own
targets) should include it and extend it like the included Makefile
does.

Please check the makefile before using it. It may not make sense for
your environment. It was tested on Ubuntu, Fedora, OSX (10.7+,
provided you have functional pip and virtualenv utilities) and Windows
8.1 under [Cygwin](http://www.cygwin.com/). If you are developing under
Windows and don't use Cygwin, you are suffering more than you need for
no good reason.

![Under Windows+Cygwin]
(https://raw.githubusercontent.com/wiki/rbanffy/testable_appengine/windows.png)

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

Debugging
---------

Debugging works like you'd expect. You just use pdb or ipdb (ipdb seems
to have a tendency not to work under the dev_appserver, but pdb is just
fine). Rule is, use ipbd if you want to debug something that's called
by a test, pdb for a live web application. Worst case scenario is that
you just need to delete a character. You can also easily use iPython to
explore your ideas before you commit them to code.

![ipython prompt and ipdb in a test]
(https://raw.githubusercontent.com/wiki/rbanffy/testable_appengine/using_ipdb.png)

Contributing
------------

File a bug report (enhancement suggestions are fine too), fork it, PEP-8
it, test it, and, if it works, send a pull request. When in doubt, get
in touch. We'll figure out what needs to be done.
