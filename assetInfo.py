from mongoDB import *
from assets.coins.memetic import memetic

col = 'basicInfo'

MC = mongoConnection(mongoAuth, memetic.database, col)

print(MC.findAssetName(col))
print(MC.findAssetType(col))