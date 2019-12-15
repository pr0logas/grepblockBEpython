from mongoDB import mongoConnection
from assets.coins import memetic

MC = mongoConnection(mongoAuth, database, 'basicInfo')


print(MC.findAssetName('basicInfo'))