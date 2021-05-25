import re
import markettradingsim.marketStack as api
import markettradingsim.databaseActions as DB

def main():
	userInput = inputAction()
	while (userInput != 'close'):
		menuControl(userInput)
		userInput = inputAction()

def inputAction():
	action = input(
			"Please enter select action (enter 'help' for options): ")
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
		print("Invalid action entered. Type 'help' to see available actions.")

def addTicker(ticker):
	key = DB.checkProfile(ticker["symbol"])
	if key == False:
		key = DB.createProfile(ticker)
	DB.insertData(ticker["eod"], key)

def inputTicker():
	while True:
		symbol = input("Please enter stock code: ")
		if not re.match("^[A-Za-z]*$", symbol):
			print("Error! Only text can be entered!")
		else:
			break
	while True:
		exchange = input("Please enter exchange: ")
		if not re.match("^[A-Za-z]*$", exchange):
			print("Error! Only text can be entered!")
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
	print("help: Show available actions")
	print("add-ticker: Collect data on a company")
	print("exchanges: Print list of available exchanges")
	print("close: Close program")

if __name__ == "__main__":
	main()
