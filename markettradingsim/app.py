import re
from markettradingsim.constants import MENU_CONSTANTS, TEXTONLY
import markettradingsim.marketStack as api
import markettradingsim.databaseActions as DB
import flask
from flask import Flask, render_template, redirect, url_for, request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET', 'POST'])
def home():
	error = None
	if request.method == 'POST':
		if request.form['submit'] == 'add-ticker':
			inputTicker(request.form)
		elif request.form['submit'] == 'get-exchanges':
			printExchanges()
		else:
			pass
	return render_template('home.html', error=error)

# Route for handling the login page logic

@app.route('/login', methods=['GET', 'POST'])
def login():
	error = None
	if request.method == 'POST':
		if request.form['username'] != 'admin' or request.form['password'] != 'admin':
			error = 'Invalid Credentials. Please try again.'
		else:
			return redirect(url_for('home'))
	return render_template('login.html', error=error)

def inputTicker(entries):
	stockCode = entries['Stock Code'].upper()
	exchange = entries['Exchange'].upper()
	if re.match(TEXTONLY["REGEX"], exchange) and re.match(TEXTONLY["REGEX"], stockCode):
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