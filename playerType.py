jobType = {}
jobType[1] = ["オーナー／社長"]
jobType[2] = ["オーナー／社長"]
jobType[4] = ["フットボールディレクター"]
jobType[5] = ["監督"]
jobType[6] = ["アシスタントマネージャー"]
jobType[7] = ["コーチ"]
jobType[8] = ["コーチ"]
jobType[9] = ["スカウト"]
jobType[10] = ["トレーナー"]
jobType[11] = ["選手"]
jobType[12] = ["選手","監督"]
jobType[13] = ["選手","アシスタントマネージャー"]
jobType[14] = ["選手","コーチ"]
jobType[15] = ["選手","コーチ"]
jobType[21] = ["選手","オーナー／社長"]
jobType[26] = ["GKコーチ"]
jobType[27] = ["選手","GKコーチ"]
jobType[30] = ["コーチ"]
jobType[34] = ["チーフスカウト"]
jobType[36] = ["ヘッドフィジオ"]
jobType[38] = ["取締役"]
jobType[55] = ["フィジカルコーチ"]
jobType[100] = ["ユース管理責任者"]
jobType[128] = ["選手","フットボールディレクター"]
jobType[173] = ["スポーツサイエンティスト"]

playerType = [
  "選手",
  "監督",
  "アシスタントマネージャー",
  "コーチ",
  "フィジカルコーチ",
  "GKコーチ",
  "スカウト",
  "チーフスカウト",
  "データアナリスト",
  "チーフデータアナリスト",
  "トレーナー",
  "ヘッドフィジオ",
  "スポーツサイエンティスト",
  "チーフスポーツサイエンティスト",
  "フットボールディレクター",
  "ユース管理責任者",
  "U18監督",
  "オーナー／社長",
  "取締役",
  "テクニカルダイレクター"
]

def getPlayerType(id=0, isPlayer=True, isNonPlayer=False):
  if id == 0:
    id = 11 if isPlayer else 8
  if not id in jobType:
    return None
  return [playerType.index(j) for j in jobType[id]]