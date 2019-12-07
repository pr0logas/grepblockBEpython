#:: By GrepBlock.com developers // pr0logas
#:: Modified date: 2019-11-30
#:: Description: This file contains default values of the asset

# Defaults
database = "groestlcoin"
assetTicker = "GRS"
assetName = "groestlcoin"
genesisBlock = 1395495671
coinGeckoStartUnixTime = 1397606400
blockTime = 60

# RPC
rpcconnect = "10.10.100.201"
rpcport = 8888
rpcuser = "grepblock"
rpcpassword = "tothemoon"

parseBlocksInRangeFor = 99

chainProvider = 'http://groestlsight.groestlcoin.org/'
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
daemonCli = "groestlcoin-cli"