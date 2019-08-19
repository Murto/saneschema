from .context import saneschema

import json
import os
import unittest



DIR = os.path.dirname(os.path.abspath(__file__))

class TestObjectCheck(unittest.TestCase):

  def test_types_in_object(self):
    SCHEMA_FILE = 'types_in_object_schema.json'
    UNCHECKED_FILE = 'types_in_object.json'
    self.do_check(SCHEMA_FILE, UNCHECKED_FILE)

  def do_check(self, schema_file, unchecked_file):
    SCHEMA_PATH = os.path.join(DIR, schema_file)
    UNCHECKED_PATH = os.path.join(DIR, unchecked_file)
    schema = saneschema.Schema(SCHEMA_PATH)
    with open(UNCHECKED_PATH, 'r') as f:
      unchecked = json.load(f)
      schema.check(unchecked)
