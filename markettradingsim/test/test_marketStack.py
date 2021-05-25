import requests
import markettradingsim.marketStack as marketStack

def test_validateResponse_error():
	input = MockError.json()
	assert marketStack.validateResponse(input) == False

def test_validateResponse_EOD():
	input = MockEOD.json()
	assert marketStack.validateResponse(input) == True

def test_validateResponse_Ticker():
	pass

def test_validateResponse_AncillaryData():
	pass

def test_validateResponse_Intraday():
	pass

def test_validateResponse_Splits():
	pass

def test_getEOD_error(monkeypatch):
    def mock_get(*args, **kwargs):
        return MockError()

    # apply the monkeypatch for requests.get to mock_get
    monkeypatch.setattr(requests, "get", mock_get)

    # app.get_json, which contains requests.get, uses the monkeypatch
    result = marketStack.getEOD('AAPL')
    assert result["error"]["code"] == "validation_error"

def test_getEOD_ok(monkeypatch):
    def mock_get(*args, **kwargs):
        return MockEOD()

    # apply the monkeypatch for requests.get to mock_get
    monkeypatch.setattr(requests, "get", mock_get)

    # app.get_json, which contains requests.get, uses the monkeypatch
    result = marketStack.getEOD('AAPL')
    assert result["data"][0]["symbol"] == "AAPL"

def test_getTicker_error():
	pass

def test_getTicker_ok():
	pass

def test_getAncillaryData_error():
	pass

def test_getAncillaryData_ok():
	pass

def test_getIntraday_error():
	pass

def test_getIntraday_ok():
	pass

def test_getSplits_error():
	pass

def test_getSplits_ok():
	pass

class MockError:
    # mock json() method always returns a specific testing dictionary
    @staticmethod
    def json():
        return {"error": {
					"code": "validation_error",
					"message": "Request failed with validation error",
					"context": {
							"symbols": [
										{
										"key": "missing_symbols",
										"message": "You did not specify any symbols."
										}
										]
								}
					}
				}

class MockEOD:
    # mock json() method always returns a specific testing dictionary
    @staticmethod
    def json():
        return {"data": [
				{
					"open": 129.8,
					"high": 133.04,
					"low": 129.47,
					"close": 132.995,
					"volume": 106686703.0,
					"adj_high": 133.04,
					"adj_low": 129.47,
					"adj_close": 132.995,
					"adj_open": 129.8,
					"adj_volume": 106686703.0,
					"split_factor": 1.0,
					"symbol": "AAPL",
					"exchange": "XNAS",
					"date": "2021-04-09T00:00:00+0000"
				}
			]
		}	