import main

def test_inputAction(monkeypatch):
	monkeypatch.setattr('builtins.input', lambda _: "help")
	action = main.inputAction()
	assert action == "help"

def test_menuControl():
	pass

def test_addTicker():
	pass

def test_inputTicker():
	pass

def test_printExchanges():
	pass

def test_showOptions(capsys):  # or use "capfd" for fd-level
	main.showOptions()
	captured = capsys.readouterr()
	assert captured.out == "help: Show available actions\n" + "add-ticker: Collect data on a company\n" + \
		"exchanges: Print list of available exchanges\n" + "close: Close program\n"