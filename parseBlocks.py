#!/usr/bin/env python

from explorer import iquidusExplorer

class aggregateBlocksData(iquidusExplorer):
	def __init__(self):
		super(iquidusExplorer, self).__init__

	def parseBlocks(self, currentBlock, explorerBlock):
		whileprogress = currentBlock
		while whileprogress < explorerBlock:
			pass

	def parseBlocksInRange(self, currentBlock, parseBlocksInRangeValue):
		whileprogress = currentBlock
		while whileprogress < parseBlocksInRangeValue:
			pass

	def appendBlockNumbertoJSON(blockData):
		pass