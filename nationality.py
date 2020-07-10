nationality = {}
nationality[21] = 'GHA'
nationality[38] = 'NGA'
nationality[116] = 'JPN'
nationality[129] = 'PRK'
nationality[135] = 'KOR'
nationality[141] = 'PHI'
nationality[390] = 'USA'
nationality[775] = 'ISR'
nationality[787] = 'POL'
nationality[796] = 'ESP'
nationality[1435] = 'AUS'
nationality[1649] = 'ARG'
nationality[1650] = 'BOL'
nationality[1651] = 'BRA'
nationality[1652] = 'CHI'

def getNationality(nid):
  return nationality[nid] if nid in nationality else nid