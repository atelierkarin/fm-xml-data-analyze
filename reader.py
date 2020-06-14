import xml.etree.ElementTree as et
from properties import properties

def check_property(id):
  name = None
  for prop in properties:
    if str(prop['id']) == id:
      name = prop['name']
      break
  return name

def get_record_value(record):
  new_value_string = record.find("string[@id='new_value']")
  new_value_int = record.find("integer[@id='new_value']")
  new_value_record = record.find("record[@id='new_value']")
  new_value_date = record.find("date[@id='new_value']")
  if not new_value_string == None:
    return new_value_string.attrib['value']
  elif not new_value_int == None:
    return new_value_int.attrib['value']
  elif not new_value_record == None:
    new_value_id = new_value_record.find("integer")
    if not new_value_id == None:
      return new_value_id.attrib['value']
  elif not new_value_date == None:
    return new_value_date.attrib['year'] + '-' + "{:02d}".format(int(new_value_date.attrib['month'])) + '-' + "{:02d}".format(int(new_value_date.attrib['day']))

  return None

def read_xml(source_file):
  tree = et.parse(source_file)
  l = tree.find("list[@id='db_changes']")
  records = {}

  for record in l.findall('record'):
    unsigned = record.find("unsigned[@id='property']")
    db_unique_id = record.find("large[@id='db_unique_id']")
    version = record.find("integer[@id='version']")

    # Last 5 values of db_unique_id is random numbers, so cut them off
    curr_id = str(db_unique_id.attrib['value'])[:-7]
    curr_property = check_property(unsigned.attrib['value'])
    if not curr_property == None:

      v = get_record_value(record)

      if not curr_id in records:
        records[curr_id] = {}

      records[curr_id]['version'] = version.attrib['value']
      records[curr_id][curr_property] = v
  
  return records