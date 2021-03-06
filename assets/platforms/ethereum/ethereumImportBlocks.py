#:: By GrepBlock.com developers // pr0logas
#:: Modified date: 2019-12-31
#:: Description: This file is a workspace for block importation.

import sys, time
from time import gmtime, strftime
from ethereum import *
sys.path.append('../../../')
from mongoDB import *
from explorer import ethereumHTTPnode
from parseBlocks import aggregatePlatformBlocksData

db = database
collectionForBlocks = "blocks"

# Init Classes;
MC = mongoConnection(mongoAuth, db, collectionForBlocks)
EX = ethereumHTTPnode(chainProvider)
AG = aggregatePlatformBlocksData()

# Check if blocks col empty or not?
if MC.checkIfBlocksColEmpty(collectionForBlocks) == "Empty":
	print("Warning! We found an empty blocks collection. Starting from zero.")
	MC.insertInitValueForBlocks(collectionForBlocks)

# Set current progress;
currentLastBlock = MC.findLastBlock(collectionForBlocks)

# Check last Explorer block:
currentExplBlock = int(EX.getLastBlock())
currentExplBlock -= 2

# Set how much blocks we want to sync from current point +- ~99
parsingBlocksInRange = parseBlocksInRangeFor + currentLastBlock

# Check if our progress is near by Explorer blocks?
diff = str(currentExplBlock - currentLastBlock)

# We have two choices here, parse the blocks in range for +- ~100 blocks (last block too far anyway) or until last Explorer block -2 //
# We don't wanna to parse up to last block in case of wrong chain.

# Start Parsing blocks ::in range:: and push to MongoDB;
if (int(diff) >= 100):
	whileprogress = currentLastBlock 

	if whileprogress == 0:
		whileprogress += 1

	while whileprogress < parsingBlocksInRange:
		setProcStart = int(round(time.time() * 1000))
		bD = EX.getBlockContentByBlockNum(str(whileprogress))
		aggregatedBlockData = AG.aggregatePlatformData(bD)
		#print(aggregatedBlockData) # Testing to see aggregated data
		status = MC.insertBlocksData(collectionForBlocks, aggregatedBlockData)
		whileprogress += 1

		setProcEnd = int(round(time.time() * 1000))
		performanceResult = str(setProcEnd - setProcStart)
		timeSet = strftime("%Y-%m-%d %H:%M:%S", gmtime())
		if str(status) != 'None':
			print(timeSet + " Block finished: " + str(status) + ' // ' + (performanceResult) + ' ms')

	timeSet = strftime("%Y-%m-%d %H:%M:%S", gmtime())
	print(timeSet + " No new blocks found, last one: " + str(parsingBlocksInRange))

# Start Parsing blocks until last Explorer block -2 and push to MongoDB;
else: 
	whileprogress = currentLastBlock 

	if whileprogress == 0:
		whileprogress += 1

	while whileprogress < currentExplBlock:
		setProcStart = int(round(time.time() * 1000))
		bD = EX.getBlockContentByBlockNum(str(whileprogress))
		aggregatedBlockData = AG.aggregatePlatformData(bD)
		#print(aggregatedBlockData) # Testing to see aggregated data
		status = MC.insertBlocksData(collectionForBlocks, aggregatedBlockData)
		whileprogress += 1

		setProcEnd = int(round(time.time() * 1000))
		performanceResult = str(setProcEnd - setProcStart)
		timeSet = strftime("%Y-%m-%d %H:%M:%S", gmtime())
		if str(status) != 'None':
			print(timeSet + " Block finished: " + str(status) + ' // ' + (performanceResult) + ' ms')

	timeSet = strftime("%Y-%m-%d %H:%M:%S", gmtime())
	print(timeSet + " No new blocks found, last one: " + str(currentExplBlock))
