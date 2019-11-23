#!/usr/bin/env python

"""
Install modules:
	pip install pymongo
"""

import sys
import os
import json
import requests
from adeptio.adeptio import *

class iquidusExplorer():
	def __init__ (self):
		self.r = requests

	def getBlockHash(self, blockNum):
		result = list(self.r.get(chainProvider+getBlockIndexMethod+blockNum))
		return result[0]

	def getBlockContentByHash(self, blockHash):
		result = list(self.r.get(chainProvider+getBlockwithHashMethod+blockHash))
		print (result[0])s
		


"""
r.status_code
200
r.headers['content-type']
'application/json; charset=utf8'
r.encoding
'utf-8'
r.text
u'{"type":"User"...'
r.json()
{u'private_gists': 419, u'total_private_repos': 77, ...}
"""