from mongoDB import *
from assets.coins.memetic import memetic

col = 'basicInfo''

MC = mongoConnection(mongoAuth, database, col)


print(MC.findAssetName(col))