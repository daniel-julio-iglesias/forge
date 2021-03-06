#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function
import python_forex_quotes
from config import Config
import json
import functools
import logging
import time
import argparse
import sys

""""Python API script: forge_api_script.py

Some initial notes :

Reused class ForexDataClient from python_forex_quotes

https://github.com/toddmotto/public-apis/blob/master/README.md#currency-exchange

API: 1Forge
https://1forge.com/forex-data-api/api-documentation
Description: Forex currency market data
Auth: apiKey
HTTPS: Yes
CORS: Unknown

YOUR_API_KEY=FORGE_API_KEY  {environment variable}

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

$python forge_api_script.py
api_key: YOUR_API_KEY

Market is open!

[u'EURHKD', u'EURCNH', u'EURDKK', u'EURMXN', u'EURPLN', u'EURXAG', u'EURXAU', u'EURBTC', u'EURETH', u'EURLTC', 
u'EURXRP', u'EURDSH', u'EURBCH', u'USDEUR', u'USDGBP', u'USDAUD', u'USDNZD', u'USDXAG', u'USDXAU', u'USDBTC', 
(...) 
u'ETHUSD', u'LTCBTC', u'LTCUSD', u'XRPUSD', u'XRPBTC', u'DSHUSD', u'DSHBTC', u'BCHUSD', u'BCHBTC']

[{u'ask': 1.15791, u'timestamp': 1538427545, u'symbol': u'EURUSD', u'price': 1.15786, u'bid': 1.15781}, 
{u'ask': 148.657, u'timestamp': 1538427545, u'symbol': u'GBPJPY', u'price': 148.6395, u'bid': 148.622}]

{u'hours_until_reset': 8, u'quota_used': 4, u'quota_remaining': 996, u'quota_limit': 1000}

{u'text': u'100 EUR is worth 115.786 USD', u'value': 115.786, u'timestamp': 1538427545}

Process finished with exit code 0

The desired command 
python forge_api_script.py output.csv pair=EURUSD --debug
is implemented as 
python forge_api_script.py -f output.csv -p EURUSD -d
obtaining the result
[{"ask": 1.15273, "timestamp": 1538582607, "symbol": "EURUSD", "price": 1.15272, "bid": 1.15272}]

python forge_api_script.py -h

usage: forge_api_script.py [-h] [-v] [--filename FILENAME] [--pair PAIRS]
                           [--debug] [--market-is-open] [--get-symbols]
                           [--quota] [--convert CONVERT CONVERT CONVERT]

optional arguments:
  -h, --help            show this help message and exit
  -v, --version         show program's version number and exit
  --filename FILENAME, -f FILENAME
                        Output filename
  --pair PAIRS, -p PAIRS
                        Add repeated values to a list. Currency pair to be
                        returned by API, e.g. EURUSD
  --debug, -d           Turns debug mode of the script
  --market-is-open, -m  Check if the market is open
  --get-symbols, -s     Get the list of available symbols
  --quota, -q           Check your usage / quota limit
  --convert CONVERT CONVERT CONVERT, -c CONVERT CONVERT CONVERT
                        Convert from one currency to another (from_currency,
                        to_currency, from_currency_value)

Usage Samples:                        
python forge_api_script.py -f output.csv -p EURUSD -d
python forge_api_script.py -f output.csv -s -d
python forge_api_script.py -f output.csv -p EURUSD -p GBPJPY -d
python forge_api_script.py -f output.csv -c EUR USD 100 -d                        
python forge_api_script.py -f output.csv -m -d
python forge_api_script.py -f output.csv -q -d
python forge_api_script.py -q
python forge_api_script.py -f output.csv -c EUR USD 100 -q -d

Error checks:
TODO: - incorrect arguments provided
TODO: - invalid output file format
- error response from server
- incorrect response

DISCLAIMER: Do Not Use In Production before being thoroughly tested.
"""

parser = argparse.ArgumentParser(version='1.0')
parser.add_argument('--filename', '-f',
                    help='Output filename')
parser.add_argument('--pair', '-p', action="append", dest="pairs",
                    help='Add repeated values to a list. Currency pair to be returned by API, e.g. EURUSD')
parser.add_argument('--debug', '-d', action='store_true', default=False, dest='debug_switch',
                    help='Turns debug mode of the script')
parser.add_argument('--market-is-open', '-m', action='store_true', default=False, dest='market_switch',
                    help='Check if the market is open')
parser.add_argument('--get-symbols', '-s', action='store_true', default=False, dest='symbols_switch',
                    help='Get the list of available symbols')
parser.add_argument('--quota', '-q', action='store_true', default=False, dest='quota_switch',
                    help='Check your usage / quota limit')
parser.add_argument('--convert', '-c', nargs=3,
                    help='Convert from one currency to another (from_currency, to_currency, from_currency_value)')
# TODO: Add the next arguments for next version v1.1 for authentication management behind proxy
# parser.add_argument('--user', action="store")
# parser.add_argument('--password', action="store")
results = parser.parse_args()
# print(results)


def logged(method):
    """Cause the decorated method to be run and its results logged, along
    with some other diagnostic information.
    """
    @functools.wraps(method)
    def inner(*args, **kwargs):
        # Record our start time.
        start = time.time()

        # Run the decorated method.
        return_value = method(*args, **kwargs)

        if results.debug_switch:
            # Record our completion time, and calculate the delta.
            end = time.time()
            delta = end - start

            # Log the method call and the result.
            logging.basicConfig(level=logging.DEBUG, filename='forge.log', filemode='w')
            logger = logging.getLogger()
            logger.debug('Called method %s at %.02f; execution time %.02f '
                         'seconds; result %r.' %
                         (method.__name__, start, delta, return_value))

        # Return the method's original return value.
        return return_value
    return inner


class JSONOutputError(Exception):
    def __init__(self, message):
        self._message = message

    def __str__(self):
        return self._message


def json_output(decorated_=None, indent=None, sort_keys=False):
    """Run the decorated function, serialize the result of that function
    to JSON, and return the JSON string.
    """
    # Did we get both a decorated method and keyword arguments?
    # That should not happen.
    if decorated_ and (indent or sort_keys):
        raise RuntimeError('Unexpected arguments.')

    # Define the actual decorator function.
    def actual_decorator(func):
        @functools.wraps(func)
        def inner(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
            except JSONOutputError as ex:
                result = {
                    'status': 'error',
                    'message': str(ex),
                }
            return json.dumps(result, indent=indent, sort_keys=sort_keys)
        return inner

    # Return either the actual decorator, or the result of applying
    # the actual decorator, depending on what arguments we got.
    if decorated_:
        return actual_decorator(decorated_)
    else:
        return actual_decorator


class Forge():
    def __init__(self, api_key=None):
        """You can get an API key for free at 1forge.com
        """
        if not api_key:
            self.api_key = Config().FORGE_API_KEY or 'YOUR_API_KEY'
        else:
            self.api_key = api_key
        self.client = python_forex_quotes.ForexDataClient(self.api_key)

    @json_output
    @logged
    def market_is_open(self):
        """Check if the market is open
        """
        if self.client.marketIsOpen():
            return True
        else:
            return False

    @json_output
    @logged
    def get_symbols(self):
        """Get the list of available symbols
        """
        symbols = self.client.getSymbols()
        return symbols

    @json_output
    @logged
    def get_quotes(self, specified_symbols):
        """Get quotes for specified symbols
        """
        quotes = self.client.getQuotes(specified_symbols)
        return quotes

    @json_output
    @logged
    def quota(self):
        """Check your usage / quota limit
        """
        quota = self.client.quota()
        return quota

    @json_output
    @logged
    def convert(self, from_currency, to_currency, from_currency_value):
        """"Convert from one currency to another
        """
        conversion = self.client.convert(from_currency, to_currency, from_currency_value)
        return conversion

    @logged
    def write_to_file(self, output_string=None):
        """Write down to an output file
        """
        if results.filename:
            with open(results.filename, 'a') as my_file:
                my_file.write(output_string + '\n')
        else:
            print(output_string)


def main():
    forge = Forge()
    # sys.exit()

    if results.market_switch:
        if forge.market_is_open():
            # print("Market is open!")
            output_string = "Market is open!"
        else:
            # print("Market is closed!")
            output_string = "Market is closed!"
        forge.write_to_file(output_string)

    if results.symbols_switch:
        symbols = forge.get_symbols()
        # print(symbols)
        output_string = symbols
        forge.write_to_file(output_string)

    if results.pairs:
        # specified_symbols = ['EURUSD', 'GBPJPY']
        specified_symbols = results.pairs
        quotes = forge.get_quotes(specified_symbols)
        # print(quotes)
        output_string = quotes
        forge.write_to_file(output_string)

    if results.quota_switch:
        quota = forge.quota()
        # print(quota)
        output_string = quota
        forge.write_to_file(output_string)

    if results.convert:
        from_currency = results.convert[0]
        to_currency = results.convert[1]
        from_currency_value = float(results.convert[2])
        # from_currency = 'EUR'
        # to_currency = 'USD'
        # from_currency_value = 100
        conversion = forge.convert(from_currency, to_currency, from_currency_value)
        # print(conversion)
        output_string = conversion
        forge.write_to_file(output_string)


if __name__ == '__main__':
    main()
