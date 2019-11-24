#!/usr/bin/env python

import json ,re
from mongoDB import mongoAuth, mongoConnection
from performance import perfResult
from explorer import *

class aggregateWalletsData():
	def __init__(self, data):
		self.data = data
	
	def findAllWalletsAddr(self):
		firstObj = json.loads(self.data)
		print firstObj
		nestedData = str(firstObj['vout'])
		print nestedData
		#result = re.search('addresses(.*)OP_CHECKSIG', nestedData)
		#print(result.group(1))
