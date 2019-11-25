#!/usr/bin/env python

import sys, time
from coin import *
sys.path.append('../../../')
from mongoDB import *
from parseWallets import aggregateWalletsData
from explorer import iquidusExplorer

for coin in coins:

	collectionForBlocks = "blocks"

	# Init Mongo Connection to Class;
	MC = mongoConnection(mongoAuth, coin.database, collectionTxidProgress)

	# Set current progress;
	currentLastBlock = MC.findLastBlock(collectionForBlocks)

	# Init Explorer params to Class;
	EX = iquidusExplorer(coin.chainProvider, coin.getBlockIndexMethod, coin.getBlockwithHashMethod, coin.getTx)

	# Init Data Aggregation Class;
	AG = aggregateWalletsData()

	# Check if blocks col empty or not?
	print MC.checkIfBlocksColEmpty(collectionForBlocks)