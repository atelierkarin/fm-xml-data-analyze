import sys
import pandas as pd
import argparse

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

from playerData import genPlayerData

from datetime import datetime

cred = credentials.Certificate("fm-j-league-pack-firebase-adminsdk-h2qyn-6574551878.json")
firebase_admin.initialize_app(cred)

parser = argparse.ArgumentParser()
parser.add_argument("filename", help="Filename of csv file", type=str)
parser.add_argument("--club", help="Club ID for updating", type=int)
parser.add_argument("--player", help="Player name for updating", type=str)

args = parser.parse_args()

def getDataFileType(filename=''):
  if filename == "jleague-2.xml.csv":
    return "新規選手2.fmf"
  elif filename == "jleague-3.xml.csv":
    return "新規選手3.fmf"
  elif filename == "jleague-jfl.xml.csv":
    return "新規選手 JFL.fmf"
  elif filename == "jleague-regional.xml.csv":
    return "新規選手 地域1.fmf"
  elif filename == "jleague-existing.xml.csv":
    return "既存選手変更.fmf"
  return "新規選手.fmf"

if not hasattr(args, 'filename'):
  print('You need to provide filename!')
else:
  df = pd.read_csv(args.filename, encoding='utf_8_sig')

  db = firestore.client()

  for index, row in df.iterrows():
    # Skip retired person
    if row['person_type'] == 5:
      continue

    # Sip no nationailty
    if row['nationality'] != row['nationality']:
      continue

    # Skip player with Club not equal to specific Club ID
    if args.club:
      skip_club = args.club
      if skip_club is not None:
        if int(skip_club) == 0:
          if not row['club'] != row['club']:
            continue
        elif row['club'] != row['club'] or not int(row['club']) == int(skip_club):
          continue
    
    # Skip player with player name not match
    if args.player:
      if row['common_name'] != args.player:
        continue

    playerData = genPlayerData(row, getDataFileType(args.filename))

    firestore_id = None

    query = db.collection('playerDb').where('player.basicInfo.name', '==', row['common_name'])
    docs = query.stream()
    
    for doc in docs:
      firestore_id = doc.id

      original_data = doc.to_dict()
      try:
        jleagueId = original_data['player']['location']['jleagueId']
        if jleagueId: playerData['location']['jleagueId'] = jleagueId
      except KeyError:
        pass

    if firestore_id == None:
      # Only add player / staff with club records
      if row['club'] == row['club']:
        doc_ref = db.collection(u'playerDb').document()
        new_id = doc_ref.id
        add_data = {'id': new_id, 'player': playerData}
        db.collection(u'playerDb').document(new_id).set(add_data)
        print(row['common_name'] + "の記録が追加されました。")
    else:
      if row['club'] != row['club']:
        db.collection(u'playerDb').document(firestore_id).delete()
        print(row['common_name'] + "の記録が削除されました。")
      else:
        playerData["basicInfo"]["updateDate"] = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
        update_data = {'id': firestore_id, 'player': playerData}
        db.collection(u'playerDb').document(firestore_id).set(update_data)
        print(row['common_name'] + "の記録が更新されました。")