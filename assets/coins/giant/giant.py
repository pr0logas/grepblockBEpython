#:: By GrepBlock.com developers // pr0logas
#:: Modified date: 2019-11-30
#:: Description: This file contains default values of the asset

# Defaults
database = "giantpay"
assetTicker="ADE"
assetName = "giantpay"
genesisBlock = 1525748357
coinGeckoStartUnixTime = 1532088000
blockTime = 60

# RPC
rpcconnect = "10.10.100.201"
rpcport = 9078
rpcuser = "grepblock"
rpcpassword = "tothemoon"

parseBlocksInRangeFor = 99

chainProvider = 'https://explorer.adeptio.cc'
getBlockIndexMethod = '/api/getblockhash?index='
getBlockwithHashMethod = '/api/getblock?hash='
getTx = '/api/getrawtransaction?txid='

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

daemonCli = "giantpay-cli"