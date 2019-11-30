#:: By GrepBlock.com developers // pr0logas
#:: Modified date: 2019-11-30
#:: Description: This file contains default values of the asset

# Defaults
database = "syscoin"
assetTicker="SYS"
assetName = "syscoin"
genesisBlock = 1559677606
coinGeckoStartUnixTime = 1412121600
blockTime = 60

# RPC
rpcconnect = "10.10.100.201"
rpcport = 8370
rpcuser = "grepblock"
rpcpassword = "tothemoon"

parseBlocksInRangeFor = 99

chainProvider = 'https://explorer.blockchainfoundry.co'
getBlockIndexMethod = '/api/getblockhash?index='
getBlockwithHashMethod = '/api/getblock?hash='
getTx = '/api/getrawtransaction?txid='

apiProvider = 'api.coingecko.com'

#
daemonCli = "syscoin-cli"