import re
import tkinter as tk
from markettradingsim.constants import MENU_CONSTANTS, TEXTONLY
import markettradingsim.marketStack as api
import markettradingsim.databaseActions as DB

def inputTicker(entries):
	stockCode = entries['Stock Code'].get().upper()
	exchange = entries['Exchange'].get().upper()
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

def makeform(root):
	entries = {}
	for field in MENU_CONSTANTS["FIELDS"]:
		print(field)
		row = tk.Frame(root)
		lab = tk.Label(row, width=22, text=field+": ", anchor='w')
		ent = tk.Entry(row)
		ent.insert(0, "")
		row.pack(side=tk.TOP,
				fill=tk.X,
				padx=5,
				pady=5)
		lab.pack(side=tk.LEFT)
		ent.pack(side=tk.RIGHT,
				expand=tk.YES,
				fill=tk.X)
		entries[field] = ent
	return entries

if __name__ == '__main__':
	root = tk.Tk()
	ents = makeform(root)
	b1 = tk.Button(root, text='Add Ticker',
			command=(lambda e=ents: inputTicker(e)))
	b1.pack(side=tk.LEFT, padx=5, pady=5)
	b2 = tk.Button(root, text='Print Exchanges',
			command=(lambda e=ents: printExchanges()))
	b2.pack(side=tk.LEFT, padx=5, pady=5)
	b3 = tk.Button(root, text='Quit', command=root.quit)
	b3.pack(side=tk.LEFT, padx=5, pady=5)
	root.mainloop()
