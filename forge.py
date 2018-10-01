#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function
import python_forex_quotes
from config import Config

""""Python API script: forge

https://github.com/toddmotto/public-apis/blob/master/README.md#currency-exchange

API: 1Forge
https://1forge.com/forex-data-api/api-documentation
Description: Forex currency market data
Auth: apiKey
HTTPS: Yes
CORS: Unknown

YOUR_API_KEY=SECRET_KEY  {environment variable}

Script would be called like:

$ python forge_api_script.py output.csv pairs=EURUSD --debug

where:
output.csv - output filename
pairs=EURUSD – currency pair to be returned by API
--debug turns debug mode of the script i.e.: more detailed log messages
Running above command would result in sending request to the following
endpoint https://forex.1forge.com/1.0.3/quotes?pairs=EURUSD with pairs=EURUSD as query argument
and saving output data to output.csv file.
https://forex.1forge.com/1.0.3/quotes?pairs=EURUSD

REQUEST:
GET https://forex.1forge.com/1.0.3/quotes?pairs=EURUSD,GBPJPY,AUDUSD&api_key=YOUR_API_KEY

RESPONSE:
[
     {
          symbol: "AUDUSD",
          price: 0.792495,
          bid: 0.79248,
          ask: 0.79251,
          timestamp: 1502160793
     },
     {
          symbol: "EURUSD",
          price: 1.181,
          bid: 1.18099,
          ask: 1.18101,
          timestamp: 1502160794
     },
     {
          symbol: "GBPJPY",
          price: 144.3715,
          bid: 144.368,
          ask: 144.375,
          timestamp: 1502160794
     }
]

Current Plan: Free
Update frequency: 100 updates per second
Currency pairs: Over 700 currency pairs+gold and silver
REST Rate Limiting: 1,000 requests per day
WebSocket Support: None
Delivery formats: JSON
Redundancy: Basic
Encryption: 256-bit
"""


class Forge:
    def __init__(self, api_key=None):
        # You can get an API key for free at 1forge.com
        if api_key is None:
            self.api_key = Config.SECRET_KEY or 'YOUR_API_KEY'
        else:
            self.api_key = api_key
        # Instantiate the client
        self.client = python_forex_quotes.ForexDataClient(self.api_key)

    # Check if the market is open
    def market_is_open(self):
        if self.client.marketIsOpen():
            return True
        else:
            return False

    # Get the list of available symbols
    def get_symbols(self):
        symbols = self.client.getSymbols()
        return symbols

    # Get quotes for specified symbols
    def get_quotes(self, specified_symbols):
        quotes = self.client.getQuotes(specified_symbols)
        return quotes

    # Check your usage / quota limit
    def quota(self):
        quota = self.client.quota()
        return quota

    # Convert from one currency to another
    def convert(self, from_currency, to_currency, from_currency_value):
        conversion = self.client.convert(from_currency, to_currency, from_currency_value)
        return conversion


if __name__ == '__main__':
    forge = Forge()

    if forge.market_is_open():
        print("Market is open!")
    else:
        print("Market is closed!")

    print(forge.get_symbols())

    specified_symbols = ['EURUSD', 'GBPJPY']
    print(forge.get_quotes(specified_symbols))

    print(forge.quota())

    from_currency = 'EUR'
    to_currency = 'USD'
    from_currency_value = 100
    print(forge.convert(from_currency, to_currency, from_currency_value))
