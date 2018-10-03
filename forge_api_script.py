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

""""Python API script: forge

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

python forge_api_script.py output.csv pair=EURUSD --debug
python forge_api_script.py -h
pforge_api_script.py [-h] [-v] [--filename FILENAME] [--pair PAIRS]
                           [--debug]
python forge_api_script.py --filename output.csv --pair EURUSD --pair GBPJPY --pair AUDUSD --debug
"""

parser = argparse.ArgumentParser(version='1.0')

parser.add_argument('--filename',
                    help='Output filename')
parser.add_argument('--pair', action="append", dest="pairs",
                    help='Add repeated values to a list. Currency pair to be returned by API, e.g. EURUSD')
parser.add_argument('--debug', action='store_true', default=False, dest='debug_switch',
                    help='Turns debug mode of the script')

results = parser.parse_args()
print(results)


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
        # self.client = None

    def instantiate_the_client(self):
        """Instantiate the client
        """
        self.client = python_forex_quotes.ForexDataClient(self.api_key)
        # return self.client

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
        """Create an output file
        """
        if results.filename:
            with open(results.filename, 'w') as my_file:
                my_file.write(output_string)
        else:
            print(output_string)


def main():
    forge = Forge()
    # forge = Forge().instantiate_the_client()
    # forge = Forge('YOUR_API_KEY')
    # print("api_key: {}".format(forge.api_key))
    # sys.exit()
    # print("forge {}".format(forge))
    # print(forge)
    # sys.exit()

    if forge.market_is_open():
        print("Market is open!")
    else:
        print("Market is closed!")

    print(forge.get_symbols())

    if results.pairs:
        # specified_symbols = ['EURUSD', 'GBPJPY']
        specified_symbols = results.pairs
        quotes = forge.get_quotes(specified_symbols)
        # print(quotes)
        output_string = quotes
        forge.write_to_file(output_string=output_string)

    quota = forge.quota()
    print(quota)

    from_currency = 'EUR'
    to_currency = 'USD'
    from_currency_value = 100
    conversion = forge.convert(from_currency, to_currency, from_currency_value)
    print(conversion)


if __name__ == '__main__':
    main()
