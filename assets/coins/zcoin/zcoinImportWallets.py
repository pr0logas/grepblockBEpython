import sys, time
from time import gmtime, strftime
from zcoin import *
sys.path.append('../../../')
from mongoDB import *
from rpc import nodeRpcCallerDash
from parseWallets import aggregateWalletsData

collectionTxidProgress = "txidsProgress"
collectionForBlocks = "blocks"
collectionForWallets = "wallets"

# Init Classes;
MC = mongoConnection(mongoAuth, database, collectionTxidProgress)
RPC = nodeRpcCallerDash(daemonCli, rpcconnect, rpcport, rpcuser, rpcpassword)
AG = aggregateWalletsData()

# Check if txidProgress col empty or not?
if MC.checkIfTxidProgressColEmpty(collectionTxidProgress) == "Empty":
	print "Warning! We found an empty txidProgress collection. Starting from zero."
	MC.insertInitValueForWalletsProgress(collectionTxidProgress)

# Set current progress;
currentLastTxidProgress = MC.findLastTxidProgress(collectionTxidProgress)
currentLastBlock = MC.findLastBlock(collectionForBlocks)

# Decrease txidsProgress value in case of previous failure;
if currentLastTxidProgress != 0:
	MC.updateLastTxidProgressMinusOne(collectionTxidProgress, currentLastTxidProgress)
	if int(MC.findLastTxidProgress(collectionTxidProgress)) == int(currentLastTxidProgress):
		print ("FAIL: Unable to decrease lastblock value in txidsProgress!")
		sys.exit(1)
	else:
		print ("OK: txidsProgress value succesfully decreased to:" + ' ' + str(MC.findLastTxidProgress(collectionTxidProgress)))

if currentLastTxidProgress == 0:
	currentLastTxidProgress += 1

# Start Parsing for unique Wallets and push to MongoDB;
whileprogress = currentLastTxidProgress
while whileprogress<currentLastBlock:

	setProcEnd = 0
	status = ''
	setProcStart = int(round(time.time() * 1000))
	blockData = MC.findByBlock(collectionForBlocks, whileprogress)
	blockTime = blockData['time']
	blockNumber = blockData['height']
	for txid in blockData['tx']:
		getTxData = RPC.getTxContentByTxid(txid)
		randomWlts = AG.findAllWalletsAddr(getTxData)
		if randomWlts != []:
			uniqWlts = AG.aggregateOnlyUniqueWallets(randomWlts)
			for uw in uniqWlts:
				createJSON = AG.createJsonForWallet(str(blockNumber), str(blockTime), uw)
				result = MC.upsertUniqueWallets(collectionForWallets, createJSON)
				status = result
				t = int(round(time.time() * 1000))
				setProcEnd = t

	performanceResult = str(setProcEnd - setProcStart)
	timeSet = strftime("%Y-%m-%d %H:%M:%S", gmtime())
	if str(status) != 'None':
		if str(status) != '':
			print timeSet + " Wallet inserted : " + str(status)
		else:
			print timeSet + " Warning! Txid don't have any vout Wallets!"
	
	print timeSet + " Block finished: " + str(blockNumber) + ' // ' + (performanceResult) + ' ms'

	# Increase txidsProgress to move forward;
	MC.updateLastTxidProgressPlusOne(collectionTxidProgress, whileprogress)
	whileprogress += 1