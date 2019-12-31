#:: By GrepBlock.com developers // pr0logas, mrNemo
#:: Modified date: 2019-12-31
#:: Description: This file contains block aggregation methods.

import json

class aggregateBlocksData():
	def __init__(self):
		pass

	def aggregateInsertBlockNumber(self, blockData):
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

			# Html coin
			if 'minedBy' in firstObj:
				firstObj['minedBy'] = str(firstObj['minedBy'])

			return json.dumps(firstObj)
		else:
			print "FAIL! Looks like we can't aggregate Block Number!?"
			sys.exit(1)

class aggregatePlatformBlocksData():
	def __init__(self):
		pass

	def aggregatePlatformData(self, blockData):
		firstObj = json.loads(blockData)
		findBlockNum = int(firstObj['number'])
		check = isinstance(findBlockNum, (hex, long))

		if check == True:
			# ETH hex to string conversion
			if 'difficulty' in firstObj:
				firstObj['difficulty'] = int(firstObj['mediantime'][0], 16)
			if 'gasLimit' in firstObj:
				firstObj['gasLimit'] = int(firstObj['gasLimit'][0], 16)
			if 'gasUsed' in firstObj:
				firstObj['gasUsed'] = int(firstObj['gasUsed'][0], 16)
			if 'nonce' in firstObj:
				firstObj['nonce'] = int(firstObj['nonce'][0], 16)
			if 'number' in firstObj:
				firstObj['number'] = int(firstObj['number'][0], 16)
			if 'size' in firstObj:
				firstObj['size'] = int(firstObj['size'][0], 16)
			if 'timestamp' in firstObj:
				firstObj['timestamp'] = int(firstObj['timestamp'][0], 16)
			if 'totalDifficulty' in firstObj:
				firstObj['totalDifficulty'] = int(firstObj['totalDifficulty'][0], 16)

			# Too long to store, no real value to keep
			firstObj['logsBloom'] = str("null")

			firstObj['block'] = int(firstObj['number'])
			firstObj['time'] = int(firstObj['timestamp'])

			return json.dumps(firstObj)
		else:
			print("FAIL! Looks like we can't aggregate platform block data from HEX to decimal?")
			sys.exit(1)