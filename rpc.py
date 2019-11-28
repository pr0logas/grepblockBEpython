import sys, requests, time, re
import json
import subprocess
from time import gmtime, strftime

__metaclass__ = type
class nodeRpcCaller():
	def __init__(self, daemonCli, IP, port, user, password):
		self.daemonCli = daemonCli
		self.ip = IP
		self.port = port
		self.user = user
		self.password = password
		self.command = self.daemonCli + ' -rpcconnect=' + str(self.ip) + ' -rpcport=' + str(self.port) + ' -rpcuser=' + self.user + ' -rpcpassword=' + self.password

	def getBlockHash(self, blockNum):
		fullcall = self.command + ' getblockhash' + ' ' + str(blockNum)
		try:
		    res = subprocess.check_output(fullcall, shell=True).strip()
		except:
			timeSet = strftime("%Y-%m-%d %H:%M:%S", gmtime())
			print timeSet + " No new Blocks found1. Sleeping..."
			sys.exit(0)

		return res

	def getBlockContentByHash(self, blockHash):
		fullcall = self.command + ' getblock' + ' ' + str(blockHash)
		try:
		    res = subprocess.check_output(fullcall, shell=True).strip()
		except:
			timeSet = strftime("%Y-%m-%d %H:%M:%S", gmtime())
			print timeSet + " No new Blocks found2. Sleeping..."
			sys.exit(0)

		return res

	def getTxContentByTxid(self, txid):
		fullcall = self.command + ' getrawtransaction' + ' ' + str(txid) + ' ' + str(1)
		try:
		    res = subprocess.check_output(fullcall, shell=True).strip()
		except:
			timeSet = strftime("%Y-%m-%d %H:%M:%S", gmtime())
			print timeSet + " No new TXids found1. Sleeping..."
			sys.exit(0)

		return res

	def getLastBlock(self):
		fullcall = self.command + ' getblockcount'
		res = subprocess.check_output(fullcall, shell=True).strip()
		t = any(char.isdigit() for char in res)
		if t == True:
			return res
		else:
			timeSet = strftime("%Y-%m-%d %H:%M:%S", gmtime())
			print timeSet + " Can't get last block?"
			sys.exit(1)


class nodeRpcCallerDash(nodeRpcCaller):
	def __init__ (self, daemonCli, IP, port, user, password):
		nodeRpcCaller.__init__(self, daemonCli, IP, port, user, password)

	def getLastBlock(self):
		fullcall = self.command + ' getinfo'
		res = subprocess.check_output(fullcall, shell=True).strip()
		t = any(char.isdigit() for char in res)
		if t == True:
			firstObj = json.loads(res)
			result = str(firstObj['blocks'])
			return result
		else:
			timeSet = strftime("%Y-%m-%d %H:%M:%S", gmtime())
			print timeSet + " Can't get last block?"
			sys.exit(1)