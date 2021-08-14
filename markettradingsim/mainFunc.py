import re
from markettradingsim.constants import TEXTONLY
import markettradingsim.marketStack as api
import markettradingsim.databaseActions as DB

def inputTicker(entries):
	stockCode = entries['Stock Code'].upper()
	exchange = entries['Exchange'].upper()
	if re.match(TEXTONLY["REGEX"], exchange) and re.match(TEXTONLY["REGEX"], stockCode) and len(exchange + stockCode)!= 0:
		if exchange == 'XNAS':
			ticker = stockCode
		else:
			ticker = stockCode + '.' + exchange
		addTicker(ticker)
	else:
		print(TEXTONLY["ERROR"])

def addTicker(ticker):
	api_response = api.getTicker(ticker, 'eod')
	if api.validateResponse(api_response):
		key = DB.checkProfile(api_response["data"]["symbol"])
		if key == False:
			key = DB.createProfile(api_response["data"])
		DB.insertData(api_response["data"]["eod"], key)

def printExchanges():
	api_response = api.getAncillaryData('exchanges')
	if api.validateResponse(api_response):
		for exchange in api_response["data"]:
			if exchange["name"] != 'INDEX':
				print('Name:' + exchange["name"] + ' | '
					'Acronym:' + exchange["acronym"] + ' | '
					'Code:' + exchange["mic"])