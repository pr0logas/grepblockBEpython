import pymongo
import json, ast, time
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
	def findLastTxidProgress(self, fromCollection):
		searchLastTxidProg = list(self.mongoDB[fromCollection].find({},{ "_id": 0, "lastblock": 1}).sort([( '$natural', -1 )] ).limit(1))
		lastTxidProgress = searchLastTxidProg[0]['lastblock']
  		return int(lastTxidProgress)

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

 	@autoreconnect_retry
	def insertInitValueForWalletsProgress(self, toCollection):
		data = '{ "lastblock" : 0 }'
		setData = ast.literal_eval(data)
		self.mongoDB[toCollection].insert(setData)

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
	def checkIfBlocksColEmpty(self, fromCollection):
		check = list(self.mongoDB[fromCollection].find({},{ "_id": 0, "block": 1}).sort([( '$natural', -1 )] ).limit(1))
		if check == []:
			return "Empty"

	@autoreconnect_retry
	def checkIfTxidProgressColEmpty(self, fromCollection):	
		check = list(self.mongoDB[fromCollection].find({},{ "_id": 0, "lastblock": 1}).sort([( '$natural', -1 )] ).limit(1))
		if check == []:
			return "Empty"