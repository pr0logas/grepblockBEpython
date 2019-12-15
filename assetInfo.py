from mongoDB import *
import os, json

asset = 'memetic'
jsonPath = 'assets/coins/' + asset + '/JSON/'
jsonFile = 'assetInfo.json'
fullPath = (jsonPath+jsonFile)
col = 'basicInfo'
initJsonText = '{}'

# Init Mongo
MC = mongoConnection(mongoAuth, asset, col)

# WriteEmpty File
file = open(fullPath, "w")
file.write(str(initJsonText))
file.close()

assetName = (MC.findAssetName(col))
assetType = (MC.findAssetType(col))
assetTicker = (MC.findAssetTicker(col))
print(MC.findAssetMineable(col))
print(MC.findAssetMasternode(col))
print(MC.findAssetSourceCode(col))
print(MC.findAssetBlockTime(col))
print(MC.findAssetMaxSupply(col))
print(MC.findAssetBlockSize(col))
print(MC.findAssetWalletPrefix(col))
print(MC.findAssetExplorer(col))
print(MC.findAssetExplorer2(col))
print(MC.findAssetExplorer3(col))
print(MC.findAssetWebsite(col))
print(MC.findAssetRpcPort(col))
print(MC.findAssetNetworkPort(col))
print(MC.findAssetBitcointalkThread(col))
print(MC.findAssetTelegram(col))
print(MC.findAssetReddit(col))
print(MC.findAssetTwitter(col))
print(MC.findAssetChat(col))
print(MC.findAssetAbout(col))
print(MC.findAssetAlgorithm(col))
print(MC.findAssetDeveloperFee(col))
print(MC.findAssetWhitepaper(col))
print(MC.findAssetFirstBlock(col))


file = open(fullPath, "r")
content = file.read()
cjson = json.loads(content)


cjson = assetName[0]
result = (json.dumps(cjson))
file = open(fullPath, "w")
file.write(str(result))
cjson = assetType[0]
result = (json.dumps(cjson))
file = open(fullPath, "w")
file.write(str(result))












file.close()
