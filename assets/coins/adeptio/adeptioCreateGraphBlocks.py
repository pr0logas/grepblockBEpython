import sys, time
from time import gmtime, strftime
from adeptio import *
sys.path.append('../../../')
from parseGraphs import parseGraph

# Init Classes;
GR = parseGraph(fileForBlockCount, genesisBlock)

res = GR.parseBlocksFindLastValue()

print res
