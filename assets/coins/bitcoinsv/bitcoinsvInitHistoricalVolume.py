#:: By GrepBlock.com developers // pr0logas, mrNemo
#:: Modified date: 2019-12-03
#:: Description: This file is a workspace for assetGraph creation.

import sys, time
from datetime import datetime, timedelta
from time import gmtime, strftime
from bitcoinsv import *
sys.path.append('../../../')
from mongoDB import *
from parseGraphs import parseGraph

db = database
collectionForHistoricalPrices = "historicalPriceData"

# Init Classes;
PG = parseGraph(assetTicker, fileForVolume, genesisBlock)
MC = mongoConnection(mongoAuth, db, collectionForHistoricalPrices)

# Find Last unixTime value in a working json file;
lU = PG.parsePriceFindLastValue(coinGeckoStartUnixTime)
if lU == 'FileWasEmpty!':
	lU = PG.parsePriceFindLastValue(coinGeckoStartUnixTime)
	print("Warning, file was empty, init zero params!")

# Find the same but in MongoDB;
lastUnixTimeinDB = MC.findLastPriceDataUnixTime(collectionForHistoricalPrices)

while True:
	lU = PG.parsePriceFindLastValue(coinGeckoStartUnixTime)
	unixTime = MC.findLastPriceGtThan(collectionForHistoricalPrices, lU)
	if unixTime == 'Empty':
		# Send new JSON to FE;
		PG.sendJSONtoFronend()
		timeSet = strftime("%Y-%m-%d %H:%M:%S", gmtime())
		print(timeSet +" ***JSON copied to FE instance***")
		print(timeSet +" All tasks were successful.")
		break
	else:
		printTime = (datetime.fromtimestamp(unixTime)).strftime('%Y-%m-%d')
		price = MC.findLastVolume(collectionForHistoricalPrices, unixTime)
		resJSON = PG.appendNewContentToPriceGraph(float(price), unixTime)
		resWrite = PG.writeJSONtoFile(resJSON)
		if resWrite == 'OK':
			timeSet = strftime("%Y-%m-%d %H:%M:%S", gmtime())
			print(timeSet + " Found historical Volume: " + str(price) + " // We at " + str(printTime))
		else:
			print("FATAL!")
			sys.exit(1)