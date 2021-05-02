import unittest
import marketStack


def test_checkProfile():
    assert marketStack.checkProfile("GarbageProfile") == False


def test_readTicker(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "WTC.XASX")
    ticker = marketStack.readTicker()
    assert ticker == "WTC.XASX"
