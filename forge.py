#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function
import python_forex_quotes
from config import Config
import sys

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

$python forge.py
api_key: YOUR_API_KEY

Market is open!

[u'EURHKD', u'EURCNH', u'EURDKK', u'EURMXN', u'EURPLN', u'EURXAG', u'EURXAU', u'EURBTC', u'EURETH', u'EURLTC', u'EURXRP', u'EURDSH', u'EURBCH', u'USDEUR', u'USDGBP', u'USDAUD', u'USDNZD', u'USDXAG', u'USDXAU', u'USDBTC', u'USDETH', u'USDLTC', u'USDXRP', u'USDDSH', u'USDBCH', u'JPYEUR', u'JPYUSD', u'JPYGBP', u'JPYCAD', u'JPYCHF', u'JPYAUD', u'JPYNZD', u'JPYSGD', u'JPYNOK', u'JPYRUB', u'JPYSEK', u'JPYTRY', u'JPYZAR', u'JPYHKD', u'JPYCNH', u'JPYDKK', u'JPYMXN', u'JPYPLN', u'JPYXAG', u'JPYXAU', u'JPYBTC', u'JPYETH', u'JPYLTC', u'JPYXRP', u'JPYDSH', u'JPYBCH', u'GBPEUR', u'GBPRUB', u'GBPTRY', u'GBPZAR', u'GBPCNH', u'GBPDKK', u'GBPMXN', u'GBPPLN', u'GBPXAG', u'GBPXAU', u'GBPBTC', u'GBPETH', u'GBPLTC', u'GBPXRP', u'GBPDSH', u'GBPBCH', u'CADEUR', u'CADUSD', u'CADGBP', u'CADAUD', u'CADNZD', u'CADSGD', u'CADNOK', u'CADRUB', u'CADSEK', u'CADTRY', u'CADZAR', u'CADHKD', u'CADCNH', u'CADDKK', u'CADMXN', u'CADPLN', u'CADXAG', u'CADXAU', u'CADBTC', u'CADETH', u'CADLTC', u'CADXRP', u'CADDSH', u'CADBCH', u'CHFEUR', u'CHFUSD', u'CHFGBP', u'CHFCAD', u'CHFAUD', u'CHFNZD', u'CHFNOK', u'CHFRUB', u'CHFSEK', u'CHFTRY', u'CHFZAR', u'CHFHKD', u'CHFCNH', u'CHFDKK', u'CHFMXN', u'CHFPLN', u'CHFXAG', u'CHFXAU', u'CHFBTC', u'CHFETH', u'CHFLTC', u'CHFXRP', u'CHFDSH', u'CHFBCH', u'AUDEUR', u'AUDGBP', u'AUDNOK', u'AUDRUB', u'AUDSEK', u'AUDTRY', u'AUDZAR', u'AUDHKD', u'AUDCNH', u'AUDDKK', u'AUDMXN', u'AUDPLN', u'AUDXAG', u'AUDXAU', u'AUDBTC', u'AUDETH', u'AUDLTC', u'AUDXRP', u'AUDDSH', u'AUDBCH', u'NZDEUR', u'NZDGBP', u'NZDAUD', u'NZDSGD', u'NZDNOK', u'NZDRUB', u'NZDSEK', u'NZDTRY', u'NZDZAR', u'NZDHKD', u'NZDCNH', u'NZDDKK', u'NZDMXN', u'NZDPLN', u'NZDXAG', u'NZDXAU', u'NZDBTC', u'NZDETH', u'NZDLTC', u'NZDXRP', u'NZDDSH', u'NZDBCH', u'SGDEUR', u'SGDUSD', u'SGDGBP', u'SGDCAD', u'SGDCHF', u'SGDAUD', u'SGDNZD', u'SGDNOK', u'SGDRUB', u'SGDSEK', u'SGDTRY', u'SGDZAR', u'SGDHKD', u'SGDCNH', u'SGDDKK', u'SGDMXN', u'SGDPLN', u'SGDXAG', u'SGDXAU', u'SGDBTC', u'SGDETH', u'SGDLTC', u'SGDXRP', u'SGDDSH', u'SGDBCH', u'NOKEUR', u'NOKUSD', u'NOKGBP', u'NOKCAD', u'NOKCHF', u'NOKAUD', u'NOKNZD', u'NOKSGD', u'NOKRUB', u'NOKSEK', u'NOKTRY', u'NOKZAR', u'NOKHKD', u'NOKCNH', u'NOKDKK', u'NOKMXN', u'NOKPLN', u'NOKXAG', u'NOKXAU', u'NOKBTC', u'NOKETH', u'NOKLTC', u'NOKXRP', u'NOKDSH', u'NOKBCH', u'RUBEUR', u'RUBUSD', u'RUBJPY', u'RUBGBP', u'RUBCAD', u'RUBCHF', u'RUBAUD', u'RUBNZD', u'RUBSGD', u'RUBNOK', u'RUBSEK', u'RUBTRY', u'RUBZAR', u'RUBHKD', u'RUBCNH', u'RUBDKK', u'RUBMXN', u'RUBPLN', u'RUBXAG', u'RUBXAU', u'RUBBTC', u'RUBETH', u'RUBLTC', u'RUBXRP', u'RUBDSH', u'RUBBCH', u'SEKEUR', u'SEKUSD', u'SEKJPY', u'SEKGBP', u'SEKCAD', u'SEKCHF', u'SEKAUD', u'SEKNZD', u'SEKSGD', u'SEKNOK', u'SEKRUB', u'SEKTRY', u'SEKZAR', u'SEKHKD', u'SEKCNH', u'SEKDKK', u'SEKMXN', u'SEKPLN', u'SEKXAG', u'SEKXAU', u'SEKBTC', u'SEKETH', u'SEKLTC', u'SEKXRP', u'SEKDSH', u'SEKBCH', u'TRYEUR', u'TRYUSD', u'TRYJPY', u'TRYGBP', u'TRYCAD', u'TRYCHF', u'TRYAUD', u'TRYNZD', u'TRYSGD', u'TRYNOK', u'TRYRUB', u'TRYSEK', u'TRYZAR', u'TRYHKD', u'TRYCNH', u'TRYDKK', u'TRYMXN', u'TRYPLN', u'TRYXAG', u'TRYXAU', u'TRYBTC', u'TRYETH', u'TRYLTC', u'TRYXRP', u'TRYDSH', u'TRYBCH', u'ZAREUR', u'ZARUSD', u'ZARJPY', u'ZARGBP', u'ZARCAD', u'ZARCHF', u'ZARAUD', u'ZARNZD', u'ZARSGD', u'ZARNOK', u'ZARRUB', u'ZARSEK', u'ZARTRY', u'ZARHKD', u'ZARCNH', u'ZARDKK', u'ZARMXN', u'ZARPLN', u'ZARXAG', u'ZARXAU', u'ZARBTC', u'ZARETH', u'ZARLTC', u'ZARXRP', u'ZARDSH', u'ZARBCH', u'HKDEUR', u'HKDUSD', u'HKDJPY', u'HKDGBP', u'HKDCAD', u'HKDCHF', u'HKDAUD', u'HKDNZD', u'HKDSGD', u'HKDNOK', u'HKDRUB', u'HKDSEK', u'HKDTRY', u'HKDZAR', u'HKDCNH', u'HKDDKK', u'HKDMXN', u'HKDPLN', u'HKDXAG', u'HKDXAU', u'HKDBTC', u'HKDETH', u'HKDLTC', u'HKDXRP', u'HKDDSH', u'HKDBCH', u'CNHEUR', u'CNHUSD', u'CNHJPY', u'CNHGBP', u'CNHCAD', u'CNHCHF', u'CNHAUD', u'CNHNZD', u'CNHSGD', u'CNHNOK', u'CNHRUB', u'CNHSEK', u'CNHTRY', u'CNHZAR', u'CNHHKD', u'CNHDKK', u'CNHMXN', u'CNHPLN', u'CNHXAG', u'CNHXAU', u'CNHBTC', u'CNHETH', u'CNHLTC', u'CNHXRP', u'CNHDSH', u'CNHBCH', u'DKKEUR', u'DKKUSD', u'DKKJPY', u'DKKGBP', u'DKKCAD', u'DKKCHF', u'DKKAUD', u'DKKNZD', u'DKKSGD', u'DKKNOK', u'DKKRUB', u'DKKSEK', u'DKKTRY', u'DKKZAR', u'DKKHKD', u'DKKCNH', u'DKKMXN', u'DKKPLN', u'DKKXAG', u'DKKXAU', u'DKKBTC', u'DKKETH', u'DKKLTC', u'DKKXRP', u'DKKDSH', u'DKKBCH', u'MXNEUR', u'MXNUSD', u'MXNJPY', u'MXNGBP', u'MXNCAD', u'MXNCHF', u'MXNAUD', u'MXNNZD', u'MXNSGD', u'MXNNOK', u'MXNRUB', u'MXNSEK', u'MXNTRY', u'MXNZAR', u'MXNHKD', u'MXNCNH', u'MXNDKK', u'MXNPLN', u'MXNXAG', u'MXNXAU', u'MXNBTC', u'MXNETH', u'MXNLTC', u'MXNXRP', u'MXNDSH', u'MXNBCH', u'PLNEUR', u'PLNUSD', u'PLNJPY', u'PLNGBP', u'PLNCAD', u'PLNCHF', u'PLNAUD', u'PLNNZD', u'PLNSGD', u'PLNNOK', u'PLNRUB', u'PLNSEK', u'PLNTRY', u'PLNZAR', u'PLNHKD', u'PLNCNH', u'PLNDKK', u'PLNMXN', u'PLNXAG', u'PLNXAU', u'PLNBTC', u'PLNETH', u'PLNLTC', u'PLNXRP', u'PLNDSH', u'PLNBCH', u'XAGJPY', u'XAGGBP', u'XAGCAD', u'XAGCHF', u'XAGAUD', u'XAGNZD', u'XAGSGD', u'XAGNOK', u'XAGRUB', u'XAGSEK', u'XAGTRY', u'XAGZAR', u'XAGHKD', u'XAGCNH', u'XAGDKK', u'XAGMXN', u'XAGPLN', u'XAGXAU', u'XAGBTC', u'XAGETH', u'XAGLTC', u'XAGXRP', u'XAGDSH', u'XAGBCH', u'XAUEUR', u'XAUJPY', u'XAUGBP', u'XAUCAD', u'XAUCHF', u'XAUAUD', u'XAUNZD', u'XAUSGD', u'XAUNOK', u'XAURUB', u'XAUSEK', u'XAUTRY', u'XAUZAR', u'XAUHKD', u'XAUCNH', u'XAUDKK', u'XAUMXN', u'XAUPLN', u'XAUXAG', u'XAUBTC', u'XAUETH', u'XAULTC', u'XAUXRP', u'XAUDSH', u'XAUBCH', u'BTCEUR', u'BTCJPY', u'BTCGBP', u'BTCCAD', u'BTCCHF', u'BTCAUD', u'BTCNZD', u'BTCSGD', u'BTCNOK', u'BTCRUB', u'BTCSEK', u'BTCTRY', u'BTCZAR', u'BTCHKD', u'BTCCNH', u'BTCDKK', u'BTCMXN', u'BTCPLN', u'BTCXAG', u'BTCXAU', u'BTCETH', u'BTCLTC', u'BTCXRP', u'BTCDSH', u'BTCBCH', u'ETHEUR', u'ETHJPY', u'ETHGBP', u'ETHCAD', u'ETHCHF', u'ETHAUD', u'ETHNZD', u'ETHSGD', u'ETHNOK', u'ETHRUB', u'ETHSEK', u'ETHTRY', u'ETHZAR', u'ETHHKD', u'ETHCNH', u'ETHDKK', u'ETHMXN', u'ETHPLN', u'ETHXAG', u'ETHXAU', u'ETHLTC', u'ETHXRP', u'ETHDSH', u'ETHBCH', u'LTCEUR', u'LTCJPY', u'LTCGBP', u'LTCCAD', u'LTCCHF', u'LTCAUD', u'LTCNZD', u'LTCSGD', u'LTCNOK', u'LTCRUB', u'LTCSEK', u'LTCTRY', u'LTCZAR', u'LTCHKD', u'LTCCNH', u'LTCDKK', u'LTCMXN', u'LTCPLN', u'LTCXAG', u'LTCXAU', u'LTCETH', u'LTCXRP', u'LTCDSH', u'LTCBCH', u'XRPEUR', u'XRPJPY', u'XRPGBP', u'XRPCAD', u'XRPCHF', u'XRPAUD', u'XRPNZD', u'XRPSGD', u'XRPNOK', u'XRPRUB', u'XRPSEK', u'XRPTRY', u'XRPZAR', u'XRPHKD', u'XRPCNH', u'XRPDKK', u'XRPMXN', u'XRPPLN', u'XRPXAG', u'XRPXAU', u'XRPETH', u'XRPLTC', u'XRPDSH', u'XRPBCH', u'DSHEUR', u'DSHJPY', u'DSHGBP', u'DSHCAD', u'DSHCHF', u'DSHAUD', u'DSHNZD', u'DSHSGD', u'DSHNOK', u'DSHRUB', u'DSHSEK', u'DSHTRY', u'DSHZAR', u'DSHHKD', u'DSHCNH', u'DSHDKK', u'DSHMXN', u'DSHPLN', u'DSHXAG', u'DSHXAU', u'DSHETH', u'DSHLTC', u'DSHXRP', u'DSHBCH', u'BCHEUR', u'BCHJPY', u'BCHGBP', u'BCHCAD', u'BCHCHF', u'BCHAUD', u'BCHNZD', u'BCHSGD', u'BCHNOK', u'BCHRUB', u'BCHSEK', u'BCHTRY', u'BCHZAR', u'BCHHKD', u'BCHCNH', u'BCHDKK', u'BCHMXN', u'BCHPLN', u'BCHXAG', u'BCHXAU', u'BCHETH', u'BCHLTC', u'BCHXRP', u'BCHDSH', u'EURUSD', u'USDJPY', u'GBPUSD', u'USDCAD', u'USDCHF', u'AUDUSD', u'NZDUSD', u'EURGBP', u'EURCHF', u'EURCAD', u'EURAUD', u'EURNZD', u'EURJPY', u'GBPJPY', u'CHFJPY', u'CADJPY', u'AUDJPY', u'NZDJPY', u'GBPCHF', u'GBPAUD', u'GBPCAD', u'GBPNZD', u'AUDCAD', u'AUDCHF', u'AUDNZD', u'CADCHF', u'AUDSGD', u'CHFSGD', u'EURNOK', u'EURRUB', u'EURSEK', u'EURSGD', u'EURTRY', u'EURZAR', u'GBPHKD', u'GBPNOK', u'GBPSEK', u'GBPSGD', u'NOKJPY', u'NZDCAD', u'NZDCHF', u'SGDJPY', u'USDCNH', u'USDDKK', u'USDHKD', u'USDMXN', u'USDNOK', u'USDPLN', u'USDRUB', u'USDSEK', u'USDSGD', u'USDTRY', u'USDZAR', u'XAGEUR', u'XAGUSD', u'XAUUSD', u'BTCUSD', u'ETHBTC', u'ETHUSD', u'LTCBTC', u'LTCUSD', u'XRPUSD', u'XRPBTC', u'DSHUSD', u'DSHBTC', u'BCHUSD', u'BCHBTC']

[{u'ask': 1.15791, u'timestamp': 1538427545, u'symbol': u'EURUSD', u'price': 1.15786, u'bid': 1.15781}, 
{u'ask': 148.657, u'timestamp': 1538427545, u'symbol': u'GBPJPY', u'price': 148.6395, u'bid': 148.622}]

{u'hours_until_reset': 8, u'quota_used': 4, u'quota_remaining': 996, u'quota_limit': 1000}

{u'text': u'100 EUR is worth 115.786 USD', u'value': 115.786, u'timestamp': 1538427545}

Process finished with exit code 0
"""


class Forge:
    def __init__(self, api_key=None):
        # You can get an API key for free at 1forge.com
        if not api_key:
            self.api_key = Config().SECRET_KEY or 'YOUR_API_KEY'
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
    # forge = Forge('YOUR_API_KEY')
    # print("api_key: {}".format(forge.api_key))
    # sys.exit()

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
