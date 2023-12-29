import pytest
import requests
import pandas as pd
from unittest.mock import Mock, patch
from project import fetch_bse_top_companies_list, fetch_time_series, fetch_rsi


# Constants for testing
BSE_URL = "https://www.bseindia.com/markets/equity/EQReports/TopMarketCapitalization.aspx"
USER_AGENT = 'YOUR_USER_AGENT'


def test_fetch_bse_top_companies_list():
    # Call the function with the HTTP request
    companies_info = fetch_bse_top_companies_list(BSE_URL, USER_AGENT)
    # The following  assertions are made based on the BSE100 list available in December 2023.
    # To adapt them for testing, it's essential to modify them in accordance with the relevant year and month.
    assert companies_info[0]['company_name'] == "RELIANCE INDUSTRIES LTD."
    assert companies_info[0]['symbol'] == "RELIANCE"
    assert isinstance(companies_info[0]['closing_price'], float)



# Mock responses
mock_correct_response = {
    'Time Series (Daily)': {
        '2005-01-14': {'1. open': '355.7379', '2. high': '356.4194', '3. low': '348.3097', '4. close': '349.8430', '5. volume': '13240871'}
    }
}

mock_http_error_response = Mock()
mock_http_error_response.raise_for_status.side_effect = requests.exceptions.HTTPError("HTTP error")
mock_key_error_response = {"some_other_key": "some_value"}

symbol = "RELIANCE.BSE"
api_key = "YOUR_API_KEY"

# Mock requests.get method to return the desired responses
@patch("requests.get")
def test_fetch_time_series(mock_requests_get):
    url = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY"

    # Test success scenario
    mock_requests_get.return_value.json.return_value = mock_correct_response
    time_series_data = fetch_time_series(url, symbol, api_key)

    # Assertions for success scenario
    assert isinstance(time_series_data, pd.DataFrame)
    assert not time_series_data.empty

    # Assert relevant keys are present in the DataFrame
    expected_keys = {"1. open", "2. high", "3. low", "4. close", "5. volume"}
    assert set(time_series_data.columns) == expected_keys

    # Test HTTPError
    mock_requests_get.return_value = mock_http_error_response
    with pytest.raises(requests.exceptions.HTTPError):
        fetch_time_series(url, symbol, api_key)

    # Test KeyError
    mock_requests_get.return_value = Mock(json=lambda: mock_key_error_response)
    with pytest.raises(KeyError, match="Time series data not found in the API response"):
        fetch_time_series(url, symbol, api_key)



# Mock requests.get method to return the desired responses
@patch("requests.get")
def test_fetch_rsi(mock_requests_get):
    url = "https://www.alphavantage.co/query?function=RSI"
    time_period = 14

    # Test success scenario
    mock_correct_response = {
        'Technical Analysis: RSI': {
            '2023-01-02': {'RSI': '70.0'},
            '2023-01-01': {'RSI': '75.0'},
        }
    }

    mock_requests_get.return_value.json.return_value = mock_correct_response
    rsi_value = fetch_rsi(url, symbol, api_key, time_period)

    # Assertions for success scenario
    assert isinstance(rsi_value, float)
    assert rsi_value == 70.0  # Adjust the expected result based on your test data

    # Test HTTPError
    mock_requests_get.return_value = mock_http_error_response
    with pytest.raises(requests.exceptions.HTTPError):
        fetch_rsi(url, symbol, api_key, time_period)

    # Test KeyError
    mock_requests_get.return_value = Mock(json=lambda: mock_key_error_response)
    with pytest.raises(KeyError, match="RSI data not found in the API response."):
        fetch_rsi(url, symbol, api_key, time_period)


