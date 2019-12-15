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
'''
file = open(fullPath, "w")
file.write(str(initJsonText))
file.close()
'''

def writeToFile(data):
    file = open(fullPath, "a")
    file.write(str(data))
    file.close()


assetName = (MC.findAssetName(col))
assetType = (MC.findAssetType(col))
assetTicker = (MC.findAssetTicker(col))
assetMineable = (MC.findAssetMineable(col))
assetMasternode = (MC.findAssetMasternode(col))
assetSourceCode = (MC.findAssetSourceCode(col))
assetBlockTime = (MC.findAssetBlockTime(col))
assetMaxSupply = (MC.findAssetMaxSupply(col))
assetBlockSize = (MC.findAssetBlockSize(col))
assetWalletPrefix = (MC.findAssetWalletPrefix(col))
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

init = '['
result = (json.dumps(assetName))
res = (init + result)
writeToFile(res)
result = (json.dumps(assetType))
res = (', ' + result + ', ')
writeToFile(res)
result = (json.dumps(assetTicker))
res = (', ' + result + ', ')
writeToFile(res)
result = (json.dumps(assetMineable))
res = (', ' + result + ', ')
writeToFile(res)
result = (json.dumps(assetMasternode))
res = (', ' + result + ', ')
writeToFile(res)
result = (json.dumps(assetSourceCode))
res = (', ' + result + ', ')
writeToFile(res)
result = (json.dumps(assetBlockTime))
res = (', ' + result + ', ')
writeToFile(res)
result = (json.dumps(assetMaxSupply))
res = (', ' + result + ', ')
writeToFile(res)
result = (json.dumps(assetBlockSize))
res = (', ' + result + ', ')
writeToFile(res)
result = (json.dumps(assetWalletPrefix))
res = (', ' + result + ', ')
writeToFile(res)


