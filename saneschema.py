import logging
import json
import re

class SchemaCheckError(BaseException):
  
  def __init__(self, msg):
    self.msg = msg

class Schema:

  OBJECT_TYPE  = type(json.loads('{}'))
  ARRAY_TYPE   = type(json.loads('[]'))
  STRING_TYPE  = type(json.loads('""'))
  INT_TYPE     = type(json.loads('0'))
  FLOAT_TYPE   = type(json.loads('0.0'))
  BOOLEAN_TYPE = type(json.loads('true'))
  NULL_TYPE    = type(json.loads('null'))

  def __init__(self, path):
    self._logger = logging.getLogger(__name__)
    try:
      with open(path, 'r') as f:
        self._schema = json.load(f)
    except IOError:
      self._logger.error('Error opening JSON schema file')
      raise
    except json.JSONDecodeError:
      self._logger.error('Error decoding JSON schema')
      raise
    except:
      self._logger.error('An unknown error occurred')
      raise

  def check(self, unchecked):
    pass

  def __check(self, checked, unchecked):
    pass

  def __check_class(self, checked, unchecked):
    pass

  def __check_array(self, checked, unchecked):
    pass

  def __check_string(self, checked, unchecked):
    pass

  def __check_number(self, checked, unchecked):
    pass

  def __check_boolean(self, checked, unchecked):
    pass

  def __check_null(self, checked, unchecked):
    pass
