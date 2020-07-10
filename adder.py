import sys
import pandas as pd

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

from playerData import genPlayerData

from datetime import datetime

cred = credentials.Certificate("fm-j-league-pack-firebase-adminsdk-h2qyn-6574551878.json")
firebase_admin.initialize_app(cred)

args = sys.argv

if len(args) < 2:
  print('You need to provide filename!')
else:
  df = pd.read_csv(args[1], encoding='utf_8_sig')

  db = firestore.client()

  for index, row in df.iterrows():
    # Skip retired person
    if row['person_type'] == 5:
      continue

    # Skip player not club id if provide
    skip_club = args[2]
    if skip_club is not None:
      if row['club'] != row['club'] or not int(row['club']) == int(skip_club):
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
      playerData["basicInfo"]["updateDate"] = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
      update_data = {'id': firestore_id, 'player': playerData}
      db.collection(u'playerDb').document(firestore_id).set(update_data)
      print(row['common_name'] + " UPDATED.")