"""
Ensure the fixture system works
"""

# Do not add your own tests to this file. This file is intended for the sole
# purpose of confirming your environment was properly set-up


import unittest
import webtest

from google.appengine.api import memcache
from google.appengine.ext import db
from google.appengine.ext import testbed

from google.appengine.ext import ndb

class Person(ndb.Model):
    first_name = ndb.StringProperty()
    last_name = ndb.StringProperty()
    born = ndb.DateTimeProperty()

from tools import load_fixture

from src import main

class LoaderTest(unittest.TestCase):
    def setUp(self):
        self.testbed = testbed.Testbed()
        self.testbed.activate()
        self.testbed.init_datastore_v3_stub()
        self.testbed.init_memcache_stub()
        load_fixture('file.json', Person)

    def tearDown(self):
        self.testbed.deactivate()

    def test_loaded(self):
        self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()
