#:: By GrepBlock.com developers // pr0logas, mrNemo
#:: Modified date: 2019-11-30
#:: Description: This file is a workspace for assetGraph creation.

import sys, time
from datetime import datetime, timedelta
from time import gmtime, strftime
from adeptio import *
sys.path.append('../../../')
from mongoDB import *
from parseGraphs import parseGraph

db = database
collectionForBlocks = "blocks"

# Init Classes;
PG = parseGraph(assetTicker, fileForBlockCount, genesisBlock)
MC = mongoConnection(mongoAuth, db, collectionForBlocks)

# Find Last unixTime value in a working json file;
lU = PG.parseBlocksFindLastValue()
if lU == 'FileWasEmpty!':
	lU = PG.parseBlocksFindLastValue()
	print "Warning, file was empty, init zero params!"

# Find the same but in MongoDB;
lastBlockByUnixTime = MC.findLastBlockTime(collectionForBlocks, lU)

# Last Block value in mongoDB;
findLastBlock = MC.findLastBlock(collectionForBlocks)

# Init Global while vars;
nextDayTime = (datetime.fromtimestamp(float(lU)) + timedelta(hours=24)).strftime('%Y-%m-%d') # Increase 1 day;
sumBlocks = 0
nextDayTimeWhileProgress = nextDayTime

whileprogress = lastBlockByUnixTime
while whileprogress <= findLastBlock:
	setProcStart = int(round(time.time() * 1000))
	lB = MC.findByBlock(collectionForBlocks, whileprogress)
	if lB != []: # This should never happen!
		count = lB['block']
		unixTime = lB['time']
		reqNum = (count - count) + 1 # How to get count? Change this :DD
		currBlkTime = (datetime.fromtimestamp(unixTime)).strftime('%Y-%m-%d')

		timeSet = strftime("%Y-%m-%d %H:%M:%S", gmtime())
		print timeSet + " Counting blocks: " + str(sumBlocks)

		if currBlkTime != nextDayTimeWhileProgress:
			sumBlocks = (reqNum + sumBlocks)
		else:
			printTime = (datetime.fromtimestamp(unixTime)).strftime('%Y-%m-%d')
			timeSet = strftime("%Y-%m-%d %H:%M:%S", gmtime())
			resJSON = PG.appendNewContentToBlocksGraph(sumBlocks, unixTime)
			resWrite = PG.writeJSONtoFile(resJSON)
			if resWrite == 'OK':
				setProcEnd = int(round(time.time() * 1000))
				performanceResult = str(setProcEnd - setProcStart)
				print timeSet + " Next day found. Total blocks: " + str(sumBlocks) + " // We at " + str(printTime) + ' // ' + str(performanceResult) + ' ms'
				sumBlocks = 0
				nextDayTimeWhileProgress = (datetime.fromtimestamp(unixTime) + timedelta(hours=24)).strftime('%Y-%m-%d') # Increase 1 day;
			else:
				print "FATAL!"
				sys.exit(1)

	else:
		print "FATAL! Something went wrong while counting Blocks Graph!"
		sys.exit(1)

	whileprogress += 1

# Send new JSON to FE;
PG.sendJSONtoFronend()
timeSet = strftime("%Y-%m-%d %H:%M:%S", gmtime())
print timeSet +" JSON copied to FE instance"

timeSet = strftime("%Y-%m-%d %H:%M:%S", gmtime())
print timeSet +" All task was successful."