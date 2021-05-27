import re
from markettradingsim.constants import MENU_CONSTANTS, TEXTONLY
import markettradingsim.marketStack as api
import markettradingsim.databaseActions as DB

def main():
	userInput = inputAction()
	while (userInput != 'close'):
		menuControl(userInput)
		userInput = inputAction()

def inputAction():
	action = input(MENU_CONSTANTS["WELCOME"])
	return action

def menuControl(userInput):
	if userInput == 'help':
		showOptions()
	elif userInput == 'add-ticker':
		ticker = inputTicker()
		api_response = api.getTicker(ticker, 'eod')
		if api.validateResponse(api_response):
			addTicker(api_response["data"])
	elif userInput == 'exchanges':
		api_response = api.getAncillaryData(userInput)
		if api.validateResponse(api_response):
			printExchanges(api_response["data"])
	else:
		print(MENU_CONSTANTS["INVALID"])

def addTicker(ticker):
	key = DB.checkProfile(ticker["symbol"])
	if key == False:
		key = DB.createProfile(ticker)
	DB.insertData(ticker["eod"], key)

def inputTicker():
	while True:
		symbol = input("Please enter stock code: ")
		if not re.match(TEXTONLY["REGEX"], symbol):
			print(TEXTONLY["ERROR"])
		else:
			break
	while True:
		exchange = input("Please enter exchange: ")
		if not re.match(TEXTONLY["REGEX"], exchange):
			print(TEXTONLY["ERROR"])
		else:
			break
	if exchange == 'XNAS' or exchange == 'xnas':
		ticker = symbol
	else:
		ticker = symbol + '.' + exchange
	print(ticker + ' entered.')
	return ticker

def printExchanges(exchanges):
	for exchange in exchanges:
		if exchange["name"] != 'INDEX':
			print('Name:' + exchange["name"] + ' | '
				'Acronym:' + exchange["acronym"] + ' | '
				'Code:' + exchange["mic"])

def showOptions():
	for option in MENU_CONSTANTS["OPTIONS"] :
		print(option["key"] + ': ' + option["message"])

if __name__ == "__main__":
	main()
