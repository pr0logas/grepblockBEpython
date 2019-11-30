#:: By GrepBlock.com developers // pr0logas
#:: Modified date: 2019-11-30
#:: Description: This file contains default values of the asset

#!/usr/bin/env python

# Defaults
database = 'solaris'
assetTicker = 'XLR'
assetName = 'solaris'
genesisBlock = 1572355036
coinGeckoStartUnixTime = 1512864000
blockTime = 60

# RPC
rpcconnect = '10.10.100.201'
rpcport = 1111
rpcuser = 'grepblock'
rpcpassword = 'tothemoon'

parseBlocksInRangeFor = 99

chainProvider = 'https://explorer.solarisplatform.com'
getBlockIndexMethod = '/api/getblockhash?index='
getBlockwithHashMethod = '/api/getblock?hash='
getTx = '/api/getrawtransaction?txid='

apiProvider = 'api.coingecko.com'

#
daemonCli = "solaris-cli"