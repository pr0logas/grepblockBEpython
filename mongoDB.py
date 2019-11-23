#!/usr/bin/env python

"""
Install modules:
	apt install python-pip
	pip install pymongo
"""

import pymongo
from pymongo.errors import AutoReconnect

mongoAuth = {
	"host" : "127.0.0.1",
	"port" : ":27017",
	"db" : "adeptio",
	"col" : "blocks"
}

class mongoConnection():
	def __init__ (self, mongoAuth):
		self.mongoConn = pymongo.MongoClient(mongoAuth['host'] + mongoAuth['port'])
		self.mongoDB = self.mongoConn[mongoAuth["db"]]
		self.mongoCol = self.mongoDB[mongoAuth["col"]]

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
	def findByBlock(self, blockNum):
		searchBlock = list(self.mongoCol.find({'block' : blockNum}))
		return searchBlock

	@autoreconnect_retry
	def findByTx(self, blockTx):
		searchTx = list(self.mongoCol.find({'tx' : blockTx}))
		return searchTx

	@autoreconnect_retry
	def findLastBlock(self):
		searchLastBlock = list(self.mongoCol.find({},{ "_id": 0, "block": 1}).sort([( '$natural', -1 )] ).limit(1))
		lastBlock = searchLastBlock[0]['block']
  		return lastBlock