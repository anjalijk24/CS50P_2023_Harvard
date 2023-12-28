# BSE Top Companies Analysis
#### Video Demo:

## Overview

This Python script performs analysis on the top companies listed on the Bombay Stock Exchange (BSE), utilizing data from the Alpha Vantage API. It fetches company information, calculates various financial indicators, and identifies the top 5 companies based on specific criteria.

## Prerequisites

Before running the script, ensure you have the following prerequisites:

- Python 3.x installed
- Required Python libraries: `requests`, `pandas`, `BeautifulSoup` (bs4), `tabulate`

## Setup

1. Clone the repository or download the script.
2. Install the required Python libraries:

   ```bash
   pip install requests pandas beautifulsoup4 tabulate
3. Replace placeholders in the script:

    Replace 'YOUR_API_KEY' with your Alpha Vantage API key.
    Replace 'YOUR_USER_AGENT_INFO' with your user agent information.

### Script Structure

#### Constants

1. **BSE_URL:**
    - URL providing the list of top companies listed on the Bombay Stock Exchange (BSE), India.

    ```python
    BSE_URL = "https://www.bseindia.com/markets/equity/EQReports/TopMarketCapitalization.aspx"
    ```

2. **ALPHA_VANTAGE_URL:**
    - Base URL for Alpha Vantage API.

    ```python
    ALPHA_VANTAGE_URL = 'https://www.alphavantage.co/query?'
    ```

3. **ALPHA_VANTAGE_KEY:**
    - Your Alpha Vantage API key.

    ```python
    ALPHA_VANTAGE_KEY = 'YOUR_API_KEY'
    ```

4. **USER_AGENT:**
    - User agent information for the HTTP request.
    - Retrieve your user agent from [WhatIsMyBrowser](https://www.whatismybrowser.com/).

    ```python
    USER_AGENT = 'YOUR_USER_AGENT_INFO'
    ```

These constants define essential URLs and keys required for fetching data from the BSE website and the Alpha Vantage API.

#### Functions

1. `fetch_bse_top_companies_list(url, user_agent)`

   - **Description:**
     Fetches BSE100 companies' names, symbols, and closing prices from the BSE site.

   - **Parameters:**
     - `url`: URL of the BSE page.
     - `user_agent`: User agent for the HTTP request.

   - **Returns:**
     - List of dictionaries containing company information.
2. `fetch_time_series(url, symbol, api_key)`

   - **Description:**
     Fetches time series data for a given symbol from Alpha Vantage using the TIME_SERIES_DAILY function.

   - **Parameters:**
     - `url`: Base URL for Alpha Vantage API.
     - `symbol`: The stock symbol for which to fetch time series data.
     - `api_key`: The API key for accessing Alpha Vantage.

   - **Returns:**
     - Pandas DataFrame containing the daily time series data.

3. `fetch_rsi(url, symbol, api_key, time_period, series_type='close')`

   - **Description:**
     Fetches the Relative Strength Index (RSI) for a given symbol from the Alpha Vantage API.

   - **Parameters:**
     - `url`: Base URL of the Alpha Vantage API.
     - `symbol`: The stock symbol for which RSI is to be fetched.
     - `api_key`: The API key for accessing the Alpha Vantage API.
     - `time_period`: The time period to calculate RSI over.
     - `series_type` (optional): The price series to use for RSI calculation (default is 'close').

   - **Returns:**
     - Latest RSI value for the specified stock symbol.
4. `calculate_macd_and_signal_line(data)`

   - **Description:**
     Calculates Moving Average Convergence Divergence (MACD) and Signal Line.

   - **Parameters:**
     - `data`: DataFrame containing stock price data, including the "4. close" column.

   - **Returns:**
     - Tuple with the latest MACD value and latest Signal Line value.

5. `main()`

   - **Description:**
     Main function to fetch BSE top companies, analyze their indicators, and print the top 5 companies.


### Disclaimer

This script is provided for educational and informational purposes only. By using this script, you agree to:

- Use the script responsibly and in accordance with the terms of service of the Bombay Stock Exchange (BSE) website.
- Adhere to the terms and conditions of the Alpha Vantage API when accessing data.
- Understand that the script involves financial data analysis and comes with inherent risks.
- Acknowledge that the script may not be suitable for real-time trading decisions.

**Use at your own risk:** The script author is not responsible for any financial losses or other consequences resulting from the use of this script. It is recommended to verify and validate any data or analysis provided by the script before making financial decisions.

Ensure compliance with the terms of service of the BSE website and Alpha Vantage API, and exercise caution when using financial data for decision-making.
