from .context import saneschema

import json
import os
import unittest



DIR = os.path.dirname(os.path.abspath(__file__)) 

class TestBasicTypeCheck(unittest.TestCase):

  def test_object(self):
    SCHEMA_FILE = 'jex_object_schema.json'
    UNCHECKED_FILE = 'object.json'
    self.do_check(SCHEMA_FILE, UNCHECKED_FILE)

  def test_array(self):
    SCHEMA_FILE = 'jex_array_schema.json'
    UNCHECKED_FILE = 'array.json'
    self.do_check(SCHEMA_FILE, UNCHECKED_FILE)

  def test_string(self):
    SCHEMA_FILE = 'jex_string_schema.json'
    UNCHECKED_FILE = 'string.json'
    self.do_check(SCHEMA_FILE, UNCHECKED_FILE)

  def test_number(self):
    SCHEMA_FILE = 'jex_number_schema.json'
    UNCHECKED_FILE = 'number.json'
    self.do_check(SCHEMA_FILE, UNCHECKED_FILE)

  def test_boolean(self):
    SCHEMA_FILE = 'jex_boolean_schema.json'
    UNCHECKED_FILE = 'boolean.json'
    self.do_check(SCHEMA_FILE, UNCHECKED_FILE)

  def test_null(self):
    SCHEMA_FILE = 'jex_null_schema.json'
    UNCHECKED_FILE = 'null.json'
    self.do_check(SCHEMA_FILE, UNCHECKED_FILE)

  def do_check(self, schema_file, unchecked_file):
    SCHEMA_PATH = os.path.join(DIR, schema_file)
    UNCHECKED_PATH = os.path.join(DIR, unchecked_file)
    schema = saneschema.Schema(SCHEMA_PATH)
    with open(UNCHECKED_PATH, 'r') as f:
      unchecked = json.load(f)
      schema.check(unchecked)

