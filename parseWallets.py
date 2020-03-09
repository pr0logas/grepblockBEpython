#:: By GrepBlock.com developers // pr0logas, mrNemo
#:: Modified date: 2020-01-01
#:: Description: This file contains wallets aggregation methods.

from explorer import *

class aggregateWalletsData():
	def __init__(self):
		pass

	def findAllWalletsAddr(self, data):
		firstObj = json.loads(data)
		nestedData = firstObj['vout']
		resultList = []
		for i in nestedData:
			try:
				for y in i['scriptPubKey']['addresses']:
					resultList.append(y)
			except KeyError:
				continue

			return resultList

	def findAllPlatformsWalletsAddr(self, data):
		firstObj = json.loads(data)
		fromAddr  = firstObj['from']
		toAddr = firstObj['to']
		resultList = []
		if fromAddr != None:
			resultList.append(fromAddr)

		if toAddr != None:
			resultList.append(toAddr)

		return(resultList)

	def aggregateOnlyUniqueWallets(self, wallets):
		output = set()
		for x in wallets:
			output.add(x)
		return output

	def aggregateOnlyUniqueWalletsFaster(self, wallets):
		return list(set(wallets))

	# Works only data from Explorer
	def aggregateOnlyTxidHashes(self, blockData):
		firstObj = json.loads(blockData)
		nestedData = firstObj['tx']
		resultList = []
		for i in nestedData:
			resultList.append(i)

			return resultList

	def createJsonForWallet(self, blockNum, blockTime, wallet):
		json = '{ "block" : ' + blockNum + ', "walletTime" : ' + blockTime + ', "wallet" : ' + '"'+wallet+'"' + '}'
		return json

	def setBlockTime(self, blockData):
		firstObj = json.loads(blockData)
		time = firstObj['time']
		return time

	def setBlockTimeByMedianTime(self, blockData):
		firstObj = json.loads(blockData)
		time = firstObj['mediantime']
		return time

	def setBlockNumber(self, blockData):
		firstObj = json.loads(blockData)
		blockNumber = firstObj['height']
		return blockNumber
