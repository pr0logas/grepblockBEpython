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
EX = iquidusExplorer(chainProvider, getBlockIndexMethod, getBlockwithHashMethod, getTx)\
PB = aggregateBlocksData(db, collectionForBlocks)
AG = aggregateWalletsData()

# Set current progress;
currentLastBlock = MC.findLastBlock(collectionForBlocks)

# Check if blocks col empty or not?
if MC.checkIfBlocksColEmpty(collectionForBlocks) == "Empty":
	MC.insertInitValueForBlocks(collectionForBlocks)

# Check last Explorer block:
currentExplBlock = EX.
currentExplBlock -= 1

# Set how much blocks we want to sync from current point +- ~99
parsingBlocksInRange = parseBlocksInRangeFor + currentLastBlock

# Check if our progress is near by Explorer blocks?
diff = currentExplBlock - currentLastBlock

# Init parseBlocks Class;


if diff <= 100
	# Start Parsing blocks and push to MongoDB;
	PB.parseBlocks()
else:
	# Start Parsing blocks ::in range:: and push to MongoDB;
	PB.parseBlocksInRange()