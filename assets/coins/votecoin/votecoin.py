#:: By GrepBlock.com developers // pr0logas
#:: Modified date: 2019-12-09
#:: Description: This file contains default values of the asset

## Explorer has disabled API

# Defaults
database = "votecoin"
assetTicker = "VOT"
assetName = "votecoin"
genesisBlock = 1475020813
coinGeckoStartUnixTime = 1476057600
blockTime = 300

# RPC
rpcconnect = "10.10.100.201"
rpcport = 8888
rpcuser = "grepblock"
rpcpassword = "tothemoon"

parseBlocksInRangeFor = 99

chainProvider = 'https://explorer.votecoin.site/'
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
daemonCli = "votecoin-cli"