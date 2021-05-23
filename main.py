import re
import marketStack as api
import databaseActions as DB

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
		addTicker(api_response)
	elif userInput == 'exchanges':
		api_response = api.getExchanges()
		if validateResponse(api_response):
			printExchanges(api_response["data"])
	else:
		print("Invalid action entered. Type 'help' to see available actions.")

def addTicker(api_response):
	if validateResponse(api_response):
		key = DB.checkProfile(api_response["data"]["symbol"])
		if key == False:
			key = DB.createProfile(api_response["data"])
		DB.insertData(api_response["data"]["eod"], key)

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

def validateResponse(api_response):
	if "error" in api_response:
		print('Error reported by service:', api_response["error"]["message"])
		return False
	else:
		return True

def showOptions():
	print("help: Show available actions")
	print("add-ticker: Collect data on a company")
	print("exchanges: Print list of available exchanges")
	print("close: Close program")

if __name__ == "__main__":
	main()
