import sys, time
from time import gmtime, strftime
from solaris import *
sys.path.append('../../../')
from mongoDB import *
from explorer import iquidusExplorer
from parseBlocks import aggregateBlocksData

db = database
collectionForBlocks = "blocks"

# Init Classes;
MC = mongoConnection(mongoAuth, db, collectionForBlocks)
EX = iquidusExplorer(chainProvider, getBlockIndexMethod, getBlockwithHashMethod, getTx)
AG = aggregateBlocksData()

# Check if blocks col empty or not?
if MC.checkIfBlocksColEmpty(collectionForBlocks) == "Empty":
	print "Warning! We found an empty blocks collection. Starting from zero."
	MC.insertInitValueForBlocks(collectionForBlocks)

# Set current progress;
currentLastBlock = MC.findLastBlock(collectionForBlocks)

# Check last Explorer block:
currentExplBlock = int(EX.getLastBlockSolarisDirty())
currentExplBlock -= 3

# Set how much blocks we want to sync from current point +- ~99
parsingBlocksInRange = parseBlocksInRangeFor + currentLastBlock

# Check if our progress is near by Explorer blocks?
diff = str(currentExplBlock - currentLastBlock)

# We have two choises here, parse the blocks in range for +- ~100 block (last block too far anyway) or until last Explorer block -2 //
# We don't wanna to parse up to last block, because in case of wrong chain parsing node could rewrite the latest few blocks;

# Start Parsing blocks ::in range:: and push to MongoDB;
if diff >= 100:
	whileprogress = currentLastBlock 

	if whileprogress == 0:
		whileprogress += 1

	while whileprogress < parsingBlocksInRange:
		print "while2", whileprogress
		print "expl2", currentExplBlock
		setProcStart = int(round(time.time() * 1000))
		bH = EX.getBlockHash(str(whileprogress))
		bD = EX.getBlockContentByHash(bH)
		aggregatedBlockData = AG.aggregateInsertBlockNumber(bD)
		status = MC.insertBlocksData(collectionForBlocks, aggregatedBlockData)
		whileprogress += 1

		setProcEnd = int(round(time.time() * 1000))
		performanceResult = str(setProcEnd - setProcStart)
		timeSet = strftime("%Y-%m-%d %H:%M:%S", gmtime())
		if str(status) != 'None':
			print timeSet + " Block finished: " + str(status) + ' // ' + (performanceResult) + ' ms'

# Start Parsing blocks until last Explorer block -2 and push to MongoDB;
else: 
	whileprogress = currentLastBlock 

	if whileprogress == 0:
		whileprogress += 1

	while whileprogress < currentExplBlock:
		print "while", whileprogress
		print "expl", currentExplBlock
		setProcStart = int(round(time.time() * 1000))
		bH = EX.getBlockHash(str(whileprogress))
		bD = EX.getBlockContentByHash(bH)
		aggregatedBlockData = AG.aggregateInsertBlockNumber(correction)
		status = MC.insertBlocksData(collectionForBlocks, aggregatedBlockData)
		whileprogress += 1

		setProcEnd = int(round(time.time() * 1000))
		performanceResult = str(setProcEnd - setProcStart)
		timeSet = strftime("%Y-%m-%d %H:%M:%S", gmtime())
		if str(status) != 'None':
			print timeSet + " Block finished: " + str(status) + ' // ' + (performanceResult) + ' ms'