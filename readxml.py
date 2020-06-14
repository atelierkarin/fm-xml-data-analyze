import pandas as pd
from reader import read_xml
from properties import properties

import numpy as np

data = read_xml('regional.xml')

header = ["version"].append([p["name"] for p in properties])

df = pd.DataFrame.from_dict(data, orient='index', columns=header)

df.loc[df['common_name'].isnull(), 'common_name'] = df['first_name'] + ' ' + df['last_name']

df.to_csv('regional.csv', encoding='utf_8_sig')