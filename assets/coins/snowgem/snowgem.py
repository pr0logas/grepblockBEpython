#:: By GrepBlock.com developers // pr0logas
#:: Modified date: 2019-11-30
#:: Description: This file contains default values of the asset

# Defaults
database = 'snowgem'
assetTicker = 'XSG'
assetName = 'snowgem'
genesisBlock = 1514034481
coinGeckoStartUnixTime = 1522540800
blockTime = 120

# RPC
rpcconnect = '10.10.100.201'
rpcport = 16112
rpcuser = 'grepblock'
rpcpassword = 'tothemoon'

parseBlocksInRangeFor = 99

chainProvider = 'https://explorer.snowgem.org/'
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
daemonCli = "snowgem-cli"