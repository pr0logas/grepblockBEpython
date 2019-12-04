#:: By GrepBlock.com developers // pr0logas
#:: Modified date: 2019-12-04
#:: Description: This file contains default values of the asset

# Defaults
database = "dash"
assetTicker = "DASH"
assetName = "dash"
genesisBlock = 1390103681
coinGeckoStartUnixTime = 1394928000
blockTime = 150

# RPC
rpcconnect = "10.10.100.201"
rpcport = 9998
rpcuser = "grepblock"
rpcpassword = "tothemoon"

parseBlocksInRangeFor = 99

chainProvider = ''
getBlockIndexMethod = ''
getBlockwithHashMethod = ''
getTx = ''

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
daemonCli = "dash-cli"