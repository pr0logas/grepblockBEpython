import json, fileinput
from explorer import iquidusExplorer
import os, pprint
from pprint import pprint

class aggregateBlocksData():
	def __init__(self):
		pass

	def aggregateInsertBlockNumber(self, blockData):
		qq = pprint(blockData.json())
		print qq
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