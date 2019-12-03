#:: By GrepBlock.com developers // pr0logas
#:: Modified date: 2019-11-30
#:: Description: This file contains default values of the asset

# Defaults
database = 'bitcoin-gold'
assetTicker = 'BTG'
assetName = 'bitcoin-gold'
genesisBlock = 1231469665
coinGeckoStartUnixTime = 1510099200
blockTime = 600

# RPC
rpcconnect = '10.10.100.201'
rpcport = 11111
rpcuser = 'grepblock'
rpcpassword = 'tothemoon'

parseBlocksInRangeFor = 99

chainProvider = 'https://btgexplorer.com/'
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
daemonCli = "bitcoingold-cli"
