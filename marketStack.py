import pyodbc
import json
import requests
import config

def main():
	ticker = readTicker()
	while (ticker != 'close'):
		api_response = getTicker(ticker)
		print('You pulled data on', api_response["data"]["symbol"], api_response["data"]["name"])
		key = stockProfile(api_response)
		insertData(api_response, key)
		ticker = readTicker()

def insertData(api_response, key):
	cursor, cnxn = connect()
	x = 0
	while x < 100:
		cursor.execute("insert into dailyResults(DR_SP, DR_High, DR_Low, DR_Close, DR_Date) values (?, ?, ?, ?, ?)", key, api_response["data"]["eod"][x]["high"], api_response["data"]["eod"][x]["low"], api_response["data"]["eod"][x]["close"], api_response["data"]["eod"][x]["date"])
		cnxn.commit()
		x += 1

def stockProfile(api_response):
	cursor, cnxn = connect()
	cursor.execute("select SP_PK from stockProfile where SP_Symbol = ?", api_response["data"]["symbol"])
	row = cursor.fetchone()
	if row:
		print(api_response["data"]["symbol"], 'already exists.')
		return row.SP_PK
	else:
		print('Creating', api_response["data"]["symbol"])
		cursor.execute("insert into stockProfile(SP_Name, SP_Symbol) values (?, ?)", api_response["data"]["name"], api_response["data"]["symbol"])
		cnxn.commit()
		cursor.execute("select SP_PK from stockProfile where SP_Symbol = ?", api_response["data"]["symbol"])
		row = cursor.fetchone()
		return row.SP_PK

def readTicker():
	ticker = input("Please input your stock code or type 'close' to finish: ")
	return ticker

def getTicker(ticker):
	params = {
		'access_key': config.API_ACCESSKEY
	}
	url = 'http://api.marketstack.com/v1/tickers/' + ticker + '/eod'
	# Call MarketStack
	api_result = requests.get(url, params)
	api_response = api_result.json()
	return api_response
	
def connect():
	server = config.DB_SERVER
	database = config.DB_DATABASE
	username = config.DB_USERNAME
	password = config.DB_PASSWORD
	cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
	cursor = cnxn.cursor()
	return cursor, cnxn

if __name__== "__main__":
	main()