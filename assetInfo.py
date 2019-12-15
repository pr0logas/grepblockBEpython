from mongoDB import *
import json
import subprocess
import random, time

asset = 'memetic'
assetTickerPath = 'MEME'
jsonPath = 'assets/coins/' + asset + '/JSON/'
jsonFile = 'assetInfo.json'
fullPath = (jsonPath+jsonFile)
col = 'basicInfo'

print('Writing to path: ' + str(fullPath))

# Init Mongo
MC = mongoConnection(mongoAuth, asset, col)

def writeToFile(data):
    file = open(fullPath, "a")
    file.write(str(data))
    file.close()

def copyFileToWebsiteFE():
    instancePath = '/usr/share/nginx/grepblockcom/apidata/'
    makeDir = 'ssh root@websiteHostIP "mkdir -p /usr/share/nginx/grepblockcom/apidata/' + str(assetTickerPath) + '/"'
    command = 'scp ./' + str(fullPath) + ' root@websiteHostIP:' + instancePath + str(assetTickerPath) + '/' + str(jsonFile)
    try:
        subprocess.check_output(makeDir, shell=True).strip()
        time.sleep(random.randint(1, 3))  # Sleep, ssh too many sessions are mean in failure
        subprocess.check_output(command, shell=True).strip()
    except:
        print("FATAL! Failed to copy JSON to FE websiteHostIP")
        sys.exit(1)

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
assetExplorer = (MC.findAssetExplorer(col))
assetExplorer2 = (MC.findAssetExplorer2(col))
assetExplorer3 = (MC.findAssetExplorer3(col))
assetWebsite = (MC.findAssetWebsite(col))
assetRpcPort = (MC.findAssetRpcPort(col))
assetNetworkPort = (MC.findAssetNetworkPort(col))
assetBitcointalkT = (MC.findAssetBitcointalkThread(col))
assetTelegram = (MC.findAssetTelegram(col))
assetReddit = (MC.findAssetReddit(col))
assetTwitter = (MC.findAssetTwitter(col))
assetDiscord = (MC.findAssetChat(col))
assetAbout = (MC.findAssetAbout(col))
assetAlgo = (MC.findAssetAlgorithm(col))
assetDevFee = (MC.findAssetDeveloperFee(col))
assetWhitepaper = (MC.findAssetWhitepaper(col))
assetFirstBlock = (MC.findAssetFirstBlock(col))

fullString = ''

init = '['
result = (json.dumps(assetName))
res = (init + result)
fullString.join(res)
result = (json.dumps(assetType))
res = (', ' + result + ', ')
fullString.join(res)
result = (json.dumps(assetTicker))
res = (result + ', ')
fullString.join(res)
result = (json.dumps(assetMineable))
res = (result + ', ')
fullString.join(res)
result = (json.dumps(assetMasternode))
res = (result + ', ')
fullString.join(res)
result = (json.dumps(assetSourceCode))
res = (result + ', ')
fullString.join(res)
result = (json.dumps(assetBlockTime))
res = (result + ', ')
fullString.join(res)
result = (json.dumps(assetMaxSupply))
res = (result + ', ')
fullString.join(res)
result = (json.dumps(assetBlockSize))
res = (result + ', ')
fullString.join(res)
result = (json.dumps(assetWalletPrefix))
res = (result + ', ')
fullString.join(res)
result = (json.dumps(assetExplorer))
res = (result + ', ')
fullString.join(res)
result = (json.dumps(assetExplorer2))
res = (result + ', ')
fullString.join(res)
result = (json.dumps(assetExplorer3))
res = (result + ', ')
fullString.join(res)
result = (json.dumps(assetWebsite))
res = (result + ', ')
fullString.join(res)
result = (json.dumps(assetRpcPort))
res = (result + ', ')
fullString.join(res)
result = (json.dumps(assetNetworkPort))
res = (result + ', ')
fullString.join(res)
result = (json.dumps(assetBitcointalkT))
res = (result + ', ')
fullString.join(res)
result = (json.dumps(assetTelegram))
res = (result + ', ')
fullString.join(res)
result = (json.dumps(assetReddit))
res = (result + ', ')
fullString.join(res)
result = (json.dumps(assetTwitter))
res = (result + ', ')
fullString.join(res)
result = (json.dumps(assetDiscord))
res = (result + ', ')
fullString.join(res)
result = (json.dumps(assetAbout))
res = (result + ', ')
fullString.join(res)
result = (json.dumps(assetAlgo))
res = (result + ', ')
fullString.join(res)
result = (json.dumps(assetDevFee))
res = (result + ', ')
fullString.join(res)
result = (json.dumps(assetWhitepaper))
res = (result + ', ')
fullString.join(res)
result = (json.dumps(assetFirstBlock))
res = (result + ']')
fullString.join(res)

writeToFile(fullString)
copyFileToWebsiteFE()

print('All tasks were successful')