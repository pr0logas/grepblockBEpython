#:: By GrepBlock.com developers // pr0logas, mrNemo
#:: Modified date: 2019-12-03
#:: Description: This file is a workspace for assetGraph creation.

import sys, time
from datetime import datetime, timedelta
from time import gmtime, strftime
from memetic import *
sys.path.append('../../../')
from mongoDB import *
from parseGraphs import parseGraph

db = database
collectionForPrices = "priceDataUSD"

# Init Classes;
PG = parseGraph(assetTicker, fileForMarketCap, genesisBlock)
MC = mongoConnection(mongoAuth, db, collectionForPrices)

# Find Last unixTime value in a working json file;
lU = PG.parsePriceFindLastValue(coinGeckoStartUnixTime)
if lU == 'FileWasEmpty!':
	lU = PG.parsePriceFindLastValue(coinGeckoStartUnixTime)
	print("Warning, file was empty, init zero params!")

# Find the same but in MongoDB;
lastUnixTimeinDB = MC.findLastPriceDataUnixTime(collectionForPrices)

while True:
	lU = PG.parsePriceFindLastValue(coinGeckoStartUnixTime)
	unixTime = MC.findLastPriceGtThan(collectionForPrices, lU)
	if unixTime == 'Empty':
		# Send new JSON to FE;
		PG.sendJSONtoFronend()
		timeSet = strftime("%Y-%m-%d %H:%M:%S", gmtime())
		print(timeSet +" ***JSON copied to FE instance***")
		print(timeSet +" All tasks were successful.")
		break
	else:
		printTime = (datetime.fromtimestamp(unixTime)).strftime('%Y-%m-%d %H:%M:%S')
		price = MC.findLastMarketCapQuick(collectionForPrices, unixTime)
		if price == 'KeyError':
			print('WARNING! Cannot parse price in unixTime, KeyError: ' + str(unixTime))
			sys.exit(1)
		resJSON = PG.appendNewContentToPriceGraph(float(price), unixTime)
		resWrite = PG.writeJSONtoFile(resJSON)
		if resWrite == 'OK':
			timeSet = strftime("%Y-%m-%d %H:%M:%S", gmtime())
			print timeSet + " Found MarketCap: " + str(price) + " // We at " + str(printTime)
		else:
			print("FATAL!")
			sys.exit(1)