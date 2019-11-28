import sys, requests, time, re
import json
import subprocess
from time import gmtime, strftime

__metaclass__ = type
class nodeRpcCaller():
	def __init__(self, daemonCli, IP, port, user, password)
	self.daemonCli = daemonCli
	self.ip = IP
	self.port = port
	self.user = user
	self.password = password
	self.command = self.daemonCli + self.ip + self.port + self.user + self.password
	print self.command
