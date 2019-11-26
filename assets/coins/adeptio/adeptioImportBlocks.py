#!/usr/bin/env python

import sys, time
from adeptio import *
sys.path.append('../../../')
from mongoDB import *
from explorer import iquidusExplorer
from parseBlocks import aggregateBlocksData

db = database
collectionForBlocks = "blocks"

# Init Classes;
MC = mongoConnection(mongoAuth, db, collectionForBlocks)
EX = iquidusExplorer(chainProvider, getBlockIndexMethod, getBlockwithHashMethod, getTx)
AG = aggregateBlocksData()

# Check if blocks col empty or not?
if MC.checkIfBlocksColEmpty(collectionForBlocks) == "Empty":
	print "Warning! We found an empty blocks collection. Starting from zero."
	MC.insertInitValueForBlocks(collectionForBlocks)

# Set current progress;
currentLastBlock = MC.findLastBlock(collectionForBlocks)

# Check last Explorer block:
currentExplBlock = int(EX.getLastBlock())
currentExplBlock -= 1

# Set how much blocks we want to sync from current point +- ~99
parsingBlocksInRange = parseBlocksInRangeFor + currentLastBlock

# Check if our progress is near by Explorer blocks?
diff = str(currentExplBlock - currentLastBlock)

# We have two choises here, parse the blocks in range for +- ~100 block (last block too far anyway) or until last Explorer block -2 //
# We don't wanna to parse up to last block, because in case of wrong chain parsing node could rewrite the latest few blocks;
if diff >= 100:
	whileprogress = currentLastBlock # Start Parsing blocks ::in range:: and push to MongoDB;

	if whileprogress == 0:
		whileprogress += 1

	while whileprogress < parsingBlocksInRange:
		bH = EX.getBlockHash(str(whileprogress))
		bD = EX.getBlockContentByHash(bH)
		aggregatedBlockData = AG.aggregateInsertBlockNumber(bD)
		MC.insertBlocksData(collectionForBlocks, aggregatedBlockData)
		whileprogress += 1

else: 
	whileprogress = currentLastBlock # Start Parsing blocks until last Explorer block -2 and push to MongoDB;

	if whileprogress == 0:
		whileprogress += 1

	while whileprogress < currentExplBlock:
		bH = EX.getBlockHash(str(whileprogress))
		bD = EX.getBlockContentByHash(bH)
		AG.aggregateInsertBlockNumber(bD)
		whileprogress += 1