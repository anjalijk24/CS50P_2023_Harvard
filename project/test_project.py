
import pytest
from project import fetch_bse_top_comapnies_list, fetch_ema, fetch_rsi


# Constants for testing
BSE_URL = "https://www.bseindia.com/markets/equity/EQReports/TopMarketCapitalization.aspx"
USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:120.0) Gecko/20100101 Firefox/120.0'


def test_fetch_bse_top_comapnies_list():
    # Call the function with the HTTP request
    companies_info = fetch_bse_top_comapnies_list(BSE_URL, USER_AGENT)
    # These assertions are based on the BSE100 list as available on Dec. 2023
    # anyone planning to test these will have to make corrections based on the year and month
    assert companies_info[0]['company_name'] == "RELIANCE INDUSTRIES LTD."
    assert companies_info[0]['symbol'] == "RELIANCE"
    assert isinstance(companies_info[0]['closing_price'], float)


def test_function_2():
    ...


def test_function_n():
    ...
