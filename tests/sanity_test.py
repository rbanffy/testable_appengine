"""
Ensure the environment is sane
"""

import unittest
import webtest

from google.appengine.api import memcache
from google.appengine.ext import db
from google.appengine.ext import testbed

from src import main


class SanityTest(unittest.TestCase):

    def setUp(self):
        self.testbed = testbed.Testbed()
        self.testbed.activate()
        self.testbed.init_datastore_v3_stub()
        self.testbed.init_memcache_stub()

    def tearDown(self):
        self.testbed.deactivate()

    def test_sanity(self):
        self.assertTrue(True)


class HandlerTest(unittest.TestCase):

    def setUp(self):
        self.testapp = webtest.TestApp(main.application)

    def test_sample_request(self):
        response = self.testapp.get('/')
        self.assertEqual(response.status_int, 200)


if __name__ == '__main__':
    unittest.main()
