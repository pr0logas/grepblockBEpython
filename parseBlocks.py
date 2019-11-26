import json, fileinput
from explorer import iquidusExplorer
import os

class aggregateBlocksData():
	def __init__(self):
		pass

	def aggregateInsertBlockNumber(self, blockData):
		print blockData
		firstObj = json.loads(blockData)
		print firstObj
		pretty_data = json.dumps(firstObj.json(), indent=4)
		print pretty_data
		originalData = blockData
		firstObj = json.loads(blockData)
		findBlockNum = int(firstObj['height'])
		check = isinstance(findBlockNum, (int, long))

		if check == True:
			append = '{\n  "block" : ' + str(findBlockNum) + ','
			inserted = originalData.replace('{', append)
			return inserted
		else:
			print "FAIL! Looks like we can't aggregate Block Number!?"
			sys.exit(1)