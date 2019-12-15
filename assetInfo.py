from mongoDB import *
from assets.coins.memetic import memetic

col = 'basicInfo'

MC = mongoConnection(mongoAuth, memetic.database, col)

print(col)
print(MC.findAssetName(col))