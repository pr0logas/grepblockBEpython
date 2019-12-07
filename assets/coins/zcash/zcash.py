#:: By GrepBlock.com developers // pr0logas
#:: Modified date: 2019-12-07
#:: Description: This file contains default values of the asset

# Defaults
database = 'zcash'
assetTicker = 'ZEC'
assetName = 'zcash'
genesisBlock = 1477671596
coinGeckoStartUnixTime = 1477785600
blockTime = 150

# RPC
rpcconnect = '10.10.100.201'
rpcport = 11111
rpcuser = 'grepblockuser'
rpcpassword = 'grepblocktothemoon'

parseBlocksInRangeFor = 99

chainProvider = 'https://zcash.blockexplorer.com/'
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
daemonCli = "zcash-cli"