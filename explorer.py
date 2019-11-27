import sys, requests, time, re
import urllib2, cookielib, json
import subprocess
from time import gmtime, strftime

class iquidusExplorer():
	def __init__ (self, chainProvider, getBlockIndexMethod, getBlockwithHashMethod, getTx):
		self.chainProvider = chainProvider
		self.getBlockIndexMethod = getBlockIndexMethod
		self.getBlockwithHashMethod = getBlockwithHashMethod
		self.getTx = getTx
		self.r = requests
		self.u = urllib2
		self.header = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, GrepBlock.com) Chrome/23.0.1271.64 Safari/537.11',
		       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
		       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
		       'Accept-Encoding': 'none',
		       'Accept-Language': 'en-US,en;q=0.8',
		       'Connection': 'keep-alive'}

	def getBlockHash(self, blockNum):
		try:
		    result = list(self.r.get(self.chainProvider+self.getBlockIndexMethod+blockNum))
		    return result[0]
		except:
			timeSet = strftime("%Y-%m-%d %H:%M:%S", gmtime())
			print timeSet + " No new Blocks found. Sleeping..."
			sys.exit(0)		

	def getBlockContentByHash(self, blockHash):
		url = (self.chainProvider+self.getBlockwithHashMethod+blockHash)
		req = self.u.Request(url, headers=self.header)
		try:
		    page = self.u.urlopen(req)
		except:
			timeSet = strftime("%Y-%m-%d %H:%M:%S", gmtime())
			print timeSet + " No new Blocks found. Sleeping..."
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
			print timeSet + " No new TXids found. Sleeping..."
			sys.exit(0)

		content = page.read()
		return content

	def getLastBlock(self):
		url = (self.chainProvider+'/api/getblockcount')
		req = self.u.Request(url, headers=self.header)
		try:
		    page = self.u.urlopen(req)
		except:
			timeSet = strftime("%Y-%m-%d %H:%M:%S", gmtime())
			print timeSet + " Can't get last block?"
			sys.exit(1)

		content = page.read()
		return content

	def getLastBlockSolarisDirty(self):
		result = subprocess.check_output("curl -s https://explorer.solarisplatform.com | grep 'row rows' | head -1 | grep -o '[0-9]*'", shell=True).strip()
		try:
			test = result
    		test += 1
    		return result
		except TypeError:
			timeSet = strftime("%Y-%m-%d %H:%M:%S", gmtime())
			print timeSet + " Can't get last block?"
			sys.exit(1)