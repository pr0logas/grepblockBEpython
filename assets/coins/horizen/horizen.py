#:: By GrepBlock.com developers // pr0logas
#:: Modified date: 2019-11-30
#:: Description: This file contains default values of the asset

# Defaults
database = "horizen"
assetTicker = "ZEN"
assetName = "horizen"
genesisBlock = 1478414242
coinGeckoStartUnixTime = 1500076800
blockTime = 150

# RPC
rpcconnect = "10.10.100.28"
rpcport = 18231
rpcuser = "grepblockuser"
rpcpassword = "grepblocktothemoon"

parseBlocksInRangeFor = 99

chainProvider = 'https://explorer.horizen.cc'
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
daemonCli = "zen-cli"