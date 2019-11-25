#!/usr/bin/env python

import sys, time
from adeptio import *
sys.path.append('../../../')
from mongoDB import *
from explorer import iquidusExplorer
from parseWallets import aggregateWalletsData

collectionTxidProgress = "txidsProgress"
collectionForBlocks = "blocks"
collectionForWallets = "wallets"

# Init Mongo Connection to Class;
MC = mongoConnection(mongoAuth, database, collectionTxidProgress)

# Set current progress;
currentLastTxidProgress = MC.findLastTxidProgress(collectionTxidProgress)
currentLastBlock = MC.findLastBlock(collectionForBlocks)

# Init Explorer params to Class;
EX = iquidusExplorer(chainProvider, getBlockIndexMethod, getBlockwithHashMethod, getTx)

# Init Data Aggregation Class;
AG = aggregateWalletsData()

# Decrease txidsProgress value in case of previous failure;
MC.updateLastTxidProgressMinusOne(collectionTxidProgress, currentLastTxidProgress)

if int(MC.findLastTxidProgress(collectionTxidProgress)) == int(currentLastTxidProgress):
	print ("FAIL: Unable to decrease lastblock value in txidsProgress!")
	sys.exit(1)
else:
	print ("OK: txidsProgress value succesfully decreased to:" + ' ' + str(MC.findLastTxidProgress(collectionTxidProgress)))

# Start Parsing for unique Wallets and push to MongoDB;
whileprogress = currentLastTxidProgress
while whileprogress < currentLastBlock:

	setProcStart = int(round(time.time() * 1000))
	blockData = MC.findByBlock(collectionForBlocks, whileprogress)
	blockTime = blockData['time']
	blockNumber = blockData['height']
	for txid in blockData['tx']:
		getTxData = EX.getTxContentByTxid(txid)
		randomWlts = AG.findAllWalletsAddr(getTxData)
		if randomWlts != []:
			uniqWlts = AG.aggregateOnlyUniqueWallets(randomWlts)
			for uw in uniqWlts:
				createJSON = AG.createJsonForWallet(str(blockNumber), str(blockTime), uw)
				setProcEnd = int(round(time.time() * 1000))
				performanceResult = str(setProcEnd - setProcStart)
				#print (performanceResult) + ' ms'
				MC.upsertUniqueWallets(collectionForWallets, createJSON)
	# Increase txidsProgress to move forward;
	print "check current", currentLastTxidProgress
	MC.updateLastTxidProgressPlusOne(collectionTxidProgress, currentLastTxidProgress)
	currentLastTxidProgress += 1
	print currentLastTxidProgress