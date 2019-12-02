#:: By GrepBlock.com developers // pr0logas, mrNemo
#:: Modified date: 2019-11-30
#:: Description: This file contains methods which gives us current prices for the assets.

import urllib2, cookielib, json, time, sys
from time import gmtime, strftime

class parseCoinGeckoPrices():
	def __init__ (self, apiProvider, vsCurrency, assetName):
		self.apiProvider = apiProvider
		self.vsCurrency = vsCurrency
		self.assetName = assetName
		self.u = urllib2
		self.header = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (INFO, GrepBlock.com) Chrome/23.0.1271.64 Safari/537.11',
			   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
			   'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
			   'Accept-Encoding': 'none',
			   'Accept-Language': 'en-US,en;q=0.8',
			   'Connection': 'keep-alive'}

	def parsePrice(self):
		url = (self.apiProvider+ '/api/v3/coins/markets?vs_currency=' + self.vsCurrency + '&ids=' + self.assetName + 
		'&order=market_cap_desc&per_page=100&page=1&sparkline=false')
		req = self.u.Request(url, headers=self.header)
		try:
			page = self.u.urlopen(req)
		except:
			timeSet = strftime("%Y-%m-%d %H:%M:%S", gmtime())
			print timeSet + " PR.Class. FATAL: " + self.apiProvider + " failed to provide data. " + url
			sys.exit(0)

		content = page.read()
		return content

	def aggregateInsertUnixTime(self, priceData):
		firstObj = json.loads(priceData)
		secObj = firstObj[0]
		unixTime = int(time.time())
		secObj['unix_time'] = int(unixTime)

		if secObj['roi'] is None:
			secObj['roi'] = str('null')
		
		if secObj['high_24h'] is None:
			secObj['high_24h'] = str('null')

		if secObj['low_24h'] is None:
			secObj['low_24h'] = str('null')

		if secObj['price_change_percentage_24h'] is None:
			secObj['price_change_percentage_24h'] = int('0')

		if secObj['price_change_24h'] is None:
			secObj['price_change_24h'] = int('0')

		return json.dumps(secObj)
