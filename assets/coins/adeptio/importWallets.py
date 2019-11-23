#!/usr/bin/env python

import sys
from adeptio import *
sys.path.append('../../')
from mongoDB import *
from parseWallets import * 
from performance import perfResult, setTimeCommand, time

collection = "txidsProgress"
setProcStart = setTimeCommand

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

