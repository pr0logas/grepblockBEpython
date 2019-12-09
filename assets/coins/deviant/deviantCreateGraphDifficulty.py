#:: By GrepBlock.com developers // pr0logas, mrNemo
#:: Modified date: 2019-11-30
#:: Description: This file is a workspace for assetGraph creation.

import sys, time
from datetime import datetime, timedelta
from time import gmtime, strftime
from deviant import *
sys.path.append('../../../')
from mongoDB import *
from parseGraphs import parseGraph

db = database
collectionForBlocks = "blocks"

# Init Classes;
PG = parseGraph(assetTicker, fileForDifficulty, genesisBlock)
MC = mongoConnection(mongoAuth, db, collectionForBlocks)

# Find Last unixTime value in a working json file;
lU = PG.parseDifficultyFindLastValue()
if lU == 'FileWasEmpty!':
	lU = PG.parseDifficultyFindLastValue()
	print "Warning, file was empty, init zero params!"

while True:
	lU = PG.parseDifficultyFindLastValue()
	lastProgress = MC.findLastDiffbyTime(collectionForBlocks, lU)
	averageBlkMinus = (86400 - int(blockTime))
	lastProgress = (lastProgress + averageBlkMinus)
	diffRes = MC.findDiffGtThan(collectionForBlocks, lastProgress)

	if diffRes == 'Empty':
		# Send new JSON to FE;
		PG.sendJSONtoFronend()
		timeSet = strftime("%Y-%m-%d %H:%M:%S", gmtime())
		print timeSet +" ***JSON copied to FE instance***"
		print timeSet +" All tasks were successful."
		break
	else:
		unixTime = MC.findDiffGtThanReturnTime(collectionForBlocks, lastProgress)
		printTime = (datetime.fromtimestamp(unixTime)).strftime('%Y-%m-%d')
		timeSet = strftime("%Y-%m-%d %H:%M:%S", gmtime())
		resJSON = PG.appendNewContentToDifficultyGraph(float(diffRes), unixTime)
		resWrite = PG.writeJSONtoFile(resJSON)
		if resWrite == 'OK':
			print timeSet + " Next day found. Difficulty: " + str(diffRes) + " // We at " + str(printTime)
		else:
			print "FATAL!"
			sys.exit(1)