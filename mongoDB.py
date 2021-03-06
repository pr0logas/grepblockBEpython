#:: By GrepBlock.com developers // pr0logas, mrNemo
#:: Modified date: 2019-12-03 - 2020-03-04
#:: Description: This file contains all MongoDB core methods - find / insert / update / check / assigning mongodb indexes.

import pymongo
import json, ast, time, sys
from time import gmtime, strftime
from pymongo.errors import AutoReconnect
from pymongo import errors as mongoerrors

mongoAuth = {
	"host" : "mongoHostIP",
	"port" : ":27017",
}

class mongoConnection():
	def __init__ (self, mongoAuth, database, collection):
		self.mongoConn = pymongo.MongoClient(mongoAuth['host'] + mongoAuth['port'])
		self.mongoDB = self.mongoConn[database]

	def autoreconnect_retry(fn, retries=10):
		def db_op_wrapper(*args, **kwargs):
			tries = 0

			while tries < retries:
				try:
					return fn(*args, **kwargs)

				except AutoReconnect:
					tries += 1

			raise Exception("MongoDB not responding. No luck even after %d retries" % retries)

		return db_op_wrapper

	@autoreconnect_retry
	def findByBlock(self, fromCollection, blockNum):
		searchBlock = list(self.mongoDB[fromCollection].find({'block' : blockNum}))
		return searchBlock[0]

	@autoreconnect_retry
	def findByTx(self, fromCollection, blockTx):
		searchTx = list(self.mongoDB[fromCollection].find({'tx' : blockTx}))
		return searchTx

	@autoreconnect_retry
	def findLastBlock(self, fromCollection):
		searchLastBlock = list(self.mongoDB[fromCollection].find({},{ "_id": 0, "block": 1}).sort([( '$natural', -1 )] ).limit(1))
		lastBlock = searchLastBlock[0]['block']
		return int(lastBlock)

	@autoreconnect_retry
	def findWallet(self, fromCollection, wallet):
		searchWlt = list(self.mongoDB[fromCollection].find({'wallet' : wallet}))
		return searchWlt

	@autoreconnect_retry
	def findLastTxidProgress(self, fromCollection):
		searchLastTxidProg = list(self.mongoDB[fromCollection].find({},{ "_id": 0, "lastblock": 1}).sort([( '$natural', -1 )] ).limit(1))
		lastTxidProgress = searchLastTxidProg[0]['lastblock']
		return int(lastTxidProgress)

	@autoreconnect_retry
	def findLastHistoricalPrices(self, fromCollection):
		s = list(self.mongoDB[fromCollection].find({},{ "_id": 0, "unix_time": 1}).sort([( '$natural', -1 )] ).limit(1))
		r = s[0]['unix_time']
		return int(r)

	@autoreconnect_retry
	def findLastPriceDataUnixTime(self, fromCollection):
		s = list(self.mongoDB[fromCollection].find({},{ "_id": 0, "unix_time": 1}).sort([( '$natural', -1 )] ).limit(1))
		r = s[0]['unix_time']
		return int(r)

	@autoreconnect_retry
	def findLastPriceGtThan(self, fromCollection, unixTime):
		s = list(self.mongoDB[fromCollection].find({'unix_time': {"$gt": int(unixTime)}}).sort([( '$natural', 1 )] ).limit(1))
		if s == []:
			return "Empty"
		else:
			r = s[0]['unix_time']
			return int(r)

	@autoreconnect_retry
	def findLastPrice(self, fromCollection, unixTime):
		s = list(self.mongoDB[fromCollection].find({'unix_time' : unixTime}).limit(1))
		r = ''
		if 'market_data' in s[0]:
			r = s[0]['market_data']['current_price']['usd']
		else:
			return float(0.0)

		if r is None:
			print('WARNING there are no historical price for unixTime: ' + str(unixTime))
			return float(0.0)
		else:
			return float(r)


	@autoreconnect_retry
	def findLastMarketCap(self, fromCollection, unixTime):
		s = list(self.mongoDB[fromCollection].find({'unix_time' : unixTime}).limit(1))
		r = ''
		if 'market_data' in s[0]:
			r = s[0]['market_data']['market_cap']['usd']
		else:
			return float(0.0)

		if r is None:
			print('WARNING there are no historical price for unixTime: ' + str(unixTime))
			return float(0.0)
		else:
			return float(r)

	@autoreconnect_retry
	def findLastVolume(self, fromCollection, unixTime):
		s = list(self.mongoDB[fromCollection].find({'unix_time' : unixTime}).limit(1))
		r = ''
		if 'market_data' in s[0]:
			r = s[0]['market_data']['total_volume']['usd']
		else:
			return float(0.0)

		if r is None:
			print('WARNING there are no historical price for unixTime: ' + str(unixTime))
			return float(0.0)
		else:
			return float(r)

	@autoreconnect_retry
	def findLastMarketCapQuick(self, fromCollection, unixTime):
		s = list(self.mongoDB[fromCollection].find({'unix_time' : unixTime}).limit(1))
		try:
			r = s[0]['market_cap']
			return float(r)
		except KeyError:
			return 'KeyError'

	@autoreconnect_retry
	def findLastVolumeQuick(self, fromCollection, unixTime):
		s = list(self.mongoDB[fromCollection].find({'unix_time' : unixTime}).limit(1))
		try:
			r = s[0]['total_volume']
			return float(r)
		except KeyError:
			return 'KeyError'

	@autoreconnect_retry
	def findLastPriceQuick(self, fromCollection, unixTime):
		s = list(self.mongoDB[fromCollection].find({'unix_time' : unixTime}).limit(1))
		try:
			r = s[0]['current_price']
			return float(r)
		except KeyError:
			return 'KeyError'

	@autoreconnect_retry
	def findLastBlockTime(self, fromCollection, unixTime):
		s = list(self.mongoDB[fromCollection].find({'time' : int(unixTime)}))
		r = s[0]['block']
		return int(r)

	@autoreconnect_retry
	def findLastBlockMedianTime(self, fromCollection, unixTime):
		s = list(self.mongoDB[fromCollection].find({'mediantime' : int(unixTime)}))
		r = s[0]['block']
		return int(r)

	@autoreconnect_retry
	def findLastDiffbyTime(self, fromCollection, unixTime):
		s = list(self.mongoDB[fromCollection].find({'time' : int(unixTime)}))
		r = s[0]['time']
		return int(r)

	@autoreconnect_retry
	def findLastActiveWalletsbyTime(self, fromCollection, unixTime):
		s = list(self.mongoDB[fromCollection].find({'time' : int(unixTime)}))
		r = s[0]['time']
		return int(r)

	@autoreconnect_retry
	def findLastActiveWalletsbyTimeReturnBlock(self, fromCollection, unixTime):
		s = list(self.mongoDB[fromCollection].find({'time' : int(unixTime)}))
		r = s[0]['block']
		return int(r)

	@autoreconnect_retry
	def findDiffGtThan(self, fromCollection, unixTime):
		s = list(self.mongoDB[fromCollection].find({'time': {"$gt": int(unixTime)}}).sort([( '$natural', 1 )] ).limit(1))
		if s == []:
			return "Empty"
		else:
			r = s[0]['difficulty']
			return float(r)

	@autoreconnect_retry
	def findDiffGtThanReturnTime(self, fromCollection, unixTime):
		s = list(self.mongoDB[fromCollection].find({'time': {"$gt": int(unixTime)}}).sort([( '$natural', 1 )] ).limit(1))
		r = s[0]['time']
		return int(r)

	@autoreconnect_retry
	def findActiveWalletsGtThan(self, fromCollection, unixTime):
		s = list(self.mongoDB[fromCollection].find({'time': {"$gt": int(unixTime)}}).sort([( '$natural', 1 )] ).limit(1))
		if s == []:
			return "Empty"
		else:
			r = s[0]['time']
			return float(r)

	@autoreconnect_retry
	def findActiveWalletsGtThanReturnBlock(self, fromCollection, unixTime):
		s = list(self.mongoDB[fromCollection].find({'time': {"$gt": int(unixTime)}}).sort([('$natural', 1)]).limit(1))
		if s == []:
			return int(10000000000) # Send 10 Billions in order to stop //
		else:
			r = s[0]['block']
		return int(r)

	@autoreconnect_retry
	def findActiveWalletsGtThanCalc1(self, fromCollection, unixTime):
		ut = int(unixTime)
		s = (self.mongoDB[fromCollection].count_documents({'walletTime': {"$lt": ut}}))
		return int(s)

	@autoreconnect_retry
	def findActiveWalletsGtThanCalc2(self, fromCollection, unixTime):
		ut = int(unixTime)
		s = (self.mongoDB[fromCollection].count_documents({'walletTime': {"$lt": ut}}))
		return int(s)

	@autoreconnect_retry
	def findActiveWalletsGtThanReturnTime(self, fromCollection, unixTime):
		s = list(self.mongoDB[fromCollection].find({'time': {"$gt": int(unixTime)}}).sort([( '$natural', 1 )] ).limit(1))
		r = s[0]['time']
		return int(r)

	@autoreconnect_retry
	def findBasicInfo(self, fromCollection, whatToFind):
		check = list(self.mongoDB[fromCollection].find({whatToFind: {"$exists": "true"}},{ "_id": 0, whatToFind : 1})).limit(1)
		if check == []:
			print("Collumn is empty!")
			sys.exit(1)
		else:
			return str(check)

	@autoreconnect_retry
	def updateLastTxidProgressPlusOne(self, toCollection, lastTxidProgress):
		increasing = int(lastTxidProgress)
		decresing = int(lastTxidProgress -1)
		current = { "lastblock": decresing }
		new = { "$set": { "lastblock": increasing } }
		self.mongoDB[toCollection].update_one(current, new)

	@autoreconnect_retry
	def updateLastTxidProgressMinusOne(self, toCollection, lastTxidProgress):
		decrease = int(lastTxidProgress - 1)
		current = { "lastblock": lastTxidProgress }
		decreasing = { "$set": { "lastblock": decrease } }
		self.mongoDB[toCollection].update_one(current, decreasing)

	@autoreconnect_retry
	def upsertUniqueWallets(self, toCollection, jsonOfWallets):
		data = eval(jsonOfWallets)
		#print(mongoerrors.__dict__.keys())
		try:	
			self.mongoDB[toCollection].insert(data)
			return str(data['wallet'])
		except pymongo.errors.DuplicateKeyError:
			timeSet = strftime("%Y-%m-%d %H:%M:%S", gmtime())
			print timeSet + " MongoDB dup wlt, skip"
			pass

	@autoreconnect_retry
	def insertInitValueForBlocks(self, toCollection):
		data = '{ "block" : 0 }'
		setData = ast.literal_eval(data)
		self.mongoDB[toCollection].insert(setData)
		print "**Creating required indexes for MongoDB**"
		self.mongoDB[toCollection].create_index([('block', pymongo.ASCENDING)], unique=True)
		self.mongoDB[toCollection].create_index([('tx', pymongo.ASCENDING)])
		self.mongoDB[toCollection].create_index([('hash', pymongo.ASCENDING)])
		self.mongoDB[toCollection].create_index([('merkleroot', pymongo.ASCENDING)])
		self.mongoDB[toCollection].create_index([('time', pymongo.DESCENDING)])
		self.mongoDB[toCollection].create_index([('mediantime', pymongo.DESCENDING)])

	@autoreconnect_retry
	def insertInitValueForWalletsProgress(self, toCollection):
		data = '{ "lastblock" : 0 }'
		setData = ast.literal_eval(data)
		print "**Creating required indexes for MongoDB**"
		self.mongoDB[toCollection].insert(setData)
		self.mongoDB[toCollection].create_index([('lastblock', pymongo.ASCENDING)], unique=True)
		self.mongoDB['wallets'].create_index([('walletTime', pymongo.ASCENDING)])
		self.mongoDB['wallets'].create_index([('block', pymongo.ASCENDING)])
		self.mongoDB['wallets'].create_index([('wallet', pymongo.ASCENDING)], unique=True)

	@autoreconnect_retry
	def insertInitValueForHP(self, toCollection, time):
		data = '{ "unix_time" : ' + str(time) + ' }'
		setData = ast.literal_eval(data)
		self.mongoDB[toCollection].insert(setData)
		print "**Creating required indexes for MongoDB**"
		self.mongoDB[toCollection].create_index([('unix_time', pymongo.ASCENDING)], unique=True)
		self.mongoDB['priceDataUSD'].create_index([('unix_time', pymongo.ASCENDING)], unique=True)

		
	@autoreconnect_retry
	def insertBlocksData(self, toCollection, aggregatedBlockData):
		data = eval(aggregatedBlockData)
		#data = ast.literal_eval(aggregatedBlockData)
		try:
			self.mongoDB[toCollection].insert(data)
			return str(data['block'])
		except pymongo.errors.DuplicateKeyError:
			timeSet = strftime("%Y-%m-%d %H:%M:%S", gmtime())
			print timeSet + " MongoDB found a duplicate block: " + str(data['block']) + ', skipping...'
			pass

	@autoreconnect_retry
	def insertPricesData(self, toCollection, aggregatedPricesData):
		data = eval(aggregatedPricesData)
		#data = ast.literal_eval(aggregatedBlockData)
		try:
			self.mongoDB[toCollection].insert(data)
			return str(data['current_price'])
		except:
			timeSet = strftime("%Y-%m-%d %H:%M:%S", gmtime())
			print(timeSet + " MongoDB failed to insert Price Data!")
			print(data)
			sys.exit(1)

	@autoreconnect_retry
	def insertHistoricalPricesData(self, toCollection, aggregatedHPData):
		null = None
		data = eval(aggregatedHPData)
		#data = ast.literal_eval(aggregatedBlockData)
		try:
			self.mongoDB[toCollection].insert(data)
			return str(data['market_data']['current_price']['usd'])
		except:
			timeSet = strftime("%Y-%m-%d %H:%M:%S", gmtime())
			print(timeSet + " MongoDB failed to insert Historical Price Data!")
			print(data)
			sys.exit(1)

	@autoreconnect_retry
	def checkIfBlocksColEmpty(self, fromCollection):
		check = list(self.mongoDB[fromCollection].find({},{ "_id": 0, "block": 1}).sort([( '$natural', -1 )] ).limit(1))
		if check == []:
			return "Empty"

	@autoreconnect_retry
	def checkIfTxidProgressColEmpty(self, fromCollection):	
		check = list(self.mongoDB[fromCollection].find({},{ "_id": 0, "lastblock": 1}).sort([( '$natural', -1 )] ).limit(1))
		if check == []:
			return "Empty"

	@autoreconnect_retry
	def checkIfHistoricalPricesColEmpty(self, fromCollection):	
		check = list(self.mongoDB[fromCollection].find({},{ "_id": 0, "unix_time": 1}).sort([( '$natural', -1 )] ).limit(1))
		if check == []:
			return "Empty"

###########################   Basic asset info methods #############################
	@autoreconnect_retry
	def findAssetName(self, fromCollection):
		res = list(self.mongoDB[fromCollection].find({"assetName" : {"$exists":True}},{ "_id": 0, "assetName" : 1}).limit(1))
		return res[0]

	@autoreconnect_retry
	def findAssetType(self, fromCollection):
		res = list(self.mongoDB[fromCollection].find({"assetType" : {"$exists":True}},{ "_id": 0, "assetType" : 1}).limit(1))
		return res[0]

	@autoreconnect_retry
	def findAssetTicker(self, fromCollection):
		res = list(self.mongoDB[fromCollection].find({"assetTicker" : {"$exists":True}},{ "_id": 0, "assetTicker" : 1}).limit(1))
		return res[0]

	@autoreconnect_retry
	def findAssetMineable(self, fromCollection):
		res = list(self.mongoDB[fromCollection].find({"mineable" : {"$exists":True}},{ "_id": 0, "mineable" : 1}).limit(1))
		return res[0]

	@autoreconnect_retry
	def findAssetMasternode(self, fromCollection):
		res = list(self.mongoDB[fromCollection].find({"masternode" : {"$exists":True}},{ "_id": 0, "masternode" : 1}).limit(1))
		return res[0]

	@autoreconnect_retry
	def findAssetSourceCode(self, fromCollection):
		res = list(self.mongoDB[fromCollection].find({"sourceCode" : {"$exists":True}},{ "_id": 0, "sourceCode" : 1}).limit(1))
		return res[0]

	@autoreconnect_retry
	def findAssetBlockTime(self, fromCollection):
		res = list(self.mongoDB[fromCollection].find({"blockTime" : {"$exists":True}},{ "_id": 0, "blockTime" : 1}).limit(1))
		return res[0]

	@autoreconnect_retry
	def findAssetMaxSupply(self, fromCollection):
		res = list(self.mongoDB[fromCollection].find({"maxSupply" : {"$exists":True}},{ "_id": 0, "maxSupply" : 1}).limit(1))
		return res[0]

	@autoreconnect_retry
	def findAssetBlockSize(self, fromCollection):
		res = list(self.mongoDB[fromCollection].find({"blockSize" : {"$exists":True}},{ "_id": 0, "blockSize" : 1}).limit(1))
		return res[0]

	@autoreconnect_retry
	def findAssetWalletPrefix(self, fromCollection):
		res = list(self.mongoDB[fromCollection].find({"walletPrefix" : {"$exists":True}},{ "_id": 0, "walletPrefix" : 1}).limit(1))
		return res[0]

	@autoreconnect_retry
	def findAssetExplorer(self, fromCollection):
		res = list(self.mongoDB[fromCollection].find({"explorer" : {"$exists":True}},{ "_id": 0, "explorer" : 1}).limit(1))
		return res[0]

	@autoreconnect_retry
	def findAssetExplorer2(self, fromCollection):
		res = list(self.mongoDB[fromCollection].find({"explorer2" : {"$exists":True}},{ "_id": 0, "explorer2" : 1}).limit(1))
		return res[0]

	@autoreconnect_retry
	def findAssetExplorer3(self, fromCollection):
		res = list(self.mongoDB[fromCollection].find({"explorer3" : {"$exists":True}},{ "_id": 0, "explorer3" : 1}).limit(1))
		return res[0]

	@autoreconnect_retry
	def findAssetWebsite(self, fromCollection):
		res = list(self.mongoDB[fromCollection].find({"website" : {"$exists":True}},{ "_id": 0, "website" : 1}).limit(1))
		return res[0]

	@autoreconnect_retry
	def findAssetRpcPort(self, fromCollection):
		res = list(self.mongoDB[fromCollection].find({"rpcPort" : {"$exists":True}},{ "_id": 0, "rpcPort" : 1}).limit(1))
		return res[0]

	@autoreconnect_retry
	def findAssetNetworkPort(self, fromCollection):
		res = list(self.mongoDB[fromCollection].find({"networkPort" : {"$exists":True}},{ "_id": 0, "networkPort" : 1}).limit(1))
		return res[0]

	@autoreconnect_retry
	def findAssetBitcointalkThread(self, fromCollection):
		res = list(self.mongoDB[fromCollection].find({"bitcointalkThread" : {"$exists":True}},{ "_id": 0, "bitcointalkThread" : 1}).limit(1))
		return res[0]

	@autoreconnect_retry
	def findAssetTelegram(self, fromCollection):
		res = list(self.mongoDB[fromCollection].find({"telegram" : {"$exists":True}},{ "_id": 0, "telegram" : 1}).limit(1))
		return res[0]

	@autoreconnect_retry
	def findAssetReddit(self, fromCollection):
		res = list(self.mongoDB[fromCollection].find({"reddit" : {"$exists":True}},{ "_id": 0, "reddit" : 1}).limit(1))
		return res[0]

	@autoreconnect_retry
	def findAssetTwitter(self, fromCollection):
		res = list(self.mongoDB[fromCollection].find({"twitter" : {"$exists":True}},{ "_id": 0, "twitter" : 1}).limit(1))
		return res[0]

	@autoreconnect_retry
	def findAssetChat(self, fromCollection):
		res = list(self.mongoDB[fromCollection].find({"chat" : {"$exists":True}},{ "_id": 0, "chat" : 1}).limit(1))
		return res[0]

	@autoreconnect_retry
	def findAssetAbout(self, fromCollection):
		res = list(self.mongoDB[fromCollection].find({"about" : {"$exists":True}},{ "_id": 0, "about" : 1}).limit(1))
		return res[0]

	@autoreconnect_retry
	def findAssetAlgorithm(self, fromCollection):
		res = list(self.mongoDB[fromCollection].find({"algorithm" : {"$exists":True}},{ "_id": 0, "algorithm" : 1}).limit(1))
		return res[0]

	@autoreconnect_retry
	def findAssetDeveloperFee(self, fromCollection):
		res = list(self.mongoDB[fromCollection].find({"developerFee" : {"$exists":True}},{ "_id": 0, "developerFee" : 1}).limit(1))
		return res[0]

	@autoreconnect_retry
	def findAssetWhitepaper(self, fromCollection):
		res = list(self.mongoDB[fromCollection].find({"whitepaper" : {"$exists":True}},{ "_id": 0, "whitepaper" : 1}).limit(1))
		return res[0]

	@autoreconnect_retry
	def findAssetFirstBlock(self, fromCollection):
		res = list(self.mongoDB[fromCollection].find({"firstBlock" : {"$exists":True}},{ "_id": 0, "firstBlock" : 1}).limit(1))
		return res[0]