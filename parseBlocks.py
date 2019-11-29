import json, fileinput
from explorer import iquidusExplorer
import os

class aggregateBlocksData():
	def __init__(self):
		pass

	def aggregateInsertBlockNumber(self, blockData):
		originalData = blockData
		firstObj = json.loads(blockData)
		findBlockNum = int(firstObj['height'])
		check = isinstance(findBlockNum, (int, long))

		if check == True:
			firstObj['block'] = int(findBlockNum)
			firstObj['time'] = int(firstObj['time'])
			firstObj['nextblockhash'] = str("null")

			if 'mediantime' in firstObj:
				firstObj['mediantime'] = int(firstObj['mediantime'])

			if 'isMainChain' in firstObj:
				firstObj['isMainChain'] = str(firstObj['isMainChain'])

			if 'stakemod' in firstObj:
				firstObj['stakemod'] = str(firstObj['stakemod'])

			if 'chainlock' in firstObj:
				firstObj['chainlock'] = str(firstObj['chainlock'])
				
			# Horizen
			if 'monitored' in firstObj['valuePools']:
				firstObj['valuePools']['monitored'] = str(firstObj['valuePools']['monitored'])

			return json.dumps(firstObj)
		else:
			print "FAIL! Looks like we can't aggregate Block Number!?"
			sys.exit(1)