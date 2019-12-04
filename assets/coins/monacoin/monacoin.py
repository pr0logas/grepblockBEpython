#:: By GrepBlock.com developers // pr0logas
#:: Modified date: 2019-11-30
#:: Description: This file contains default values of the asset

# Defaults
database = 'monacoin'
assetTicker = 'MONA'
assetName = 'monacoin'
genesisBlock = 1388534484
coinGeckoStartUnixTime = 1395273600
blockTime = 90

# RPC
rpcconnect = '10.10.100.201'
rpcport = 11111
rpcuser = 'grepblockuser'
rpcpassword = 'grepblocktothemoon'

parseBlocksInRangeFor = 99

chainProvider = 'https://mona.chainsight.info/'
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
daemonCli = "monacoin-cli"
