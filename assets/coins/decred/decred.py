#:: By GrepBlock.com developers // pr0logas
#:: Modified date: 2019-11-30
#:: Description: This file contains default values of the asset

# Defaults
database = 'decred'
assetTicker = 'DCR'
assetName = 'decred'
genesisBlock = 1454954535
coinGeckoStartUnixTime = 1455062400
blockTime = 300

# RPC
rpcconnect = '10.10.100.201'
rpcport = 11111
rpcuser = 'grepblockuser'
rpcpassword = 'grepblocktothemoon'

parseBlocksInRangeFor = 99

chainProvider = 'https://mainnet.decred.org/'
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
daemonCli = "decred-cli"
