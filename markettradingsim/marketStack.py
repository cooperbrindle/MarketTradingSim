import requests
import markettradingsim.config as config
import markettradingsim.constants as constants

def getEOD(symbol):
	api_response = requests.get(constants.BASE_URL + '/eod', params = {
		'access_key': config.API_ACCESSKEY,
		'symbols': symbol
	})
	return api_response.json()

def getTicker(symbol, func):
	api_response = requests.get(constants.BASE_URL + '/tickers/' + symbol + '/' + func, params = {
		'access_key': config.API_ACCESSKEY
	})
	return api_response.json()

def getAncillaryData(type):
	api_response = requests.get(constants.BASE_URL + '/' + type , params = {
		'access_key': config.API_ACCESSKEY
	})
	return api_response.json()

def getIntraday(symbol, interval = "5min"):
	api_response = requests.get(constants.BASE_URL + '/intraday', params = {
		'access_key': config.API_ACCESSKEY,
		'symbols': symbol,
		'interval': interval
	})
	return api_response.json()

def getSplits(symbol):
	api_response = requests.get(constants.BASE_URL + '/splits', params = {
		'access_key': config.API_ACCESSKEY,
		'symbols': symbol
	})
	return api_response.json()

def validateResponse(api_response):
	if "error" in api_response:
		print('Error reported by service:', api_response["error"]["message"])
		return False
	else:
		return True
