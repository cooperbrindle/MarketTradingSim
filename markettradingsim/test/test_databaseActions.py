import markettradingsim.databaseActions as DB

def test_checkProfile():
    assert DB.checkProfile("GarbageProfile") == False