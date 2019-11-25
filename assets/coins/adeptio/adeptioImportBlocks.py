#!/usr/bin/env python

import sys, time
from adeptio import *
sys.path.append('../../../')
from mongoDB import *
from parseWallets import aggregateWalletsData
from explorer import iquidusExplorer


collectionForBlocks = "blocks"

# Init Mongo Connection to Class;
MC = mongoConnection(mongoAuth, database, collectionTxidProgress)

# Set current progress;
currentLastBlock = MC.findLastBlock(collectionForBlocks)

# Init Explorer params to Class;
EX = iquidusExplorer(chainProvider, getBlockIndexMethod, getBlockwithHashMethod, getTx)

# Init Data Aggregation Class;
AG = aggregateWalletsData()

# Check if blocks col empty or not?
print MC.checkIfBlocksColEmpty(collectionForBlocks)