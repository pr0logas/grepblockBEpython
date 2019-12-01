#:: By GrepBlock.com developers // pr0logas
#:: Modified date: 2019-11-30
#:: Description: This file is a workspace for Historical Prices importation.

import sys, time
from time import gmtime, strftime
from adeptio import *
sys.path.append('../../../')
from mongoDB import *
from parseHistoricalPrices import parseCoinGeckoHistoricalPrices

db = database
col = collectionForHistoricalPricesUSD
coingckstart = coinGeckoStartUnixTime

# Init Classes;
MC = mongoConnection(mongoAuth, db, col)
PP = parseCoinGeckoHistoricalPrices(apiProvider, vsCurrencyUSD, assetName)


# Check if blocks col empty or not?
if MC.checkIfHistoricalPricesColEmpty(col) == "Empty":
	print "Warning! We found an empty HistoricalPrices collection. Starting from zero."
	MC.insertInitValueForHP(col, coingckstart)

# MongoDB check last progress;
lastTime = MC.findLastHistoricalPrices(col)
lastTime = (int(lastTime) + 86400) # Increase 1 day

# CoinGecko
result = PP.parseHistoricalPrice(lastTime)

# Insert Unix Time
aggregatedData = PP.aggregateInsertUnixTime(result, lastTime)

#Insert to MongoDB
res = MC.insertHistoricalPricesData(col, aggregatedData)
timeSet = strftime("%Y-%m-%d %H:%M:%S", gmtime())
print timeSet + " Succefully inserted asset historical price: $" + res