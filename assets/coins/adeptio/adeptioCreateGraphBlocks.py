#:: By GrepBlock.com developers // pr0logas
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
PG = parseGraph(fileForBlockCount, genesisBlock)
MC = mongoConnection(mongoAuth, db, collectionForBlocks)

# Find Last unixTime value in a working json file;
lUTinJSON = PG.parseBlocksFindLastValue()
if lUTinJSON == 'FileWasEmpty!':
	lUTinJSON = PG.parseBlocksFindLastValue()
	print "Warning, file was empty, init zero params!"

print lUTinJSON

# Find the same but in MongoDB;
lastBlockByUnixTime = MC.findLastBlockTime(collectionForBlocks, lUTinJSON)

# Increase number to move forward;
lastBlockByUnixTime += 1

# Last Block value in mongoDB;
findLastBlock = MC.findLastBlock(collectionForBlocks)

#nextDay = (datetime.fromtimestamp(lUTinJSON) + timedelta(hours=24)).strftime('%Y-%m-%d')
#print nextDay
sumBlocks = 0
setWorkingValue = lastBlockByUnixTime
while setWorkingValue <= findLastBlock:
	lB = MC.findByBlock(collectionForBlocks, setWorkingValue)
	if lB != []:
		print lB
		count = lB['block']
		unixTime = lB['time']
		reqNum = (count - count) + 1
		sumBlocks = (reqNum + sumBlocks)
		print sumBlocks
		dt = (datetime.fromtimestamp(unixTime)).strftime('%Y-%m-%d')
		print (dt)
		break
	else:
		print "Fatal something went wrong while counting Blocks Graph!"
		sys.exit(1)

