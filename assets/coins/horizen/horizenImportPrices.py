#:: By GrepBlock.com developers // pr0logas
#:: Modified date: 2019-11-30
#:: Description: This file is a workspace for Prices importation.

import sys, time
from time import gmtime, strftime
from horizen import *
sys.path.append('../../../')
from mongoDB import *
from parsePrices import parseCoinGeckoPrices

db = database
col = collectionForPricesUSD

# Init Classes;
MC = mongoConnection(mongoAuth, db, col)
PP = parseCoinGeckoPrices(apiProvider, vsCurrencyUSD, 'zencash')

# CoinGecko
result = PP.parsePrice()

# Insert Unix Time
aggregatedData = PP.aggregateInsertUnixTime(result)

#Insert to MongoDB
res = MC.insertPricesData(collectionForPricesUSD, aggregatedData)
timeSet = strftime("%Y-%m-%d %H:%M:%S", gmtime())
print timeSet + " Succefully inserted asset price: $" + res