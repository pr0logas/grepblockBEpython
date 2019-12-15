from mongoDB import *
from assets.coins import *

db = database

MC = mongoConnection(mongoAuth, db, 'basicInfo')


print(MC.findAssetName('basicInfo'))