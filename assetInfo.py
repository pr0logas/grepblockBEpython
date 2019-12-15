from mongoDB import mongoConnection
from assets.coins.memetic.memetic import memetic

MC = mongoConnection(mongoAuth, database, 'basicInfo')


print(MC.findAssetName('basicInfo'))