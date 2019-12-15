from mongoDB import *
import os, json

asset = 'memetic'
jsonPath = 'assets/coins/' + asset + '/'
col = 'basicInfo'
jsonFile = 'assetInfo.json'
initJsonText = '{}'

MC = mongoConnection(mongoAuth, asset, col)

assetName = (MC.findAssetName(col))
print(MC.findAssetType(col))
print(MC.findAssetTicker(col))
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

file = open((jsonPath+jsonFile), "w")
file.write(str(initJsonText))
file.close()

file = open((jsonPath+jsonFile), "r")
content = (file.read())
cjson = json.loads(content)
cjson.append(assetName[0])
print(json.dumps(cjson))