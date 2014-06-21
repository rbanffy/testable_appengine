"""
Ensure the environment is sane
"""

# Do not add your own tests to this file. This file is intended for the sole
# purpose of confirming your environment was properly set-up

import datetime
import unittest
import webtest

# The test will error out if we can't import these items
from google.appengine.api import memcache
from google.appengine.ext import db
from google.appengine.ext import ndb
from google.appengine.ext import testbed

from testable_appengine.loader import load_fixture

# If your project has a src/main.py file, it'll check if it imports
try:
    from src import main
    TEST_HANDLER = True
except ImportError:
    TEST_HANDLER = False


class Person(ndb.Model):
    first_name = ndb.StringProperty()
    last_name = ndb.StringProperty()
    born = ndb.DateTimeProperty()
    userid = ndb.IntegerProperty()
    thermostat_set_to = ndb.FloatProperty()
    snores = ndb.BooleanProperty()
    started_school = ndb.DateProperty()
    sleeptime = ndb.TimeProperty()
    favorite_movies = ndb.JsonProperty()


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


class LoaderTest(unittest.TestCase):
    def setUp(self):
        self.testbed = testbed.Testbed()
        self.testbed.activate()
        self.testbed.init_datastore_v3_stub()
        self.testbed.init_memcache_stub()
        self.loaded_data = load_fixture('tests/persons.json', Person)

    def tearDown(self):
        self.testbed.deactivate()

    def test_loaded_count(self):
        """Make sure we got 4 objects from the JSON file"""
        self.assertEqual(len(self.loaded_data), 4)

    def test_loaded_types(self):
        """Make sure all objects we loaded are instances of Person"""
        self.assertTrue(all([type(p) == Person for p in self.loaded_data]))

    def test_loaded(self):
        # Test if the first record got in
        person = Person.query(Person.first_name == 'John').get()
        self.assertEqual(person.first_name, 'John')
        self.assertEqual(person.last_name, 'Doe')
        self.assertEqual(person.born, datetime.datetime(1968, 3, 3))
        self.assertEqual(person.thermostat_set_to, 18.34)

        # Test for the third one
        person = Person.query(Person.last_name == 'Schneier' and
                              Person.first_name == 'Alice').get()
        self.assertEqual(person.first_name, 'Alice')
        self.assertEqual(person.last_name, 'Schneier')
        self.assertEqual(person.born, datetime.datetime(1999, 9, 19))
        self.assertTrue(person.snores)

        # Test for the last one
        person = Person.query(
            Person.born == datetime.datetime(1980, 5, 25, 0, 0, 0)).get()
        self.assertEqual(person.first_name, 'Bob')
        self.assertEqual(person.last_name, 'Schneier')
        self.assertEqual(person.born, datetime.datetime(1980, 5, 25))


if __name__ == '__main__':
    unittest.main()
