import json, fileinput
from explorer import iquidusExplorer
import os, pprint
from pprint import pprint

class aggregateBlocksData():
	def __init__(self):
		pass

	def aggregateInsertBlockNumber(self, blockData):
		print blockData
		originalData = blockData
		firstObj = json.loads(blockData)
		findBlockNum = int(firstObj['height'])
		check = isinstance(findBlockNum, (int, long))

		if check == True:
			firstObj['block'] = int(findBlockNum)
			firstObj['time'] = int(firstObj['time'])
			if 'mediantime' in firstObj:
				firstObj['mediantime'] = int(firstObj['mediantime'])
			return json.dumps(firstObj)
		else:
			print "FAIL! Looks like we can't aggregate Block Number!?"
			sys.exit(1)