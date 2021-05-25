import pyodbc
import config as config

def insertData(data, key):
	cursor, cnxn = connect()
	x = 0
	for day in data:
		cursor.execute("insert into dailyResults(DR_SP, DR_High, DR_Low, DR_Close, DR_Date) values (?, ?, ?, ?, ?)", key,
					   day["high"], day["low"], day["close"], day["date"])
		cnxn.commit()

def createProfile(data):
	cursor, cnxn = connect()
	print('Creating', data["symbol"])
	cursor.execute("insert into stockProfile(SP_Name, SP_Symbol) values (?, ?)",
				   data["name"], data["symbol"])
	cnxn.commit()
	cursor.execute("select SP_PK from stockProfile where SP_Symbol = ?",
				   data["symbol"])
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