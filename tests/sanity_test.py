"""
Ensure the environment is sane
"""

# Do not add your own tests to this file. This file is intended for the sole
# purpose of confirming your environment was properly set-up

import unittest
import webtest

# The test will error out if we can't import these items
from google.appengine.api import memcache
from google.appengine.ext import db
from google.appengine.ext import ndb
from google.appengine.ext import testbed

# If your project has a src/main.py file, it'll check if it imports
try:
    from src import main
    TEST_HANDLER = True
except ImportError:
    TEST_HANDLER = False


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


if TEST_HANDLER:
    class HandlerTest(unittest.TestCase):

        def setUp(self):
            self.testapp = webtest.TestApp(main.application)

        def test_sample_request(self):
            response = self.testapp.get('/')
            self.assertEqual(response.status_int, 200)


if __name__ == '__main__':
    unittest.main()
