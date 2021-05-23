import requests
import config
import constants

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

def getExchanges():
	api_response = requests.get(constants.BASE_URL + '/exchanges', params = {
		'access_key': config.API_ACCESSKEY
	})
	return api_response.json()

def getIntraday():
	pass

def getSplits():
	pass

def getCurrencies():
	pass

def getTimezones():
	pass

