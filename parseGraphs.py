#:: By GrepBlock.com developers // pr0logas, mrNemo
#:: Modified date: 2019-11-30
#:: Description: This file contains core graphs related methods.

import os, json, sys
from mongoDB import *

class parseGraph():
	def __init__ (self, file, genesisTime):
		self.file = file
		self.path = 'JSON/' + self.file
		self.genesisTime = genesisTime

	def parseBlocksFindLastValue(self):
		if os.path.isfile('JSON/' + self.file):
			lastValue = ''
			print "Found data in file. All Good. Continuing progress and appending only new data..."
			readFile = open(self.path, "r") 
			content = (readFile.read())
			cjson = json.loads(content)
			result = ''
			i = 0
			while True:
				try:
					result = cjson['values'][i]['x']
					i =+ 1
				except:
					return result
					break
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


	def appendNewContentToBlocksGraph(self, sumBlocks, unixTime):
		try:
			new = "{'y':" + str(sumBlocks) +",'x':" + str(unixTime) +"}"
			file = open(self.path, "r") 
			content = (file.read())
			cjson = json.loads(content)
			cjson['values'].append(new)
			return json.dumps(cjson)
		except:
			print "FATAL! Failed to append the data to blocks graph!"
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