#!/usr/bin/env python

import json
from mongoDB import mongoAuth, mongoConnection
from performance import perfResult
from explorer import *

class aggregateWalletsData():
	def __init__(self, data):
		self.data = data
	
	def findAllWalletsAddr(self):
		firstObj = json.loads(self.data)
		nestedData = firstObj['vout']
		resultList = []
		for i in nestedData:
			try:
				for y in i['scriptPubKey']['addresses']:
     					resultList.append(y)
 			except KeyError:
     				continue

     		return resultList

	def aggregateOnlyUniqueWallets(self, wallets):
		output = set()
		for x in wallets:
    			output.add(x)

		return output

	def aggregateOnlyTxidHashes(self, blockData):
		firstObj = json.loads(blockData)
		nestedData = firstObj['tx']
		resultList = []
		for i in nestedData:
     			resultList.append(i)
 			
     		return resultList