import sys
import pandas as pd
import argparse

from reader import read_xml
from properties import properties

import numpy as np

parser = argparse.ArgumentParser()
parser.add_argument("filename", help="Filename of exported xml file (From FM manager)", type=str)
args = parser.parse_args()

if not hasattr(args, 'filename'):
  print('You need to provide filename!')
else:
  filename = args.filename
  data = read_xml(filename)
  header = ["version"].append([p["name"] for p in properties])
  df = pd.DataFrame.from_dict(data, orient='index', columns=header)
  df.loc[df['common_name'].isnull(), 'common_name'] = df['first_name'] + ' ' + df['last_name']
  df.to_csv(filename + '.csv', encoding='utf_8_sig')