#:: By GrepBlock.com developers // pr0logas
#:: Modified date: 2019-11-30
#:: Description: This file contains default values of the asset

# Defaults
database = "gobyte"
assetTicker="GBX"
assetName = "gobyte"
genesisBlock = 1510848001
coinGeckoStartUnixTime = 1511654400
blockTime = 150

# RPC
rpcconnect = "mongoHostIP"
rpcport = 9078
rpcuser = "grepblock"
rpcpassword = "tothemoon"

parseBlocksInRangeFor = 99

chainProvider = 'http://explorer.gobyte.network:5001'
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

daemonCli = "gobyte-cli"