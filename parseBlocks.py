#:: By GrepBlock.com developers // pr0logas, mrNemo
#:: Modified date: 2019-11-30
#:: Description: This file contains block aggregation methods.

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

			# Solaris sets a string. Changing to int <
			if 'mediantime' in firstObj:
				firstObj['mediantime'] = int(firstObj['mediantime'])

			if 'isMainChain' in firstObj:
				firstObj['isMainChain'] = str(firstObj['isMainChain'])

			if 'stakemod' in firstObj:
				firstObj['stakemod'] = str(firstObj['stakemod'])

			if 'chainlock' in firstObj:
				firstObj['chainlock'] = str(firstObj['chainlock'])

			# Horizen
			if 'valuePools' in firstObj:
				firstObj['valuePools'] = str("null")

			return json.dumps(firstObj)
		else:
			print "FAIL! Looks like we can't aggregate Block Number!?"
			sys.exit(1)