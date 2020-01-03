#:: By GrepBlock.com developers // pr0logas
#:: Modified date: 2019-12-04
#:: Description: This file contains default values of the asset

# Defaults
database = 'bitcoin-sv'
assetTicker = 'BSV'
assetName = 'bitcoin-sv'
genesisBlock = 1231469665
coinGeckoStartUnixTime = 1501718400
blockTime = 600

# RPC
rpcconnect = '10.10.100.201'
rpcport = 18332
rpcuser = 'grepblockuser'
rpcpassword = 'grepblocktothemoon'

parseBlocksInRangeFor = 99

chainProvider = 'https://bchsvexplorer.com/'
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
daemonCli = "bitcoinsv-cli"
