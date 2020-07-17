from dataFileType import getDataFileType
from nationality import getNationality
from playerType import getPlayerType

def isEmpty(v):
  return v == None or v != v or v == ''

def formatNumber(v, defaultValue = None):
  if isEmpty(v):
    return defaultValue
  elif v == 0:
    return defaultValue
  else:
    return int(v)

def isPlayer(p):
  if not isEmpty(p['clubJob']):
    player_types = getPlayerType(int(p['clubJob']))
    return player_types is not None and 0 in player_types
  else:
    return not isEmpty(p['ca']) or not isEmpty(p['pa']) or p['person_type'] == 1 or not isNonPlayer(p)

def isNonPlayer(p):
  if not isEmpty(p['clubJob']):
    player_types = getPlayerType(int(p['clubJob']))
    return player_types is None or any(y > 0 for y in player_types)
  else:
    return not isEmpty(p['staffCa']) or p['person_type'] == 2 or p['person_type'] == 3

def formatObject(o):
  formattedValue = {k: v for k, v in o.items() if v is not None}
  return formattedValue if len(formattedValue.keys()) > 0 else None

def getPlayerLocation(player, datafileType):
  location = {}
  location['file'] = getDataFileType(datafileType)

  return location

def getBasicInfo(player):
  basicInfo = {}
  basicInfo['name'] = player['common_name']
  basicInfo['nameEng'] = player['first_name'] + ' ' + player['last_name']
  if not isEmpty(player['dob']): basicInfo['dob'] = player['dob']
  basicInfo['nationality'] = getNationality(int(player['nationality']))
  basicInfo['isPlayer'] = isPlayer(player)
  basicInfo['isNonPlayer'] = isNonPlayer(player)

  return basicInfo

def getClubInfo(player):
  if isEmpty(player['club']):
    return None
  else:
    clubInfo = {}
    clubInfo['id'] = int(player['club'])
    clubInfo['dateJoined'] = player['clubDateJoined']
    clubInfo['dateRenew'] = player['clubDateRenewed']
    clubInfo['job'] = getPlayerType(int(player['clubJob']) if not isEmpty(player['clubJob']) else 0, isPlayer(player), isNonPlayer(player))
    if not isEmpty(player['clubSquadNumber']): clubInfo['squardNumber'] = int(player['clubSquadNumber'])

    return clubInfo

def getLoanInfo(player):
  if not 'loanClub' in player or isEmpty(player['loanClub']):
    return None
  else:
    loanInfo = {}
    loanInfo['id'] = int(player['loanClub'])
    loanInfo['dateStart'] = player['loanDateStart']
    loanInfo['dateEnd'] = player['loanDateEnd']
    if not isEmpty(player['loanSquardNumber']): loanInfo['squardNumber'] = int(player['loanSquardNumber'])

    return loanInfo

def getPersonalData(player):
  personalData = {}

  personalData['adaptability'] = formatNumber(player['adaptability'])
  personalData['ambition'] = formatNumber(player['ambition'])
  personalData['controversy'] = formatNumber(player['controversy'])
  personalData['loyalty'] = formatNumber(player['loyalty'])
  personalData['perssure'] = formatNumber(player['pressure'])
  personalData['professionalism'] = formatNumber(player['professionalism'])
  personalData['sportsmanship'] = formatNumber(player['sportsmanship'])
  personalData['temperament'] = formatNumber(player['temperament'])

  return formatObject(personalData)

def getPlayerGeneralData(player):
  general = {}
  general['ca'] = formatNumber(player['ca'], 0)
  general['pa'] = formatNumber(player['pa'], 0)
  general['currentReputation'] = formatNumber(player['currentReputation'])
  general['homeReputation'] = formatNumber(player['homeReputation'])
  general['worldReputation'] = formatNumber(player['worldReputation'])
  general['height'] = formatNumber(player['height'])
  general['weight'] = formatNumber(player['weight'])
  general['leftFoot'] = formatNumber(player['leftFoot'])
  general['rightFoot'] = formatNumber(player['rightFoot'])

  return formatObject(general)

def getPlayerPositionsData(player):
  positions = {}
  positions['goalkeeper'] = formatNumber(player['goalkeeper'])
  positions['defenderLeft'] = formatNumber(player['defenderLeft'])
  positions['defenderCentral'] = formatNumber(player['defenderCentral'])
  positions['defenderRight'] = formatNumber(player['defenderRight'])
  positions['defensiveMidfielder'] = formatNumber(player['defensiveMidfielder'])
  positions['wingBackLeft'] = formatNumber(player['wingBackLeft'])
  positions['wingBackRight'] = formatNumber(player['wingBackRight'])
  positions['midfielderLeft'] = formatNumber(player['midfielderLeft'])
  positions['midfielderCentral'] = formatNumber(player['midfielderCentral'])
  positions['midfielderRight'] = formatNumber(player['midfielderRight'])
  positions['attackingMidfielderLeft'] = formatNumber(player['attackingMidfielderLeft'])
  positions['attackingMidfielderCentral'] = formatNumber(player['attackingMidfielderCentral'])
  positions['attackingMidfielderRight'] = formatNumber(player['attackingMidfielderRight'])
  positions['striker'] = formatNumber(player['striker'])

  return formatObject(positions)

def getPlayerMentalData(player):
  mental = {}
  mental['aggression'] = formatNumber(player['aggression'])
  mental['anticipation'] = formatNumber(player['anticipation'])
  mental['bravery'] = formatNumber(player['bravery'])
  mental['composure'] = formatNumber(player['composure'])
  mental['concentration'] = formatNumber(player['concentration'])
  mental['consistency'] = formatNumber(player['consistency'])
  mental['decisions'] = formatNumber(player['decisions'])
  mental['determination'] = formatNumber(player['determination'])
  mental['dirtiness'] = formatNumber(player['dirtiness'])
  mental['flair'] = formatNumber(player['flair'])
  mental['importantMatches'] = formatNumber(player['importantMatches'])
  mental['leadership'] = formatNumber(player['leadership'])
  mental['movement'] = formatNumber(player['movement'])
  mental['positioning'] = formatNumber(player['positioning'])
  mental['teamWork'] = formatNumber(player['teamWork'])
  mental['vision'] = formatNumber(player['vision'])
  mental['workRate'] = formatNumber(player['workRate'])

  return formatObject(mental)
 
def getPlayerPhysicalData(player):
  physical = {}
  physical['acceleration'] = formatNumber(player['acceleration'])
  physical['agility'] = formatNumber(player['agility'])
  physical['balance'] = formatNumber(player['balance'])
  physical['injuryProneness'] = formatNumber(player['injuryProneness'])
  physical['jumpingReach'] = formatNumber(player['jumpingReach'])
  physical['naturalFitness'] = formatNumber(player['naturalFitness'])
  physical['pace'] = formatNumber(player['pace'])
  physical['stamina'] = formatNumber(player['stamina'])
  physical['strength'] = formatNumber(player['strength'])

  return formatObject(physical)
 
def getPlayerTechnicalData(player):
  technical = {}
  technical['corners'] = formatNumber(player['corners'])
  technical['crossing'] = formatNumber(player['crossing'])
  technical['dribbling'] = formatNumber(player['dribbling'])
  technical['finishing'] = formatNumber(player['finishing'])
  technical['firstTouch'] = formatNumber(player['firstTouch'])
  technical['freeKicks'] = formatNumber(player['freeKicks'])
  technical['heading'] = formatNumber(player['heading'])
  technical['longShots'] = formatNumber(player['longShots'])
  technical['longThrows'] = formatNumber(player['longThrows'])
  technical['marking'] = formatNumber(player['marking'])
  technical['passing'] = formatNumber(player['passing'])
  technical['penaltyTaking'] = formatNumber(player['penaltyTaking'])
  technical['tackling'] = formatNumber(player['tackling'])
  technical['technique'] = formatNumber(player['technique'])
  technical['versatility'] = formatNumber(player['versatility'])

  return formatObject(technical)
 
def getPlayerGoalkeepingData(player):
  goalkeeping = {}
  if 'aerialAbility' in player: goalkeeping['aerialAbility'] = formatNumber(player['aerialAbility'])
  if 'commandOfArea' in player: goalkeeping['commandOfArea'] = formatNumber(player['commandOfArea'])
  if 'communication' in player: goalkeeping['communication'] = formatNumber(player['communication'])
  if 'eccentricity' in player: goalkeeping['eccentricity'] = formatNumber(player['eccentricity'])
  if 'handling' in player: goalkeeping['handling'] = formatNumber(player['handling'])
  if 'kicking' in player: goalkeeping['kicking'] = formatNumber(player['kicking'])
  if 'oneOnOnes' in player: goalkeeping['oneOnOnes'] = formatNumber(player['oneOnOnes'])
  if 'reflexes' in player: goalkeeping['reflexes'] = formatNumber(player['reflexes'])
  if 'rushingOut' in player: goalkeeping['rushingOut'] = formatNumber(player['rushingOut'])
  if 'tendencyToPunch' in player: goalkeeping['tendencyToPunch'] = formatNumber(player['tendencyToPunch'])
  if 'throwing' in player: goalkeeping['throwing'] = formatNumber(player['throwing'])

  return formatObject(goalkeeping)

def getPlayerData(player):
  playerData = {}
  playerData['general'] = getPlayerGeneralData(player)

  positionsData = getPlayerPositionsData(player)
  if positionsData != None: playerData['positions'] = positionsData

  mentalData = getPlayerMentalData(player)
  if mentalData != None: playerData['mental'] = mentalData

  physicalData = getPlayerPhysicalData(player)
  if physicalData != None: playerData['physical'] = physicalData

  technicalData = getPlayerTechnicalData(player)
  if technicalData != None: playerData['technical'] = technicalData

  goalkeepingData = getPlayerGoalkeepingData(player)
  if goalkeepingData != None: playerData['goalkeeping'] = goalkeepingData

  return formatObject(playerData)

def getNonPlayerData(player):
  nonPlayerData = {}
  nonPlayerData['ca'] = formatNumber(player['staffCa'])
  nonPlayerData['pa'] = formatNumber(player['staffPa'])
  nonPlayerData['currentReputation'] = formatNumber(player['staffCurrentReputation'])
  nonPlayerData['homeReputation'] = formatNumber(player['staffHomeReputation'])
  nonPlayerData['worldReputation'] = formatNumber(player['staffWorldReputation'])

  return formatObject(nonPlayerData)

def genPlayerData(p, datafileType="新規選手.fmf"):
  player = {}
  
  player['location'] = getPlayerLocation(p, datafileType)
  player['basicInfo'] = getBasicInfo(p)
  player['clubInfo'] = getClubInfo(p)

  loanInfo = getLoanInfo(p)
  if loanInfo != None: player['loanInfo'] = loanInfo

  personalData = getPersonalData(p)
  if personalData != None: player['personalData'] = personalData

  if isPlayer(p):
    playerData = getPlayerData(p)
    player['playerData'] = playerData

  if isNonPlayer(p):
    nonPlayerData = getNonPlayerData(p)
    if nonPlayerData != None: player['nonPlayerData'] = nonPlayerData

  return player