#:: By GrepBlock.com developers // pr0logas, mrNemo
#:: Modified date: 2019-12-03
#:: Description: This file is a workspace for assetGraph creation.

import sys, time
from datetime import datetime, timedelta
from time import gmtime, strftime
from dash import *

sys.path.append('../../../')
from mongoDB import *
from parseGraphs import parseGraph

db = database
collectionForBlocks = "blocks"
collectionForWalletsProgress = "txidsProgress"
collectionForWallets = "wallets"

# Init Classes;
PG = parseGraph(assetTicker, fileForActiveWalletsCount, genesisBlock)
MC = mongoConnection(mongoAuth, db, collectionForBlocks)

# Find Last unixTime value in a working json file;
lU = PG.parseActiveWalletsFindLastValue()
if lU == 'FileWasEmpty!':
	lU = PG.parseActiveWalletsFindLastValue()
	print("Warning, file was empty, init zero params!")

lP = MC.findLastTxidProgress(collectionForWalletsProgress)

while True:
	lU = PG.parseActiveWalletsFindLastValue()
	lastProgress = MC.findLastActiveWalletsbyTime(collectionForBlocks, lU)
	averageBlkMinus = (86400 - int(blockTime))
	lastProgress = (lastProgress + averageBlkMinus)

	lBLK = MC.findActiveWalletsGtThanReturnBlock(collectionForBlocks, lastProgress)

	if lBLK >= lP:
		timeSet = strftime("%Y-%m-%d %H:%M:%S", gmtime())
		print(timeSet + " Stopped parsing blocks with Active Wallets at: " + str(lBLK) + ' Block')
		break
	else:
		diffRes = MC.findActiveWalletsGtThan(collectionForBlocks, lastProgress)
		# Search only < 3 month older activeWallet count;
		searchActiveWltMinus3mos = int(int(diffRes) - 7776000)
		currentWalletsMinus3mos = MC.findActiveWalletsGtThanCalc1(collectionForWallets, searchActiveWltMinus3mos)
		searchingForActiveWlt = MC.findActiveWalletsGtThanCalc2(collectionForWallets, int(lastProgress))
		result = (searchingForActiveWlt - currentWalletsMinus3mos)

		unixTime = MC.findActiveWalletsGtThanReturnTime(collectionForBlocks, lastProgress)
		printTime = (datetime.fromtimestamp(unixTime)).strftime('%Y-%m-%d')
		timeSet = strftime("%Y-%m-%d %H:%M:%S", gmtime())
		resJSON = PG.appendNewContentToDifficultyGraph(int(result), unixTime)
		resWrite = PG.writeJSONtoFile(resJSON)
		if resWrite == 'OK':
			print(timeSet + " Next day found. Active Wallets: " + str(result) + " // We at " + str(printTime))
		else:
			print("FATAL!")
			sys.exit(1)

# Send new JSON to FE;
PG.sendJSONtoFronend()
timeSet = strftime("%Y-%m-%d %H:%M:%S", gmtime())
print(timeSet + " ***JSON copied to FE instance***")
print(timeSet + " All tasks were successful.")