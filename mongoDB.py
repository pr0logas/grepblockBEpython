#!/usr/bin/env python

import pymongo
import json
import ast
from pymongo.errors import AutoReconnect

mongoAuth = {
	"host" : "127.0.0.1",
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
	def updateLastTxidProgress(self, toCollection, lastTxidProgress):
		decrease = int(lastTxidProgress - 1)
		current = { "lastblock": lastTxidProgress }
		decreasing = { "$set": { "lastblock": decrease } }
		self.mongoDB[toCollection].update_one(current, decreasing)

 	@autoreconnect_retry
	def upsertUniqueWallets(self, toCollection, jsonOfWallets):
		#rint toCollection, (jsonOfWallets)
		data = ast.literal_eval(jsonOfWallets)
		self.mongoDB[toCollection].insert_one(data)