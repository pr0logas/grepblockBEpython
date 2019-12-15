from mongoDB import *
from assets.coins import *

MC = mongoConnection(mongoAuth, database, 'basicInfo')


print(MC.findAssetName('basicInfo'))