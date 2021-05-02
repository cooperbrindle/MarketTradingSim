import unittest
import marketStack
import sys

def test_inputAction(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "help")
    action = marketStack.inputAction()
    assert action == "help"

def test_showOptions(capsys):  # or use "capfd" for fd-level
    marketStack.showOptions()
    captured = capsys.readouterr()
    assert captured.out == "help - Show available actions\n" + "data - Collect data on a company\n" + "close - Close program\n"
