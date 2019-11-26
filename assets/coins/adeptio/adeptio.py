#!/usr/bin/env python

# Defaults
database = "adeptio"
assetTicker="ADE"
assetName = "adeptio"
genesisBlock = 1527710105
coinGeckoStartUnixTime = 1532088000
blockTime = 60

# RPC
rpcconnect = "10.10.100.201"
rpcport = 9078
rpcuser = "grepblock"
rpcpassword = "tothemoon"

parseBlocksInRangeFor=299

chainProvider = 'https://explorer.adeptio.cc'
getBlockIndexMethod = '/api/getblockhash?index='
getBlockwithHashMethod = '/api/getblock?hash='
getTx = '/api/getrawtransaction?txid='

apiProvider = 'api.coingecko.com'

#
daemonCli="adeptio-cli"