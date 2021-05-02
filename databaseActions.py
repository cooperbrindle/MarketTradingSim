import pyodbc
import json
import config

def insertData(api_response, key):
	cursor, cnxn = connect()
	x = 0
	while x < 100:
		cursor.execute("insert into dailyResults(DR_SP, DR_High, DR_Low, DR_Close, DR_Date) values (?, ?, ?, ?, ?)", key,
					   api_response["data"]["eod"][x]["high"], api_response["data"]["eod"][x]["low"], api_response["data"]["eod"][x]["close"], api_response["data"]["eod"][x]["date"])
		cnxn.commit()
		x += 1

def createProfile(api_response):
	cursor, cnxn = connect()
	print('Creating', api_response["data"]["symbol"])
	cursor.execute("insert into stockProfile(SP_Name, SP_Symbol) values (?, ?)",
				   api_response["data"]["name"], api_response["data"]["symbol"])
	cnxn.commit()
	cursor.execute("select SP_PK from stockProfile where SP_Symbol = ?",
				   api_response["data"]["symbol"])
	row = cursor.fetchone()
	return row.SP_PK

def checkProfile(symbol):
	cursor, cnxn = connect()
	cursor.execute(
		"select SP_PK from stockProfile where SP_Symbol = ?", symbol)
	row = cursor.fetchone()
	if row:
		print(symbol, 'already exists.')
		return row.SP_PK
	else:
		print(symbol, 'not found.')
		return False

def connect():
	server = config.DB_SERVER
	database = config.DB_DATABASE
	username = config.DB_USERNAME
	password = config.DB_PASSWORD
	cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' +
						  server+';DATABASE='+database+';UID='+username+';PWD=' + password)
	cursor = cnxn.cursor()
	return cursor, cnxn