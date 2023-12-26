# BSE Stock Analysis Script
#### Video Demo:  

## Overview

This Python script performs analysis on top companies listed on the Bombay Stock Exchange (BSE), India. It fetches data from the BSE website to obtain a list of the top companies and then utilizes the Alpha Vantage API for technical analysis, including Exponential Moving Averages (EMA), Relative Strength Index (RSI), Moving Average Convergence Divergence (MACD), and Signal Line.

## Table of Contents

- [Requirements](#requirements)
- [Configuration](#configuration)
- [Installation](#installation)
- [Script Explanation](#script-explanation)
- [Notes](#notes)
- [Disclaimer](#disclaimer)

## Requirements

- Python 3.x
- Libraries: `requests`, `pandas`, `beautifulsoup4`, `tabulate`

## Configuration

Before running the script, ensure that you have an Alpha Vantage API key. You can obtain a free key by signing up [here](https://www.alphavantage.co/support/#api-key). Replace the placeholder `ALPHA_VANTAGE_KEY` in the script with your actual API key.

Additionally, provide your user agent for web scraping. You can find your user agent [here](https://www.whatismybrowser.com/). Update the `USER_AGENT` variable with your user agent.

## Installation

1. Install the required Python libraries:

   ```bash
   pip install requests pandas beautifulsoup4 tabulate

2. Run the Script

To execute the stock analysis script, open your terminal or command prompt and navigate to the directory where the script (`project.py`) is located. Then, run the following command: 
      python project.py

## Script Explanation

The script performs the following steps:

- **Fetches the list of top companies from the BSE website using web scraping techniques.**
  - Utilizes the BeautifulSoup library to parse HTML and extract relevant information.
  - Identifies company names, symbols, and closing prices.

- **Retrieves various technical indicators for the top companies using the Alpha Vantage API, including EMA, RSI, MACD, and Signal Line.**
  - Makes API requests to Alpha Vantage for each technical indicator.
  - Gathers data and stores it in a pandas DataFrame for analysis.

- **Filters the companies based on specific criteria, such as RSI greater than 50, closing price above certain EMAs, and MACD values.**
  - Implements conditional statements to determine if a company meets the specified criteria.
  - Uses technical indicators to assess the performance of each company.

- **Prints the top 3 companies that meet the criteria in a tabular format.**
  - Utilizes the tabulate library to present the information in a clear and organized table.
  - Displays relevant details such as company name, symbol, closing price, and various technical indicators.

## Notes

- **Data Sensitivity:**
  - Financial markets can be unpredictable, and the script's analysis is based on historical data and algorithms. Past performance is not indicative of future results.

- **API Key Security:**
  - Keep the Alpha Vantage API key secure. Avoid sharing it publicly or embedding it directly in the script if possible. Consider using environment variables or a configuration file for added security.


## Disclaimer

This script was developed as part of the CS50P course and is for educational purposes only. It does not constitute financial advice.  The analysis and results obtained from the script are based on historical data and algorithmic calculations, which may not accurately predict future market conditions.

Always do your own research and consult with a qualified financial professional before making any investment decisions. The author of this script is not responsible for any financial losses or gains that may result from the use of this script. Use it at your own risk.

Please comply with the terms of use of external services such as Alpha Vantage and BSE to ensure ethical and legal usage of their data.


