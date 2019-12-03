#:: By GrepBlock.com developers // pr0logas, mrNemo
#:: Modified date: 2019-12-03
#:: Description: This file is a workspace for assetGraph creation.

import sys, time
from datetime import datetime, timedelta
from time import gmtime, strftime
from adeptio import *
sys.path.append('../../../')
from mongoDB import *
from parseGraphs import parseGraph

db = database
collectionForPrices = "priceDataUSD"
collectionForHistoricalPrices = "historicalPriceData"

# Init Classes;
PG = parseGraph(assetTicker, fileForPrice, genesisBlock)
MC = mongoConnection(mongoAuth, db, collectionForHistoricalPrices)

# Find Last unixTime value in a working json file;
lU = PG.parsePriceFindLastValue(coinGeckoStartUnixTime)
if lU == 'FileWasEmpty!':
	lU = PG.parsePriceFindLastValue(coinGeckoStartUnixTime)
	print("Warning, file was empty, init zero params!")

print lU

# Find the same but in MongoDB;
lastUnixTimeinDB = MC.findLastPriceDataUnixTime(collectionForHistoricalPrices)

print lastUnixTimeinDB

while True:
	lU = PG.parsePriceFindLastValue(coinGeckoStartUnixTime)
	unixTime = MC.findLastPriceGtThan(collectionForHistoricalPrices, lU)
	if unixTime == 'Empty':
		print 'empty'
		break
	else:
		price = MC.findLastPrice(collectionForHistoricalPrices, unixTime)
		resJSON = PG.appendNewContentToPriceGraph(float(price), unixTime)
		resWrite = PG.writeJSONtoFile(resJSON)
		printTime = (datetime.fromtimestamp(unixTime)).strftime('%Y-%m-%d')
		if resWrite == 'OK':
			print timeSet + " Found historical Price: " + str(price) + " // We at " + str(printTime)
		else:
			print "FATAL!"
			sys.exit(1)
		print resJSON