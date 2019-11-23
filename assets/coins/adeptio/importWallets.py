#!/usr/bin/env python

import sys
from adeptio import *
sys.path.append('../../')
from mongoDB import *
from parseWallets import * 
from performance import perfResult, setTimeCommand, time
from iquidusExplorer import *

collection = "txidsProgress"
setProcStart = setTimeCommand

# Init Explorer JSON data
ED = iquidusExplorer()
print ED.getBlockHash('5')
print ED.getBlockContentByHash('00000ffa49117a1763cbd558eab797dd6f046acf3d058f4ce1ee1ab53e926191')

# Init MongoConnection
MC = mongoConnection(mongoAuth, database, collection)
currentLastTxidProgress = MC.findLastTxidProgress()

# Decrease txidsProgress value in case of previuos failure;
MC.updateLastTxidProgress(currentLastTxidProgress)

if int(MC.findLastTxidProgress()) == int(currentLastTxidProgress):
	print ("FAIL: Unable to decrease lastblock value in txidsProgress!")
	sys.exit(1)
else:
	print ("OK: txidsProgress value succesfully decreased.")

