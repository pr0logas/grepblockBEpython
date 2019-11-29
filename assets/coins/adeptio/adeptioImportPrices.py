import sys, time
from time import gmtime, strftime
from adeptio import *
sys.path.append('../../../')
from mongoDB import *
from parsePrices import parseCoinGeckoPrices

db = database
collectionForPricesUSD = 'priceDataUSD'

# Init Classes;
MC = mongoConnection(mongoAuth, db, collectionForPricesUSD)
PP = parseCoinGeckoPrices(apiProvider, vsCurrencyUSD, assetName)

# CoinGecko
result = PP.parsePrice()

# Insert Unix Time
aggregatedData = PP.aggregateInsertUnixTime(result)

#Insert to MongoDB
res = MC.insertPricesData(collectionForPricesUSD, aggregatedData)
print res
