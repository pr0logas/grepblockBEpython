#:: By GrepBlock.com developers // pr0logas, mrNemo
#:: Modified date: 2019-11-30
#:: Description: This file contains core graphs related methods.

import os, json, sys
import subprocess
from mongoDB import *

class parseGraph():
	def __init__ (self, assetTicker, file, genesisTime):
		self.assetTicker = assetTicker
		self.file = file
		self.path = 'JSON/' + self.file
		self.genesisTime = genesisTime

	def parseBlocksFindLastValue(self):
		if os.path.isfile('JSON/' + self.file):
			readFile = open(self.path, "r") 
			content = (readFile.read())
			cjson = json.loads(content)
			return cjson['values'][-1]['x']
		else:
			try: 
				os.makedirs("JSON")
			except:
				pass

			# Create init json file;
			initJSON = '{"name":"Blocks","unit":"Blocks","period":"day","values":[{"x":' + str(self.genesisTime) +',"y":0}]}'
			try:	
				file = open(self.path, "w") 
				file.write(str(initJSON)) 
				file.close()
				return "FileWasEmpty!"
			except:
				print "FATAL failed to write to the file init data!"
				sys.exit(1)

	def parseTransactionsFindLastValue(self):
		if os.path.isfile('JSON/' + self.file):
			readFile = open(self.path, "r") 
			content = (readFile.read())
			cjson = json.loads(content)
			return cjson['values'][-1]['x']
		else:
			try: 
				os.makedirs("JSON")
			except:
				pass

			# Create init json file;
			initJSON = '{"name":"Transactions","unit":"Transactions","period":"day","values":[{"x":' + str(self.genesisTime) +',"y":0}]}'
			try:	
				file = open(self.path, "w") 
				file.write(str(initJSON)) 
				file.close()
				return "FileWasEmpty!"
			except:
				print "FATAL failed to write to the file init data!"
				sys.exit(1)

	def parseDifficultyFindLastValue(self):
		if os.path.isfile('JSON/' + self.file):
			readFile = open(self.path, "r") 
			content = (readFile.read())
			cjson = json.loads(content)
			return cjson['values'][-1]['x']
		else:
			try: 
				os.makedirs("JSON")
			except:
				pass

			# Create init json file;
			initJSON = '{"name":"Difficulty","unit":"Difficulty","period":"day","values":[{"x":' + str(self.genesisTime) +',"y":0}]}'
			try:	
				file = open(self.path, "w") 
				file.write(str(initJSON)) 
				file.close()
				return "FileWasEmpty!"
			except:
				print "FATAL failed to write to the file init data!"
				sys.exit(1)

	def parseBlockchainSizeFindLastValueTime(self):
		if os.path.isfile('JSON/' + self.file):
			readFile = open(self.path, "r") 
			content = (readFile.read())
			cjson = json.loads(content)
			return cjson['values'][-1]['x']
		else:
			try: 
				os.makedirs("JSON")
			except:
				pass

			# Create init json file;
			initJSON = '{"name":"BlockchainSize","unit":"BlockchainSize","period":"day","values":[{"x":' + str(self.genesisTime) +',"y":0}]}'
			try:	
				file = open(self.path, "w") 
				file.write(str(initJSON)) 
				file.close()
				return "FileWasEmpty!"
			except:
				print "FATAL failed to write to the file init data!"
				sys.exit(1)

	def parseBlockchainSizeFindLastValueSize(self):
			readFile = open(self.path, "r") 
			content = (readFile.read())
			cjson = json.loads(content)
			return cjson['values'][-1]['y']


	def appendNewContentToBlocksGraph(self, sumBlocks, unixTime):
		try:
			new = {"y":str(sumBlocks),"x":str(unixTime)}
			file = open(self.path, "r") 
			content = (file.read())
			cjson = json.loads(content)
			cjson['values'].append(new)
			return json.dumps(cjson)
		except:
			print "FATAL! Failed to append the data to blocks graph!"
			sys.exit(1)

	def appendNewContentToDifficultyGraph(self, difficulty, unixTime):
		try:
			new = {"y":str(difficulty),"x":str(unixTime)}
			file = open(self.path, "r") 
			content = (file.read())
			cjson = json.loads(content)
			cjson['values'].append(new)
			return json.dumps(cjson)
		except:
			print "FATAL! Failed to append the data to difficulty graph!"
			sys.exit(1)

	def appendNewContentToTxsGraph(self, sumTxs, unixTime):
		try:
			new = {"y":str(sumTxs),"x":str(unixTime)}
			file = open(self.path, "r") 
			content = (file.read())
			cjson = json.loads(content)
			cjson['values'].append(new)
			return json.dumps(cjson)
		except:
			print "FATAL! Failed to append the data to Txs graph!"
			sys.exit(1)

	def appendNewContentToBlockchainSizeGraph(self, sumBytes, unixTime):
		try:
			new = {"y":str(sumBytes),"x":str(unixTime)}
			file = open(self.path, "r") 
			content = (file.read())
			cjson = json.loads(content)
			cjson['values'].append(new)
			return json.dumps(cjson)
		except:
			print "FATAL! Failed to append the data to BlockchainSize graph!"
			sys.exit(1)


	def writeJSONtoFile(self, jsonFile):
		try:	
			file = open(self.path, "w") 
			file.write(jsonFile)
			file.close()
			return "OK"
		except:
			print "FATAL failed to write blocks graph to the JSON file."
			sys.exit(1)

	def sendJSONtoFronend(self):
		command = 'scp ./JSON/' + self.file + ' root@websiteHostIP:/usr/share/nginx/grepblockcom/apidata/' + self.assetTicker + '/' + self.file
		try:
			res = subprocess.check_output(command, shell=True).strip()
		except:
			print "FATAL! Failed to copy JSON to FE websiteHostIP"
			sys.exit(1)