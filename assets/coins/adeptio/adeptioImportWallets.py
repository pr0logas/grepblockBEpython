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

# Init Classes;
MC = mongoConnection(mongoAuth, database, collectionTxidProgress)
EX = iquidusExplorer(chainProvider, getBlockIndexMethod, getBlockwithHashMethod, getTx)
AG = aggregateWalletsData()

# Set current progress;
currentLastTxidProgress = MC.findLastTxidProgress(collectionTxidProgress)
currentLastBlock = MC.findLastBlock(collectionForBlocks)

# Decrease txidsProgress value in case of previous failure;
MC.updateLastTxidProgressMinusOne(collectionTxidProgress, currentLastTxidProgress)

if int(MC.findLastTxidProgress(collectionTxidProgress)) == int(currentLastTxidProgress):
	print ("FAIL: Unable to decrease lastblock value in txidsProgress!")
	sys.exit(1)
else:
	print ("OK: txidsProgress value succesfully decreased to:" + ' ' + str(MC.findLastTxidProgress(collectionTxidProgress)))

# Start Parsing for unique Wallets and push to MongoDB;
whileprogress = currentLastTxidProgress
while whileprogress<currentLastBlock:

	setProcStart = int(round(time.time() * 1000))
	print "whileprogress: ", whileprogress
	blockData = MC.findByBlock(collectionForBlocks, whileprogress)
	print "blockData: ", blockData
	blockTime = blockData['time']
	blockNumber = blockData['height']
	print "BlockNumber", blockNumber
	for txid in blockData['tx']:
		getTxData = EX.getTxContentByTxid(txid)
		print "TXcontent: ", getTxData
		randomWlts = AG.findAllWalletsAddr(getTxData)
		print "RandomWlrts: ", randomWlts
		if randomWlts != []:
			uniqWlts = AG.aggregateOnlyUniqueWallets(randomWlts)
			print "unique wallets: ", uniqWlts
			for uw in uniqWlts:
				print "Unique one wallet", uw
				createJSON = AG.createJsonForWallet(str(blockNumber), str(blockTime), uw)
				print "Created JSON: ", createJSON

				setProcEnd = int(round(time.time() * 1000))
				performanceResult = str(setProcEnd - setProcStart)
				#print (performanceResult) + ' ms'
				MC.upsertUniqueWallets(collectionForWallets, createJSON)
	# Increase txidsProgress to move forward;
	print "check the end. And what block was ?", currentLastTxidProgress
	MC.updateLastTxidProgressPlusOne(collectionTxidProgress, currentLastTxidProgress)
	currentLastTxidProgress += 1
	qq = MC.findLastTxidProgress(collectionTxidProgress)
	print "Whats is last Block after increase? ", qq
	print "Whats is block after += increase?", currentLastTxidProgress