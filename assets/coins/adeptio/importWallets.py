#!/usr/bin/env python

import sys
from adeptio import *
sys.path.append('../../../')
from mongoDB import *
from parseWallets import * 
from performance import perfResult, setTimeCommand, time
from explorer import iquidusExplorer
from parseWallets import aggregateWalletsData

collectionTxidProgress = "txidsProgress"
collectionForBlocks = "blocks"
setProcStart = setTimeCommand

# Init Mongo Connection
MC = mongoConnection(mongoAuth, database, collectionTxidProgress)

# Set current progress;
currentLastTxidProgress = MC.findLastTxidProgress()
currentLastBlock = MC.findLastBlock(collectionForBlocks)

#print currentLastBlock
#print currentLastTxidProgress

# Init Explorer params
EX = iquidusExplorer(chainProvider, getBlockIndexMethod, getBlockwithHashMethod, getTx)

#print EX.getBlockHash('5')
#print EX.getBlockContentByHash('00000ffa49117a1763cbd558eab797dd6f046acf3d058f4ce1ee1ab53e926191')
#print EX.getTxContentByTxid('890531d6773d1fb716422a2bdf9e1b561dd727b77edabe19e50ea59153b747bb')

AG = aggregateWalletsData(EX.getTxContentByTxid('61fb082ec47b267f02345bb2e171b671d3f54ff0d07fd39dc38777569fe5d851'))
#randomWlts = AG.findAllWalletsAddr()
#uniqWlts = AG.aggregateOnlyUniqueWallets(randomWlts)
#print uniqWlts

# Decrease txidsProgress value in case of previuos failure;
MC.updateLastTxidProgress(currentLastTxidProgress)

if int(MC.findLastTxidProgress()) == int(currentLastTxidProgress):
	print ("FAIL: Unable to decrease lastblock value in txidsProgress!")
	sys.exit(1)
else:
	print ("OK: txidsProgress value succesfully decreased.")

while currentLastTxidProgress <=currentLastBlock:
	hashID = EX.getBlockHash(str(currentLastTxidProgress))
	blockData = EX.getBlockContentByHash(str(hashID))
	txidHashes = AG.aggregateOnlyTxidHashes(blockData)
	for i in txidHashes:
		AG = aggregateWalletsData(EX.getTxContentByTxid(i))
		print i 