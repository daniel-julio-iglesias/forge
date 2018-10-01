#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function
import python_forex_quotes

""""Python API script: forge

https://github.com/toddmotto/public-apis/blob/master/README.md#currency-exchange

API: 1Forge
https://1forge.com/forex-data-api/api-documentation
Description: Forex currency market data
Auth: apiKey
HTTPS: Yes
CORS: Unknown

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
"""

client = python_forex_quotes.ForexDataClient('YOUR_API_KEY')

if client.marketIsOpen() == True:
    print("Market is open!")

print(client.getSymbols())
print(client.getQuotes(['EURUSD', 'GBPJPY']))
print(client.quota())
print(client.convert('EUR', 'USD', 100))

if __name__ == '__main__':
    pass
