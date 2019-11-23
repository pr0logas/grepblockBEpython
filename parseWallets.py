#!/usr/bin/env python

from mongoDB import mongoAuth, mongoConnection
from performance import perfResult

database = "adeptio"
collection = "txidsProgress"

#MC = mongoConnection(mongoAuth, database, collection)
#print MC.findByBlock(2);
#print MC.findByTx('49f40027e05960fe15f58874926331b170a9af1ff8ccee28ee0c9161ae8c9f88');
#print MC.findLastBlock()
#print MC.findLastTxidProgress()

