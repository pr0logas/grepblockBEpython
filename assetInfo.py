#:: By GrepBlock.com developers // pr0logas
#:: Modified date: 2019-12-15
#:: Description: This file is a crap. Legacy bash code with python hybrid. Most problematic thing is one line JSON requirement

from mongoDB import *
import json
import subprocess
import random, time
import os

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
    sedCommand1 = "sed -i 's@{@@g'" + './' + str(fullPath)
    sedCommand2 = "sed -i 's@}@@g'" + './' + str(fullPath)
    sedCommand3 = "sed -i '$ d'" + './' + str(fullPath)
    sedCommand4 = "sed -i '1i\{'" + './' + str(fullPath)
    sedCommand5 = "sed -i '\$a\}'" + './' + str(fullPath)
    sedCommand6 = "sed -i '1i\['" + './' + str(fullPath)
    sedCommand7 = "sed -i '\$a\]'" + './' + str(fullPath)
    sedCommand8 = "sed -i '/^[[:space:]]*$/d'" + './' + str(fullPath)

    instancePath = '/usr/share/nginx/grepblockcom/apidata/'
    makeDir = 'ssh root@websiteHostIP "mkdir -p /usr/share/nginx/grepblockcom/apidata/' + str(assetTickerPath) + '/"'
    command = 'scp ./' + str(fullPath) + ' root@websiteHostIP:' + instancePath + str(assetTickerPath) + '/' + str(jsonFile)
    try:
        subprocess.check_output(sedCommand1, shell=True).strip()
        subprocess.check_output(sedCommand2, shell=True).strip()
        subprocess.check_output(sedCommand3, shell=True).strip()
        subprocess.check_output(sedCommand4, shell=True).strip()
        subprocess.check_output(sedCommand5, shell=True).strip()
        subprocess.check_output(sedCommand6, shell=True).strip()
        subprocess.check_output(sedCommand7, shell=True).strip()
        subprocess.check_output(sedCommand8, shell=True).strip()
        subprocess.check_output(makeDir, shell=True).strip()
        time.sleep(random.randint(1, 3))  # Sleep, ssh too many sessions are mean in failure
        subprocess.check_output(command, shell=True).strip()
    except:
        subprocess.check_output(makeDir, shell=True).strip()
        time.sleep(random.randint(1, 3))  # Sleep, ssh too many sessions are mean in failure
        subprocess.check_output(command, shell=True).strip()
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

init = '['
result = (json.dumps(assetName))
res = (init + result)
writeToFile(res)
result = (json.dumps(assetType))
res = (', ' + result + ', ')
writeToFile(res)
result = (json.dumps(assetTicker))
res = (result + ', ')
writeToFile(res)
result = (json.dumps(assetMineable))
res = (result + ', ')
writeToFile(res)
result = (json.dumps(assetMasternode))
res = (result + ', ')
writeToFile(res)
result = (json.dumps(assetSourceCode))
res = (result + ', ')
writeToFile(res)
result = (json.dumps(assetBlockTime))
res = (result + ', ')
writeToFile(res)
result = (json.dumps(assetMaxSupply))
res = (result + ', ')
writeToFile(res)
result = (json.dumps(assetBlockSize))
res = (result + ', ')
writeToFile(res)
result = (json.dumps(assetWalletPrefix))
res = (result + ', ')
writeToFile(res)
result = (json.dumps(assetExplorer))
res = (result + ', ')
writeToFile(res)
result = (json.dumps(assetExplorer2))
res = (result + ', ')
writeToFile(res)
result = (json.dumps(assetExplorer3))
res = (result + ', ')
writeToFile(res)
result = (json.dumps(assetWebsite))
res = (result + ', ')
writeToFile(res)
result = (json.dumps(assetRpcPort))
res = (result + ', ')
writeToFile(res)
result = (json.dumps(assetNetworkPort))
res = (result + ', ')
writeToFile(res)
result = (json.dumps(assetBitcointalkT))
res = (result + ', ')
writeToFile(res)
result = (json.dumps(assetTelegram))
res = (result + ', ')
writeToFile(res)
result = (json.dumps(assetReddit))
res = (result + ', ')
writeToFile(res)
result = (json.dumps(assetTwitter))
res = (result + ', ')
writeToFile(res)
result = (json.dumps(assetDiscord))
res = (result + ', ')
writeToFile(res)
result = (json.dumps(assetAbout))
res = (result + ', ')
writeToFile(res)
result = (json.dumps(assetAlgo))
res = (result + ', ')
writeToFile(res)
result = (json.dumps(assetDevFee))
res = (result + ', ')
writeToFile(res)
result = (json.dumps(assetWhitepaper))
res = (result + ', ')
writeToFile(res)
result = (json.dumps(assetFirstBlock))
res = (result + ']')
writeToFile(res)

copyFileToWebsiteFE()

print('All tasks were successful')