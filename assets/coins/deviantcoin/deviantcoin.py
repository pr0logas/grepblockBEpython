#:: By GrepBlock.com developers // pr0logas
#:: Modified date: 2019-12-09
#:: Description: This file contains default values of the asset

# Defaults
database = "deviantcoin"
assetTicker="DEV"
assetName = "deviantcoin"
genesisBlock = 1529783629
coinGeckoStartUnixTime = 1522368000
blockTime = 60

# RPC
rpcconnect = "mongoHostIP"
rpcport = 9078
rpcuser = "grepblock"
rpcpassword = "tothemoon"

parseBlocksInRangeFor = 99

chainProvider = 'http://explorer.deviantcoin.io'
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

daemonCli = "deviantcoin-cli"