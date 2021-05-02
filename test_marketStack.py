import unittest
import marketStack

def test_checkProfile():
    assert marketStack.checkProfile("GarbageProfile") == False
