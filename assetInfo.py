from mongoDB import *
import os, json

asset = 'memetic'
jsonPath = 'assets/coins/' + asset + '/JSON/'
jsonFile = 'assetInfo.json'
fullPath = (jsonPath+jsonFile)
col = 'basicInfo'
initJsonText = '[]'

# Init Mongo
MC = mongoConnection(mongoAuth, asset, col)

# WriteEmpty File
file = open(fullPath, "w")
file.write(str(initJsonText))
file.close()

assetName = (MC.findAssetName(col))
assetType = (MC.findAssetType(col))
assetTicker = (MC.findAssetTicker(col))
assetMineable = (MC.findAssetMineable(col))
assetMasternode = (MC.findAssetMasternode(col))
assetSourceCode = (MC.findAssetSourceCode(col))
assetBlockTime = (MC.findAssetBlockTime(col))
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


apendedJson = cjson.append(assetName)
result = (json.dumps(apendedJson))
file = open(fullPath, "w")
file.write(str(result))












file.close()
