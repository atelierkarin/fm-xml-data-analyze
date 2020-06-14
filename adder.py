import pandas as pd

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

from playerData import genPlayerData

cred = credentials.Certificate("fm-j-league-pack-firebase-adminsdk-h2qyn-6574551878.json")
firebase_admin.initialize_app(cred)

df = pd.read_csv('regional.csv', encoding='utf_8_sig')

db = firestore.client()

for index, row in df.iterrows():

  # Skip retired person
  if row['person_type'] == 5:
    continue

  playerData = genPlayerData(row, "新規選手 地域1.fmf")

  firestore_id = None

  query = db.collection('playerDb').where('player.basicInfo.name', '==', row['common_name'])
  docs = query.stream()
  
  for doc in docs:
    firestore_id = doc.id

  if firestore_id == None:
    doc_ref = db.collection(u'playerDb').document()
    new_id = doc_ref.id
    add_data = {'id': new_id, 'player': playerData}
    db.collection(u'playerDb').document(new_id).set(add_data)
    print(row['common_name'] + " ADDED.")
  else:
    print(row['common_name'] + " SKIPPED.")