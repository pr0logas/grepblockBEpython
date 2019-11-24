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
		for i in nestedData:
			try:
				for y in i['scriptPubKey']['addresses']:
     					print y
 			except KeyError:
     				continue