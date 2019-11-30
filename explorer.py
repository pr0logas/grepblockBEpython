#:: By GrepBlock.com developers // pr0logas, mrNemo
#:: Modified date: 2019-11-30
#:: Description: This file contains all explorer related methods (getting the raw data) from foreign sources.

import sys, time, re
import urllib2, cookielib, json
import subprocess
from time import gmtime, strftime

__metaclass__ = type
class iquidusExplorer():
	def __init__ (self, chainProvider, getBlockIndexMethod, getBlockwithHashMethod, getTx):
		self.chainProvider = chainProvider
		self.getBlockIndexMethod = getBlockIndexMethod
		self.getBlockwithHashMethod = getBlockwithHashMethod
		self.getTx = getTx
		self.u = urllib2
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
		    page = self.u.urlopen(req)
		except:
			timeSet = strftime("%Y-%m-%d %H:%M:%S", gmtime())
			print timeSet + " EX.Class. No new Blocks found1. Sleeping..."
			sys.exit(0)

		content = page.read()
		return content

	def getBlockContentByHash(self, blockHash):
		url = (self.chainProvider+self.getBlockwithHashMethod+blockHash)
		req = self.u.Request(url, headers=self.header)
		try:
		    page = self.u.urlopen(req)
		except:
			timeSet = strftime("%Y-%m-%d %H:%M:%S", gmtime())
			print timeSet + " EX.Class. No new Blocks found2. Sleeping..."
			sys.exit(0)

		content = page.read()
		return content

	def getTxContentByTxid(self, txid):
		url = (self.chainProvider+self.getTx+txid+'&decrypt=1')
		req = self.u.Request(url, headers=self.header)
		try:
		    page = self.u.urlopen(req)
		except:
			timeSet = strftime("%Y-%m-%d %H:%M:%S", gmtime())
			print timeSet + " EX.Class. No new TXids found1. Sleeping..."
			sys.exit(0)

		content = page.read()
		print content
		return content

	def getLastBlock(self):
		url = (self.chainProvider+'/api/getblockcount')
		req = self.u.Request(url, headers=self.header)
		try:
		    page = self.u.urlopen(req)
		except:
			timeSet = strftime("%Y-%m-%d %H:%M:%S", gmtime())
			print timeSet + " EX.Class. Can't get last block?"
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
			print timeSet + " EX.Class. Can't get last block?"
			sys.exit(1)


class insightExplorer(iquidusExplorer):
	def __init__ (self, chainProvider, getBlockIndexMethod, getBlockwithHashMethod, getTx):
		iquidusExplorer.__init__(self, chainProvider, getBlockIndexMethod, getBlockwithHashMethod, getTx)

	def getBlockHash(self, blockNum):
		url = (self.chainProvider+self.getBlockIndexMethod+blockNum)
		req = self.u.Request(url, headers=self.header)
		try:
		    page = self.u.urlopen(req)
		except:
			timeSet = strftime("%Y-%m-%d %H:%M:%S", gmtime())
			print timeSet + " EX.Class. No new Blocks found1. Sleeping..."
			sys.exit(0)

		content = page.read()
		firstObj = json.loads(content)
		findBlockHash = str(firstObj['blockHash'])
		return findBlockHash

	def getTxContentByTxid(self, txid):
		url = (self.chainProvider+self.getTx+txid)
		req = self.u.Request(url, headers=self.header)
		try:
		    page = self.u.urlopen(req)
		except:
			timeSet = strftime("%Y-%m-%d %H:%M:%S", gmtime())
			print timeSet + " EX.Class. No new TXids found1. Sleeping..."
			sys.exit(0)

		content = page.read()
		return content

	def getLastBlock(self):
		url = (self.chainProvider+'api/status?q=getInfo')
		req = self.u.Request(url, headers=self.header)
		try:
		    page = self.u.urlopen(req)
		except:
			timeSet = strftime("%Y-%m-%d %H:%M:%S", gmtime())
			print timeSet + " EX.Class. Can't get last block?"
			sys.exit(1)

		content = page.read()
		firstObj = json.loads(content)
		findBlockNum = int(firstObj['info']['blocks'])
		return findBlockNum

	def getLastBlockAlternative(self):
		url = (self.chainProvider+'api/status?q=getLastBlockHash')
		req = self.u.Request(url, headers=self.header)
		try:
		    page = self.u.urlopen(req)
		except:
			timeSet = strftime("%Y-%m-%d %H:%M:%S", gmtime())
			print timeSet + " EX.Class. Can't get last block Alternative?"
			sys.exit(1)

		content = page.read()
		firstObj = json.loads(content)
		h = str(firstObj['lastblockhash'])

		s = (self.chainProvider+self.getBlockwithHashMethod+h)
		r = self.u.Request(s, headers=self.header)
		try:
		    page = self.u.urlopen(r)
		except:
			timeSet = strftime("%Y-%m-%d %H:%M:%S", gmtime())
			print timeSet + " EX.Class. Can't get last block Alternative 2?"
			sys.exit(0)

		content = page.read()
		sObj = json.loads(content)
		res = int(sObj['height'])
		return res