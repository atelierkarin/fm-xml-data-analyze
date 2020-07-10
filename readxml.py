import sys
import pandas as pd
from reader import read_xml
from properties import properties

import numpy as np

args = sys.argv

if len(args) < 2:
  print('You need to provide filename!')
else:
  filename = args[1]
  data = read_xml(filename)
  header = ["version"].append([p["name"] for p in properties])
  df = pd.DataFrame.from_dict(data, orient='index', columns=header)
  df.loc[df['common_name'].isnull(), 'common_name'] = df['first_name'] + ' ' + df['last_name']
  df.to_csv(filename + '.csv', encoding='utf_8_sig')