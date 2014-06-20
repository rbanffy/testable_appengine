"""
Ensure the fixture system works
"""

# Do not add your own tests to this file. This file is intended for the sole
# purpose of confirming your environment was properly set-up


import unittest
<<<<<<< HEAD
import webtest

from google.appengine.api import memcache
from google.appengine.ext import db
from google.appengine.ext import testbed

from google.appengine.ext import ndb

=======
import datetime

from google.appengine.ext import testbed
from google.appengine.ext import ndb

from testable_appengine.loader import load_fixture


>>>>>>> feature/fixtures
class Person(ndb.Model):
    first_name = ndb.StringProperty()
    last_name = ndb.StringProperty()
    born = ndb.DateTimeProperty()
<<<<<<< HEAD

from tools import load_fixture

from src import main
=======
    userid = ndb.IntegerProperty()
    thermostat_set_to = ndb.FloatProperty()
    snores = ndb.BooleanProperty()
    started_school = ndb.DateProperty()
    sleeptime = ndb.TimeProperty()
    favorite_movies = ndb.JsonProperty()

>>>>>>> feature/fixtures

class LoaderTest(unittest.TestCase):
    def setUp(self):
        self.testbed = testbed.Testbed()
        self.testbed.activate()
        self.testbed.init_datastore_v3_stub()
        self.testbed.init_memcache_stub()
<<<<<<< HEAD
        load_fixture('file.json', Person)
=======
        load_fixture('tests/persons.json', Person)
>>>>>>> feature/fixtures

    def tearDown(self):
        self.testbed.deactivate()

    def test_loaded(self):
<<<<<<< HEAD
        self.assertTrue(True)
=======
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
>>>>>>> feature/fixtures


if __name__ == '__main__':
    unittest.main()
