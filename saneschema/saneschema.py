import logging
import json
import re

class SchemaCheckError:
  pass

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

  def check(self, unchecked):
    self.__check(self._schema, unchecked)

  def __check(self, checked, unchecked):
    checked_type = type(checked)
    unchecked_type = type(unchecked)
    if (checked_type == unchecked_type):
      if (checked_type == OBJECT_TYPE):
        self.__check_class(checked, unchecked)
      elif (checked_type == ARRAY_TYPE):
        self.__check_array(checked, unchecked)
      elif (checked_type == STRING_TYPE):
        self.__check_string(checked, unchecked)
      elif (checked_type in (INT_TYPE, FLOAT_TYPE)):
        self.__check_number(checked, unchecked)
      elif (checked_type == BOOLEAN_TYPE):
        self.__check_boolean(checked, unchecked)
      elif (checked_type == NULL_TYPE):
        self.__check_null(checked_unchecked)
      else:
        self._logger.error('Unknown type. Please contact the package maintainer')
    else:
      self._logger.info('JSON failed check')
      raise SchemaCheckError()

  def __check_class(self, checked, unchecked):
    for field in unchecked:
      field_checked = False
      for pattern in checked:
        result = re.search(pattern, field)
        if (not result is None):
          try:
            self.__check(checked[pattern], unchecked)
            field_checked = True
            break
          except SchemaCheckError:
            continue
      if (field_checked == False):
        raise SchemaCheckError()

  def __check_array(self, checked, unchecked):
    for item in unchecked:
      item_checked = False
      for example in checked:
        try:
          self.__check(example, item)
          item_checked = True
          break
        except SchemaCheckError:
          continue
      if (item_checked == False):
        raise SchemaCheckError()

  def __check_string(self, checked, unchecked):
    result = re.search(checked, unchecked)
    if (result in None):
      raise SchemaCheckError()

  def __check_number(self, checked, unchecked):
    pass

  def __check_boolean(self, checked, unchecked):
    pass

  def __check_null(self, checked, unchecked):
    pass
