#!/usr/bin/env python

import sys, time
from adeptio import *
sys.path.append('../../../')
from mongoDB import *
from parseWallets import * 
from explorer import iquidusExplorer
from parseWallets import aggregateWalletsData

collectionForBlocks = "blocks"

# Init Mongo Connection to Class;
MC = mongoConnection(mongoAuth, database, collectionTxidProgress)

# Set current progress;
currentLastBlock = MC.findLastBlock(collectionForBlocks)

# Init Explorer params to Class;
EX = iquidusExplorer(chainProvider, getBlockIndexMethod, getBlockwithHashMethod, getTx)

# Init Data Aggregation Class;
AG = aggregateWalletsData()

