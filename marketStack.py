import json
import requests
import config
import constants
import re
import databaseActions as DB

def main():
	userInput = inputAction()
	while (userInput != 'close'):
		if userInput == 'help':
			showOptions()
		elif userInput == 'data':
			ticker = inputTicker()
			api_response = getData(ticker)
			print('You pulled data on',
			  api_response["data"]["symbol"], api_response["data"]["name"])
			key = DB.checkProfile(api_response["data"]["symbol"])
			if key == False:
				key = DB.createProfile(api_response)
			DB.insertData(api_response, key)
		else:
			print("Invalid action entered. Type 'help' to see available actions.")
		userInput = inputAction()

def inputAction():
	while True:
		action = input("Please enter select action (enter 'help' for options): ")
		if not re.match("^[A-Za-z]*$", action):
			print("Error! Only text can be entered!")
		else:
			break
	return action

def inputTicker():
	while True:
		code = input("Please enter stock code: ")
		if not re.match("^[A-Za-z]*$", code):
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
		ticker = code
	else:
		ticker = code + '.' + exchange
	print(ticker + ' entered.')
	return ticker

def getData(ticker):
	params = {
		'access_key': config.API_ACCESSKEY
	}
	url = constants.BASE_URL + '/tickers/' + ticker + '/eod'
	api_result = requests.get(url, params)
	api_response = api_result.json()
	return api_response

def showOptions():
	print("help - Show available actions")
	print("data - Collect data on a company")
	print("close - Close program")

if __name__ == "__main__":
	main()
