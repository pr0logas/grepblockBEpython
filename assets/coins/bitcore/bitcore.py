#:: By GrepBlock.com developers // pr0logas
#:: Modified date: 2019-12-05
#:: Description: This file contains default values of the asset

# Defaults
database = "bitcore"
assetTicker = "BTX"
assetName = "bitcore"
genesisBlock = 1492995597
coinGeckoStartUnixTime = 1497484800
blockTime = 150

# RPC
rpcconnect = "mongoHostIP"
rpcport = ''
rpcuser = "grepblock"
rpcpassword = "tothemoon"

parseBlocksInRangeFor = 99

chainProvider = 'https://insight.bitcore.cc/'
getBlockIndexMethod = 'api/block-index/'
getBlockwithHashMethod = 'api/block/'
getTx = 'api/tx/'

apiProvider = 'https://api.coingecko.com'
vsCurrencyUSD = 'usd'
collectionForPricesUSD = 'priceDataUSD'
collectionForHistoricalPricesUSD = 'historicalPriceData'

# Stats related
fileForBlockCount="assetBlocks.json"
fileForActiveWalletsCount="assetActiveWallets.json"
fileForBlockchainSize="assetBlockchainSize.json"
fileForDifficulty="assetDifficulty.json"
fileForTransactions="assetTransactions.json"

# Money related
fileForMarketCap="assetMarketCap.json"
fileForPrice="assetPrice.json"
fileForVolume="assetVolume.json"

#
daemonCli = "bitcore-cli"