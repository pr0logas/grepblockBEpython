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

if diff <= 100:
	# Start Parsing blocks and push to MongoDB;
	setProcStart = int(round(time.time() * 1000))
	AG.parseBlocks(currentLastBlock, currentExplBlock)
else:
	# Start Parsing blocks ::in range:: and push to MongoDB;
	setProcStart = int(round(time.time() * 1000))
	AG.parseBlocksInRange(currentLastBlock, parsingBlocksInRange)