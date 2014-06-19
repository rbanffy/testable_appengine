"""
Tools to automate loading of test fixtures
"""

import json
import os

from datetime import datetime

from google.appengine.ext.ndb.model import DateTimeProperty

def load_fixture(filename, cls=None):
    "Loads a file into entities of a given class"

    if cls is None:
        raise NotImplementedError(
            'Multiple types per JSON file are coming, eventually')

    def _loader(cls=cls):
        "Create a loader for this type"

        def _load(od):
            "Load the attributes defined in od into a cls and saves it"
            obj = cls()
            for attribute_name in od:
                attribute_type = cls.__dict__[attribute_name]
                if type(attribute_type) is DateTimeProperty:
                    attribute_value = datetime.strptime(od[attribute_name],
                                                        '%Y-%m-%dT%H:%M:%S')
                else:
                    attribute_value = od[attribute_name]
                obj.__dict__['_values'][attribute_name] = attribute_value
            obj.put()
            return obj

        return _load

    data = json.load(open(filename), object_hook=_loader(cls))
    return data
