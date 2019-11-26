import json, fileinput
from explorer import iquidusExplorer
import os

class aggregateBlocksData():
	def __init__(self):
		pass

	def aggregateInsertBlockNumber(self, blockData):
		originalData = blockData
		print originalData
		firstObj = json.loads(blockData)
		findBlockNum = int(firstObj['height'])
		check = isinstance(findBlockNum, (int, long))

		if check == True:
			append = '{\n  "block" : ' + str(findBlockNum) + ','
			print append
			inserted = originalData.replace('{', append)
			print inserted
			return inserted
		else:
			print "FAIL! Looks like we can't aggregate Block Number!?"
			sys.exit(1)