#Assignment: implement a program that:

   #Expects the user to specify as a command-line argument the number of Bitcoins, n, that they would like to buy.
   #If that argument cannot be converted to a float, the program should exit via sys.exit with an error message.
   #Queries the API for the CoinDesk Bitcoin Price Index at https://api.coindesk.com/v1/bpi/currentprice.json,
   #which returns a JSON object, among whose nested keys is the current price of Bitcoin as a float. Be sure to
   #catch any exceptions, as with code like:
        #import requests
        #try:
           #...
        #except requests.RequestException:
          #...
   #Outputs the current cost of n Bitcoins in USD to four decimal places, using , as a thousands separator.


import json
import requests
import sys

def main():
   #get the number of Bitcoins
   n = get_bitcoin_numer(sys.argv)
   amount = get_amount_usd(n)
   print(f'${amount:,.4f}')



def get_bitcoin_numer(arg):
   if len(arg) == 1:
      sys.exit('Missing command-line argument')
   elif len(arg) == 2:
      try:
         return float(arg[1])
      except ValueError:
         sys.exit('Command-line argument is not a number')



def get_amount_usd(nn):
   try:
      response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
      o = response.json()
      usd_rate = o["bpi"]["USD"]["rate"]
      usd_rate = float(usd_rate.replace(",", ""))
      return usd_rate * nn
   except requests.RequestException:
      sys.exit()



if __name__ == "__main__":
     main()




