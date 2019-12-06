#:: By GrepBlock.com developers // pr0logas
#:: Modified date: 2019-12-06
#:: Description: This file contains default values of the asset

# Defaults
database = "vidulum"
assetTicker = "VDL"
assetName = "vidulum"
genesisBlock = 1540683347
coinGeckoStartUnixTime = 1542412800
blockTime = 60

# RPC
rpcconnect = "10.10.100.201"
rpcport = ''
rpcuser = "grepblock"
rpcpassword = "tothemoon"

parseBlocksInRangeFor = 99

chainProvider = 'https://exp.vidulum.app/'
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
daemonCli = "vidulum-cli"