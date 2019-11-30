import os, json, sys
from mongoDB import *

class parseGraph():
	def __init__ (self, file, genesisTime):
		self.file = file
		self.check = os.path.isfile('JSON/' + self.file)
		self.path = 'JSON/' + self.file
		self.genesisTime = genesisTime

	def parseBlocksFindLastValue(self):
		if self.check:
			print "Found data in file. All Good. Continuing progress and appending only new data..."
			readFile = open(self.path, "r") 
			content = (readFile.read())
			cjson = json.loads(content)
			lastValue = 0
			index = 1
			try:
				while 0 <= index:
					lastValue = cjson['values'][index]['x']
					index += 1
			except IndexError:
				pass
				return lastValue
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
			except:
				print "FATAL failed to write to the file init data!"
				sys.exit(1)