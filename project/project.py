

import re
import requests
import pandas as pd
from bs4 import BeautifulSoup
from tabulate import tabulate


# Constants
# The following url provides the list of top companies listed on the Bombay Stock Exchange (BSE), India
BSE_URL = "https://www.bseindia.com/markets/equity/EQReports/TopMarketCapitalization.aspx"
ALPHA_VANTAGE_URL = 'https://www.alphavantage.co/query?'
# use your Alpha Vantage API key here; sign up for a free API key: https://www.alphavantage.co/support/#api-key
ALPHA_VANTAGE_KEY = 'YOUR_KEY_HERE'
# Retrieve your user agent from https://www.whatismybrowser.com/. Use the user agent and include a header
# declaration in your Python script for web scraping. This helps prevent your activity from being classified
# as spam and potentially blacklisted by the target website.
USER_AGENT = 'YOUR_USER_AGENT_INFO_HERE'



# Function to fetch BSE100 companies name and symbol from the BSE site
def fetch_bse_top_comapnies_list(url, user_agent):
    """
    Fetches BSE100 companies' names, symbols, and closing prices from the BSE site.

    Args:
    url (str): URL of the BSE page.
    user_agent (str): User agent for the HTTP request.

    Returns:
    List[Dict]: List of dictionaries containing company information.
    """

    headers = {'User-Agent': user_agent}
    response = requests.get(url, headers=headers)
    response.raise_for_status()


    soup = BeautifulSoup(response.text, 'html.parser')
    anchor_tags = soup.select('td.tdcolumn a.tablebluelink')

    pattern = r'/([^/]+)/(?:[^/]+)/$'
    tag = re.compile(rf'ContentPlaceHolder1_gvData_lblTurnover_\d+')


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



# Function to fetch EMA data from Alpha Vantage
def fetch_ema(url, symbol, api_key, time_period, series_type='close'):
    params = {
        'function': 'EMA',
        'symbol': symbol,
        'interval': 'daily',
        'time_period': time_period,
        'series_type': series_type,
        'apikey': api_key
    }

    # Make the API request
    response = requests.get(url, params=params)
    # Parse the response and extract the data
    data = response.json()
    # Convert the data to a pandas DataFrame
    df = pd.DataFrame(data['Technical Analysis: EMA']).T.astype(float)

    # return the DataFrame
    return df




# Function to fetch RSI data from Alpha Vantage
def fetch_rsi(url, symbol, api_key, time_period, series_type='close'):
    params = {
        'function': 'RSI',
        'symbol': symbol,
        'interval': 'daily',
        'time_period': time_period,
        'series_type': series_type,
        'apikey': api_key
    }

    response = requests.get(url, params=params)
    data = response.json()
    # Convert the data to a pandas DataFrame
    df = pd.DataFrame(data['Technical Analysis: RSI']).T.astype(float)
    # Extract the latest RSI value
    current_rsi = df.iloc[0]['RSI']
    return current_rsi



# Function to calculate MACD and Signal Line
def calculate_macd_and_signal_line(url, symbol, api_key):
    """
    Calculate Moving Average Convergence Divergence (MACD) and Signal Line.

    Args:
    base_url (str): The base URL for Alpha Vantage API.
    symbol (str): The stock symbol.
    api_key (str): Alpha Vantage API key.

    Returns:
    tuple: Latest MACD value and latest Signal Line value.
    """
    ema_12 = fetch_ema(url, symbol, api_key, time_period=12)
    ema_26 = fetch_ema(url, symbol, api_key, time_period=26)

    merged_df = pd.merge(ema_12, ema_26, left_index=True, right_index=True, suffixes=('_ema12', '_ema26'))
    # Calculate MACD
    merged_df['MACD'] = merged_df['EMA_ema12'] - merged_df['EMA_ema26']
    latest_macd_value = round(merged_df['MACD'].iloc[0], 2)

    merged_df['Signal_Line'] = merged_df['MACD'].ewm(span=9, adjust=False).mean()
    latest_signal_value = round(merged_df['Signal_Line'].iloc[0], 2)

    return latest_macd_value, latest_signal_value


# Main function
def main():
    """
    Main function to fetch BSE top companies, analyze their indicators, and print the top 3 companies.
    """
    companies_info = fetch_bse_top_comapnies_list(BSE_URL, USER_AGENT)
    top_companies = []

    for company in companies_info[:5]:
        symbol = f"{company['symbol']}.BSE"

        ema_20       = fetch_ema(ALPHA_VANTAGE_URL, symbol, ALPHA_VANTAGE_KEY, time_period=20).iloc[0]['EMA']
        ema_50       = fetch_ema(ALPHA_VANTAGE_URL, symbol, ALPHA_VANTAGE_KEY, time_period=50).iloc[0]['EMA']
        #ema_200     = fetch_ema(ALPHA_VANTAGE_URL, symbol, ALPHA_VANTAGE_KEY, time_period=200).iloc[0]['EMA']

        current_rsi  = fetch_rsi(ALPHA_VANTAGE_URL, symbol, ALPHA_VANTAGE_KEY, time_period=14)

        macd_value, signal_line_value = calculate_macd_and_signal_line(ALPHA_VANTAGE_URL, symbol, ALPHA_VANTAGE_KEY)

        
        closing_price = company['closing_price']

        if (
            current_rsi > 50 and
            closing_price > ema_20 and
            closing_price > ema_50 and
            closing_price > max(ema_20, ema_50) * 1.01 and
            macd_value > signal_line_value
        ):
            top_companies.append({
                'company_name': company['company_name'],
                'symbol': company['symbol'],
                'closing_price': closing_price,
                'ema_20': ema_20,
                'ema_50': ema_50,
                'rsi': current_rsi,
                'macd': macd_value,
                'signal_line': signal_line_value
            })

    top_companies.sort(key=lambda x: x['rsi'], reverse=True)
    top3_companies = top_companies[:3]

    #print info of the top 3 companies from the first five companies on the BSE100 list
    print(tabulate(top3_companies, headers='keys'))



if __name__ == "__main__":
    main()
