from .context import saneschema

import json
import os
import unittest



DIR = os.path.dirname(os.path.abspath(__file__)) 

class TestArray(unittest.TestCase):

  def test_empty(self):
    SCHEMA_FILE = 'empty_jex_array_schema.json'
    UNCHECKED_FILE = 'empty_array.json'
    self.do_check(SCHEMA_FILE, UNCHECKED_FILE)

  def test_objects(self):
    SCHEMA_FILE = 'jex_object_array_schema.json'
    UNCHECKED_FILE = 'object_array.json'
    self.do_check(SCHEMA_FILE, UNCHECKED_FILE)

  def test_arrays(self):
    SCHEMA_FILE = 'jex_array_array_schema.json'
    UNCHECKED_FILE = 'array_array.json'
    self.do_check(SCHEMA_FILE, UNCHECKED_FILE)

  def test_string(self):
    SCHEMA_FILE = 'jex_string_array_schema.json'
    UNCHECKED_FILE = 'string_array.json'
    self.do_check(SCHEMA_FILE, UNCHECKED_FILE)

  def test_numbers(self):
    SCHEMA_FILE = 'jex_number_array_schema.json'
    UNCHECKED_FILE = 'number_array.json'
    self.do_check(SCHEMA_FILE, UNCHECKED_FILE)

  def test_booleans(self):
    SCHEMA_FILE = 'jex_boolean_array_schema.json'
    UNCHECKED_FILE = 'boolean_array.json'
    self.do_check(SCHEMA_FILE, UNCHECKED_FILE)

  def test_nulls(self):
    SCHEMA_FILE = 'jex_null_array_schema.json'
    UNCHECKED_FILE = 'null_array.json'
    self.do_check(SCHEMA_FILE, UNCHECKED_FILE)

  def do_check(self, schema_file, unchecked_file):
    SCHEMA_PATH = os.path.join(DIR, schema_file)
    UNCHECKED_PATH = os.path.join(DIR, unchecked_file)
    schema = saneschema.Schema(SCHEMA_PATH)
    with open(UNCHECKED_PATH, 'r') as f:
      unchecked = json.load(f)
      schema.check(unchecked)
