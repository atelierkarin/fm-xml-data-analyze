import sys
import argparse

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

from datetime import datetime

cred = credentials.Certificate("fm-j-league-pack-firebase-adminsdk-h2qyn-6574551878.json")
firebase_admin.initialize_app(cred)

parser = argparse.ArgumentParser()
parser.add_argument("oriname", help="Original Name", type=str)
parser.add_argument("--rename", help="Rename to new Name", type=str)
parser.add_argument("--delete", help="Delete record", action='store_true')
args = parser.parse_args()

db = firestore.client()

query = db.collection('playerDb').where('player.basicInfo.name', '==', args.oriname)
docs = query.stream()

for doc in docs:
  firestore_id = doc.id
  original_data = doc.to_dict()
  playerData = original_data['player']

  if args.delete:
    db.collection(u'playerDb').document(firestore_id).delete()
    print(args.oriname + "の記録が削除されました。")
  elif args.rename:
    playerData["basicInfo"]["updateDate"] = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
    playerData["basicInfo"]["name"] = args.rename
    update_data = {'id': firestore_id, 'player': playerData}
    db.collection(u'playerDb').document(firestore_id).set(update_data)
    print(args.oriname + "の記録が更新されました。")