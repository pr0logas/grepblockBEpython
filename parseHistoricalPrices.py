#:: By GrepBlock.com developers // pr0logas, mrNemo
#:: Modified date: 2019-11-30
#:: Description: This file contains methods which gives us historical prices for the assets.

import urllib2, cookielib, json, time, sys
from time import gmtime, strftime
from datetime import datetime

class parseCoinGeckoHistoricalPrices():
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

	def parseHistoricalPrice(self, time):
		formatTime = (datetime.utcfromtimestamp(time).strftime('%d-%m-%Y'))
		url = (self.apiProvider+ '/api/v3/coins/' + self.assetName + '/history?date=' + str(formatTime) + 
		'&localization=false')
		req = self.u.Request(url, headers=self.header)
		try:
			page = self.u.urlopen(req)
		except:
			timeSet = strftime("%Y-%m-%d %H:%M:%S", gmtime())
			print timeSet + " HPR.Class. FATAL: " + self.apiProvider + " failed to provide data. " + url
			sys.exit(1)

		content = page.read()
		return content

	def aggregateInsertUnixTime(self, historicalPriceData, time):
		print historicalPriceData
		firstObj = json.loads(historicalPriceData)
		secObj = firstObj
		secObj['unix_time'] = int(time)

		if 'community_data' in secObj:
			secObj['community_data'] = str("null")

		if '"public_interest_stats"' in secObj:
			secObj['"public_interest_stats"'] = str("null")

		if 'developer_data' in secObj:
			secObj['developer_data'] = str("null")

		print json.dumps(secObj)
		return json.dumps(secObj)