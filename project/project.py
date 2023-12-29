import re
import requests
import pandas as pd
from bs4 import BeautifulSoup
from tabulate import tabulate


# Constants
# BSE_URL: URL providing the list of top companies listed on the Bombay Stock Exchange (BSE), India
BSE_URL = "https://www.bseindia.com/markets/equity/EQReports/TopMarketCapitalization.aspx"

# ALPHA_VANTAGE_URL: Base URL for Alpha Vantage API
ALPHA_VANTAGE_URL = 'https://www.alphavantage.co/query?'

# ALPHA_VANTAGE_KEY: Your Alpha Vantage API key; Sign up for a free API key at https://www.alphavantage.co/support/#api-key
ALPHA_VANTAGE_KEY = 'YOUR_API_KEY'

# USER_AGENT: User agent information to be included in the header for web scraping.
# Retrieve your user agent from https://www.whatismybrowser.com/
# Including a header declaration in your Python script helps prevent your activity from being classified as spam
# and potentially blacklisted by the target website.
USER_AGENT = 'YOUR_USER_AGENT'


# Function to fetch BSE100 companies name and symbol from the BSE site
def fetch_bse_top_companies_list(url, user_agent):
    """
    Fetches BSE100 companies' names, symbols, and closing prices from the BSE site.

    Args:
        url (str): URL of the BSE page.
        user_agent (str): User agent for the HTTP request.

    Returns:
        List[Dict]: List of dictionaries containing company information.

    Raises:
        requests.exceptions.HTTPError: If the HTTP request to the BSE site fails.
        ValueError: If the parsing of the HTML content encounters unexpected structures.

    Example:
        Example usage of the function:

        >>> url = "https://example.com/bse100"
        >>> user_agent = "YOUR_USER_AGENT"
        >>> companies_info = fetch_bse_top_companies_list(url, user_agent)
    """

    headers = {'User-Agent': user_agent}

    try:
        # Send an HTTP GET request to the specified URL
        response = requests.get(url, headers=headers)
        response.raise_for_status()

        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract relevant information from the HTML content
        anchor_tags = soup.select('td.tdcolumn a.tablebluelink')
        pattern = r'/([^/]+)/(?:[^/]+)/$'
        tag = re.compile(rf'ContentPlaceHolder1_gvData_lblTurnover_\d+')

        # Collect company information in a list of dictionaries
        company_info = []
        for anchor in anchor_tags:
            closing_price_td = anchor.find_next('td', {'class': 'tdcolumn text-right'})
            closing_price = float(closing_price_td.find('span', {'id': tag}).text.strip())

            # Append the data to the list
            company_info.append({
                'company_name': anchor.text.strip(),
                'symbol': re.search(pattern, anchor['href']).group(1).upper(),
                'closing_price': closing_price
            })

        return company_info

    except requests.exceptions.HTTPError as e:
        # Handle HTTP errors by raising an exception with details
        raise e

    except Exception as e:
        # Handle unexpected parsing errors by raising a ValueError
        raise ValueError(f"Error parsing HTML content: {e}")



# Function to fetch time series data from Alpha Vantage
def fetch_time_series(url, symbol, api_key):
    """
    Fetches time series data for a given symbol from Alpha Vantage using the TIME_SERIES_DAILY function.

    Parameters:
        url (str): The base URL for Alpha Vantage API.
        symbol (str): The stock symbol for which to fetch time series data.
        api_key (str): The API key for accessing Alpha Vantage.

    Returns:
        pd.DataFrame: A pandas DataFrame containing the daily time series data for the specified symbol.

    Raises:
        requests.exceptions.HTTPError: If the HTTP request to the Alpha Vantage API fails.
        KeyError: If the response does not contain the expected time series data.
        ValueError: If the time series data cannot be converted to a pandas DataFrame.

    Example:
        Example usage of the function:

        >>> url = "https://www.alphavantage.co/query?"
        >>> symbol = "AAPL"
        >>> api_key = "your_api_key"
        >>> # Fetch daily time series data for Apple (AAPL) using Alpha Vantage API
        >>> time_series_data = fetch_time_series(url, symbol, api_key)
    """

    # Prepare parameters for the Alpha Vantage API request
    params = {
        'function': 'TIME_SERIES_DAILY',
        'symbol': symbol,
        'outputsize': 'full',
        'apikey': api_key
    }

    try:
        # Make the API request to Alpha Vantage
        response = requests.get(url, params=params)
        response.raise_for_status()

        # Parse the JSON response and convert it to a pandas DataFrame
        data = response.json()
        df = pd.DataFrame(data["Time Series (Daily)"]).T

        return df

    except requests.exceptions.HTTPError:
        # Handle HTTP errors by raising an exception with details
        raise

    except KeyError:
        # Raise an exception if the expected time series data is not present in the response
        raise KeyError("Time series data not found in the API response")



# Function to fetch RSI data from Alpha Vantage
def fetch_rsi(url, symbol, api_key, time_period, series_type='close'):
    """
    Fetches the Relative Strength Index (RSI) for a given symbol from the Alpha Vantage API.

    Args:
        url (str): The base URL of the Alpha Vantage API.
        symbol (str): The stock symbol for which RSI is to be fetched.
        api_key (str): The API key for accessing the Alpha Vantage API.
        time_period (int): The time period to calculate RSI over.
        series_type (str, optional): The price series to use for RSI calculation (default is 'close').
            Valid values are 'close', 'open', 'high', 'low'.

    Returns:
        float: The latest RSI value for the specified stock symbol.

    Raises:
        requests.exceptions.HTTPError: If the HTTP request to the Alpha Vantage API fails.
        KeyError: If the response does not contain the expected RSI data.
        ValueError: If the RSI data cannot be converted to a pandas DataFrame.

    Example:
        Example usage of the function:

        >>> url = "https://www.alphavantage.co/query"
        >>> symbol = "AAPL"
        >>> api_key = "your_api_key"
        >>> time_period = 14
        >>> # Fetch RSI for Apple (AAPL) with a time period of 14 days
        >>> current_rsi = fetch_rsi(url, symbol, api_key, time_period)
    """

    # Prepare parameters for the Alpha Vantage API request
    params = {
        'function': 'RSI',
        'symbol': symbol,
        'interval': 'daily',
        'time_period': time_period,
        'series_type': series_type,
        'apikey': api_key
    }

    try:
        # Send an HTTP GET request to the Alpha Vantage API
        response = requests.get(url, params=params)
        response.raise_for_status()

        # Parse the JSON response and convert it to a pandas DataFrame
        data = response.json()
        df = pd.DataFrame(data['Technical Analysis: RSI']).T.astype(float)

        # Extract the latest RSI value
        current_rsi = df.iloc[0]['RSI']
        return current_rsi

    except requests.exceptions.HTTPError:
        # Handle HTTP errors by raising an exception with details
        raise

    except KeyError:
        # Raise an exception if the expected RSI data is not present in the response
        raise KeyError("RSI data not found in the API response.")




# Function to calculate MACD and Signal Line
def calculate_macd_and_signal_line(data):
    """
    Calculate Moving Average Convergence Divergence (MACD) and Signal Line.

    Args:
        data (pd.DataFrame): The DataFrame containing stock price data, including the "4. close" column.

    Returns:
        tuple: Latest MACD value and latest Signal Line value.

    Example:
        Example usage of the function:

        >>> # Assuming 'data' is a DataFrame with stock price data
        >>> latest_macd, latest_signal = calculate_macd_and_signal_line(data)
    """

    # Calculate 12-day and 26-day Exponential Moving Averages (EMAs)
    ema_12 = data["4. close"].ewm(span=12, adjust=False).mean()
    ema_26 = data["4. close"].ewm(span=26, adjust=False).mean()

    # Merge EMAs into a single DataFrame
    merged_df = pd.merge(ema_12, ema_26, left_index=True, right_index=True, suffixes=('_ema12', '_ema26'))

    # Calculate MACD (Moving Average Convergence Divergence)
    merged_df['MACD'] = merged_df['4. close_ema12'] - merged_df['4. close_ema26']
    latest_macd_value = round(merged_df['MACD'].iloc[-1], 2)

    # Calculate Signal Line using a 9-day EMA on the MACD
    merged_df['Signal_Line'] = merged_df['MACD'].ewm(span=9, adjust=False).mean()
    latest_signal_value = round(merged_df['Signal_Line'].iloc[-1], 2)

    return latest_macd_value, latest_signal_value



# Main function
def main():
    """
    Main function to fetch BSE top companies, analyze their indicators, and print the top 5 companies.
    """
    # Fetch BSE top companies information
    companies_info = fetch_bse_top_companies_list(BSE_URL, USER_AGENT)

    # Initialize a list to store information about top companies
    top_companies = []

    # Loop through the first 12 companies in the BSE100 list
    for company in companies_info[:12]:
        symbol = f"{company['symbol']}.BSE"

        # Fetch time series data for the company from Alpha Vantage
        data = fetch_time_series(ALPHA_VANTAGE_URL, symbol, ALPHA_VANTAGE_KEY)

        # Sort the time series data by date in ascending order
        data_sorted = data.copy().sort_index(ascending=True)

        # Convert the '4. close' column to numeric
        data_sorted["4. close"] = pd.to_numeric(data_sorted["4. close"], errors='coerce')

        # Calculate Exponential Moving Averages (EMAs) with periods of 20, 50, and 200 days
        ema_20 = data_sorted["4. close"].ewm(span=20, adjust=False).mean().iloc[-1]
        ema_50 = data_sorted["4. close"].ewm(span=50, adjust=False).mean().iloc[-1]
        ema_200 = data_sorted["4. close"].ewm(span=200, adjust=False).mean().iloc[-1]

        # Fetch the current Relative Strength Index (RSI) value
        current_rsi = fetch_rsi(ALPHA_VANTAGE_URL, symbol, ALPHA_VANTAGE_KEY, time_period=14)

        # Calculate MACD and Signal Line values
        macd_value, signal_line_value = calculate_macd_and_signal_line(data_sorted)

        # Extract the closing price of the company
        closing_price = company['closing_price']

        # Check conditions for inclusion in the top companies list
        if (
            current_rsi > 50 and
            closing_price > max(ema_20, ema_50, ema_200) * 1.01 and
            macd_value > signal_line_value
        ):
            top_companies.append({
                'company_name': company['company_name'],
                'symbol': company['symbol'],
                'closing_price': closing_price,
                'ema_20': ema_20,
                'ema_50': ema_50,
                'ema_200': ema_200,
                'rsi': current_rsi,
                'macd': macd_value,
                'signal_line': signal_line_value
            })

    # Sort the top companies based on RSI in descending order
    top_companies.sort(key=lambda x: x['rsi'], reverse=True)

    # Select the top 5 companies
    top5_companies = top_companies[:5]

    # Print information of the top 5 companies from the first 12 companies on the BSE100 list
    print(tabulate(top5_companies, headers='keys'))


if __name__ == "__main__":
    main()
