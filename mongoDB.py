#!/usr/bin/env python

import pymongo

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

	def findBlocks(self, blockNum):
		searchBlock = list(self.mongoCol.find({'block' : blockNum}))
		return searchBlock


MC = mongoConnection(mongoAuth)
result = MC.findBlocks(1);

print result