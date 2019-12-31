#:: By GrepBlock.com developers // pr0logas, mrNemo
#:: Modified date: 2019-11-30
#:: Description: This file contains all explorer related methods (getting the raw data) from foreign sources.

import sys, time, re
import urllib2, cookielib, json, requests
import subprocess
import ssl
from time import gmtime, strftime

__metaclass__ = type
class iquidusExplorer():
	def __init__ (self, chainProvider, getBlockIndexMethod, getBlockwithHashMethod, getTx):
		self.chainProvider = chainProvider
		self.getBlockIndexMethod = getBlockIndexMethod
		self.getBlockwithHashMethod = getBlockwithHashMethod
		self.getTx = getTx
		self.u = urllib2
		self.timeout = 15
		self.context = ssl._create_unverified_context() # Bypass old CERT validation 2.7 Python deprecated, no support
		self.header = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (INFO, GrepBlock.com) Chrome/23.0.1271.64 Safari/537.11',
			   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
			   'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
			   'Accept-Encoding': 'none',
			   'Accept-Language': 'en-US,en;q=0.8',
			   'Connection': 'keep-alive'}

	def getBlockHash(self, blockNum):
		url = (self.chainProvider+self.getBlockIndexMethod+blockNum)
		req = self.u.Request(url, headers=self.header)
		try:
			page = self.u.urlopen(req, timeout = self.timeout, context=self.context)
		except:
			print(url)
			timeSet = strftime("%Y-%m-%d %H:%M:%S", gmtime())
			print(timeSet + " No new Blocks found. Exit code: 1 Sleeping...")
			sys.exit(0)

		content = page.read()
		return content

	def getBlockContentByHash(self, blockHash):
		url = (self.chainProvider+self.getBlockwithHashMethod+blockHash)
		req = self.u.Request(url, headers=self.header)
		try:
			page = self.u.urlopen(req, timeout = self.timeout, context=self.context)
		except:
			print(url)
			timeSet = strftime("%Y-%m-%d %H:%M:%S", gmtime())
			print(timeSet + " No new Blocks found. Exit code: 2 Sleeping...")
			sys.exit(0)

		content = page.read()
		return content

	def getTxContentByTxid(self, txid):
		url = (self.chainProvider+self.getTx+txid+'&decrypt=1')
		req = self.u.Request(url, headers=self.header)
		try:
			page = self.u.urlopen(req, timeout = self.timeout, context=self.context)
		except:
			print(url)
			timeSet = strftime("%Y-%m-%d %H:%M:%S", gmtime())
			print(timeSet + " No new TXids found. Exit code: 3 Sleeping...")
			sys.exit(0)

		content = page.read()
		return content

	def getLastBlock(self):
		url = (self.chainProvider+'/api/getblockcount')
		req = self.u.Request(url, headers=self.header)
		try:
			page = self.u.urlopen(req, timeout = self.timeout, context=self.context)
		except:
			print(url)
			timeSet = strftime("%Y-%m-%d %H:%M:%S", gmtime())
			print (timeSet + " Can't get last block? Exit code: 4")
			sys.exit(1)

		content = page.read()
		return content

	def getLastBlockSolarisDirty(self):
		result = subprocess.check_output("curl -s https://explorer.solarisplatform.com | grep 'row rows' | head -1 | grep -o '[0-9]*'", shell=True).strip()
		t = any(char.isdigit() for char in result)
		if t == True:
			return result
		else:
			timeSet = strftime("%Y-%m-%d %H:%M:%S", gmtime())
			print (timeSet + " Can't get last block? Exit code: 5")
			sys.exit(1)

	def getLastBlockAmsterdamCoinDirty(self):
		result = subprocess.check_output("curl -s https://www.amsterdamblockchain.info/ | grep 'row rows' | head -1 | grep -o '[0-9]*'", shell=True).strip()
		t = any(char.isdigit() for char in result)
		if t == True:
			return result
		else:
			timeSet = strftime("%Y-%m-%d %H:%M:%S", gmtime())
			print (timeSet + " Can't get last block? Exit code: 6")
			sys.exit(1)


class insightExplorer(iquidusExplorer):
	def __init__ (self, chainProvider, getBlockIndexMethod, getBlockwithHashMethod, getTx):
		iquidusExplorer.__init__(self, chainProvider, getBlockIndexMethod, getBlockwithHashMethod, getTx)

	def getBlockHash(self, blockNum):
		url = (self.chainProvider+self.getBlockIndexMethod+blockNum)
		req = self.u.Request(url, headers=self.header)
		try:
			page = self.u.urlopen(req, timeout = self.timeout, context=self.context)
		except:
			timeSet = strftime("%Y-%m-%d %H:%M:%S", gmtime())
			print(timeSet + " No new Blocks found. Exit code: 6 Sleeping...")
			sys.exit(0)

		content = page.read()
		firstObj = json.loads(content)
		findBlockHash = str(firstObj['blockHash'])
		return findBlockHash

	def getTxContentByTxid(self, txid):
		url = (self.chainProvider+self.getTx+txid)
		req = self.u.Request(url, headers=self.header)
		try:
			page = self.u.urlopen(req, timeout = self.timeout, context=self.context)
		except:
			print(url)
			timeSet = strftime("%Y-%m-%d %H:%M:%S", gmtime())
			print(timeSet + " No new TXids found. Exit code: 7 Sleeping...")
			sys.exit(0)

		content = page.read()
		return content

	def getLastBlock(self):
		url = (self.chainProvider+'api/status?q=getInfo')
		req = self.u.Request(url, headers=self.header)
		try:
			page = self.u.urlopen(req, timeout = self.timeout, context=self.context)
		except:
			print(url)
			timeSet = strftime("%Y-%m-%d %H:%M:%S", gmtime())
			print(timeSet + " Can't get last block? Exit code: 8")
			sys.exit(1)

		content = page.read()
		firstObj = json.loads(content)
		findBlockNum = int(firstObj['info']['blocks'])
		return findBlockNum

	def getLastBlockAlternative(self):
		url = (self.chainProvider+'api/status?q=getLastBlockHash')
		req = self.u.Request(url, headers=self.header)
		try:
			page = self.u.urlopen(req, timeout = self.timeout, context=self.context)
		except:
			print(url)
			timeSet = strftime("%Y-%m-%d %H:%M:%S", gmtime())
			print(timeSet + " Can't get last block Alternative? Exit code: 9")
			sys.exit(1)

		content = page.read()
		firstObj = json.loads(content)
		generatedHash = str(firstObj['lastblockhash'])

		url2 = (self.chainProvider+self.getBlockwithHashMethod+generatedHash)
		req2 = self.u.Request(url2, headers=self.header)

		try:
			page2 = self.u.urlopen(req2, timeout = self.timeout, context=self.context)
		except:
			print(url2)
			timeSet = strftime("%Y-%m-%d %H:%M:%S", gmtime())
			print(timeSet + " Can't get last block Alternative? Exit code: 10")
			sys.exit(1)

		content2 = page2.read()
		secObj = json.loads(content2)
		return int(secObj['height'])

	def getLastBlockDecredOnly(self):
		url = (self.chainProvider+'api/status?q=getInfo')
		req = self.u.Request(url, headers=self.header)
		try:
			page = self.u.urlopen(req, timeout = self.timeout, context=self.context)
		except:
			print(url)
			timeSet = strftime("%Y-%m-%d %H:%M:%S", gmtime())
			print(timeSet + " Can't get last block? Exit code: 8")
			sys.exit(1)

		content = page.read()
		firstObj = json.loads(content)
		findBlockNum = int(firstObj['blocks'])
		return int(findBlockNum)

class ethereumHTTPnode():
	def __self__(self, chainProvider):
		self.chainProvider = chainProvider
		self.r = requests

	def getBlockContentByBlockNum(self, blockNum):
		hexBlockNum = hex(int(blockNum))
		# Here goes the post data to ETH node with HEX params. Boolean is for full tx data or not. //
		postData = {"jsonrpc":"2.0","method":"eth_getBlockByNumber","params":[hexBlockNum, False],"id":1}
		response = r.post(self.chainProvider, json=postData)
		print(response.content)

	def getLastBlock(self):
		# Here goes the post data to ETH node with HEX params. Boolean is for full tx data or not. //
		postData = {"jsonrpc": "2.0", "method": "eth_blockNumber", "params": [], "id": 1}
		response = r.post(self.chainProvider, json=postData)
		content = response.content.read()
		firstObj = json.loads(content)
		findBlockNum = int(firstObj['result'])
		print(findBlockNum)
