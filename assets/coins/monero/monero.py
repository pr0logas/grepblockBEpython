#:: By GrepBlock.com developers // pr0logas
#:: Modified date: 2019-11-30
#:: Description: This file contains default values of the asset

# Defaults
database = "monero"
assetTicker="XMR"
assetName = "monero"
genesisBlock = 1527710105
coinGeckoStartUnixTime = 1532088000
blockTime = 60

# RPC
rpcconnect = "mongoHostIP"
rpcport = 9078
rpcuser = "grepblock"
rpcpassword = "tothemoon"

parseBlocksInRangeFor = 99


#https://moneroblocks.info/api/get_stats
#https://moneroblocks.info/api/get_block_header/1000000
#https://moneroblocks.info/api/get_block_data/100023
#https://moneroblocks.info/api/get_transaction_data/c88ce9783b4f11190d7b9c17a69c1c52200f9faaee8e98dd07e6811175177139
chainProvider = 'https://explorer.monero.cc'
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

daemonCli = "monero-cli"