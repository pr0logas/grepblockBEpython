#:: By GrepBlock.com developers // pr0logas, mrNemo
#:: Modified date: 2019-11-30
#:: Description: This file is a workspace for assetGraph creation.

import sys, time
from datetime import datetime, timedelta
from time import gmtime, strftime
from dash import *
sys.path.append('../../../')
from mongoDB import *
from parseGraphs import parseGraph

db = database
collectionForBlocks = "blocks"

# Init Classes;
PG = parseGraph(assetTicker, fileForBlockchainSize, genesisBlock)
MC = mongoConnection(mongoAuth, db, collectionForBlocks)

# Find Last unixTime value in a working json file;
lU = PG.parseBlockchainSizeFindLastValueTime()
if lU == 'FileWasEmpty!':
	lU = PG.parseBlockchainSizeFindLastValueTime()
	print("Warning, file was empty, init zero params!")

# Find the same but in MongoDB;
lastBlockByUnixTime = MC.findLastBlockTime(collectionForBlocks, lU)

# Last Block value in mongoDB;
findLastBlock = MC.findLastBlock(collectionForBlocks)

# Init Global while vars;
nextDayTime = (datetime.fromtimestamp(float(lU)) + timedelta(hours=24)).strftime('%Y-%m-%d') # Increase 1 day;
sumSize = PG.parseBlockchainSizeFindLastValueSize()
nextDayTimeWhileProgress = nextDayTime

whileprogress = lastBlockByUnixTime
while whileprogress <= findLastBlock:
	lB = MC.findByBlock(collectionForBlocks, whileprogress)
	if lB != []: # This should never happen!
		count = lB['size']
		unixTime = lB['time']
		reqNum = int(count)
		currBlkTime = (datetime.fromtimestamp(unixTime)).strftime('%Y-%m-%d')

		timeSet = strftime("%Y-%m-%d %H:%M:%S", gmtime())

		# This should never happen. But if the blockchain stopped for more than 24h?
		check1 = str(currBlkTime).replace("-", "")
		check2 = str(nextDayTimeWhileProgress).replace("-", "")

		if int(check1) > int(check2):
			print("WARNING! The blockchain STALL has been detected!!!")
			printTime = (datetime.fromtimestamp(unixTime)).strftime('%Y-%m-%d')
			timeSet = strftime("%Y-%m-%d %H:%M:%S", gmtime())
			resJSON = PG.appendNewContentToBlockchainSizeGraph(sumSize, unixTime)
			resWrite = PG.writeJSONtoFile(resJSON)
			if resWrite == 'OK':
				print(timeSet + " Next day found. Total BlockchainSize: " + str(sumSize) + " bytes. // We at " + str(printTime))
				nextDayTimeWhileProgress = (datetime.fromtimestamp(unixTime) + timedelta(hours=24)).strftime('%Y-%m-%d') # Increase 1 day;
			else:
				print("FATAL!")
				sys.exit(1)

		elif currBlkTime != nextDayTimeWhileProgress:
			sumSize = (int(reqNum) + int(sumSize))

		else:
			printTime = (datetime.fromtimestamp(unixTime)).strftime('%Y-%m-%d')
			timeSet = strftime("%Y-%m-%d %H:%M:%S", gmtime())
			resJSON = PG.appendNewContentToBlockchainSizeGraph(sumSize, unixTime)
			resWrite = PG.writeJSONtoFile(resJSON)
			if resWrite == 'OK':
				print(timeSet + " Next day found. Total BlockchainSize: " + str(sumSize) + " bytes. // We at " + str(printTime))
				nextDayTimeWhileProgress = (datetime.fromtimestamp(unixTime) + timedelta(hours=24)).strftime('%Y-%m-%d') # Increase 1 day;
			else:
				print("FATAL!")
				sys.exit(1)

	else:
		print("FATAL! Something went wrong while counting BlockchainSize Graph!")
		sys.exit(1)

	whileprogress += 1

# Send new JSON to FE;
PG.sendJSONtoFronend()
timeSet = strftime("%Y-%m-%d %H:%M:%S", gmtime())
print(timeSet +" ***JSON copied to FE instance***")

timeSet = strftime("%Y-%m-%d %H:%M:%S", gmtime())
print(timeSet +" All tasks were successful.")