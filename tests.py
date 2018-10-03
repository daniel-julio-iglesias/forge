#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function
from datetime import datetime, timedelta
import unittest
from forge_api_script import Forge

""""python tests.py
python forge_api_script.py -f output.csv -p EURUSD -d
python forge_api_script.py -f output.csv -s -d
python forge_api_script.py -f output.csv -p EURUSD -p GBPJPY -d
python forge_api_script.py -f output.csv -c EUR USD 100 -d                        
python forge_api_script.py -f output.csv -m -d
python forge_api_script.py -f output.csv -q -d
python forge_api_script.py -f output.csv -c EUR USD 100 -q -d
"""


class ForgeTests(unittest.TestCase):
    def test_market_is_open(self):
        forge = Forge()
        if forge.market_is_open():
            # print("Market is open!")
            output_string = "Market is open!"
        else:
            # print("Market is closed!")
            output_string = "Market is closed!"
        self.assertEqual(output_string, "Market is open!")

    def test_get_symbols(self):
        forge = Forge()
        symbols = forge.get_symbols()
        # print(symbols)
        output_string = symbols
        self.assertEqual(output_string, '["EURHKD", "EURCNH", "EURDKK", "EURMXN", "EURPLN", "EURXAG", "EURXAU", "EURBTC", "EURETH", "EURLTC", "EURXRP", "EURDSH", "EURBCH", "USDEUR", "USDGBP", "USDAUD", "USDNZD", "USDXAG", "USDXAU", "USDBTC", "USDETH", "USDLTC", "USDXRP", "USDDSH", "USDBCH", "JPYEUR", "JPYUSD", "JPYGBP", "JPYCAD", "JPYCHF", "JPYAUD", "JPYNZD", "JPYSGD", "JPYNOK", "JPYRUB", "JPYSEK", "JPYTRY", "JPYZAR", "JPYHKD", "JPYCNH", "JPYDKK", "JPYMXN", "JPYPLN", "JPYXAG", "JPYXAU", "JPYBTC", "JPYETH", "JPYLTC", "JPYXRP", "JPYDSH", "JPYBCH", "GBPEUR", "GBPRUB", "GBPTRY", "GBPZAR", "GBPCNH", "GBPDKK", "GBPMXN", "GBPPLN", "GBPXAG", "GBPXAU", "GBPBTC", "GBPETH", "GBPLTC", "GBPXRP", "GBPDSH", "GBPBCH", "CADEUR", "CADUSD", "CADGBP", "CADAUD", "CADNZD", "CADSGD", "CADNOK", "CADRUB", "CADSEK", "CADTRY", "CADZAR", "CADHKD", "CADCNH", "CADDKK", "CADMXN", "CADPLN", "CADXAG", "CADXAU", "CADBTC", "CADETH", "CADLTC", "CADXRP", "CADDSH", "CADBCH", "CHFEUR", "CHFUSD", "CHFGBP", "CHFCAD", "CHFAUD", "CHFNZD", "CHFNOK", "CHFRUB", "CHFSEK", "CHFTRY", "CHFZAR", "CHFHKD", "CHFCNH", "CHFDKK", "CHFMXN", "CHFPLN", "CHFXAG", "CHFXAU", "CHFBTC", "CHFETH", "CHFLTC", "CHFXRP", "CHFDSH", "CHFBCH", "AUDEUR", "AUDGBP", "AUDNOK", "AUDRUB", "AUDSEK", "AUDTRY", "AUDZAR", "AUDHKD", "AUDCNH", "AUDDKK", "AUDMXN", "AUDPLN", "AUDXAG", "AUDXAU", "AUDBTC", "AUDETH", "AUDLTC", "AUDXRP", "AUDDSH", "AUDBCH", "NZDEUR", "NZDGBP", "NZDAUD", "NZDSGD", "NZDNOK", "NZDRUB", "NZDSEK", "NZDTRY", "NZDZAR", "NZDHKD", "NZDCNH", "NZDDKK", "NZDMXN", "NZDPLN", "NZDXAG", "NZDXAU", "NZDBTC", "NZDETH", "NZDLTC", "NZDXRP", "NZDDSH", "NZDBCH", "SGDEUR", "SGDUSD", "SGDGBP", "SGDCAD", "SGDCHF", "SGDAUD", "SGDNZD", "SGDNOK", "SGDRUB", "SGDSEK", "SGDTRY", "SGDZAR", "SGDHKD", "SGDCNH", "SGDDKK", "SGDMXN", "SGDPLN", "SGDXAG", "SGDXAU", "SGDBTC", "SGDETH", "SGDLTC", "SGDXRP", "SGDDSH", "SGDBCH", "NOKEUR", "NOKUSD", "NOKGBP", "NOKCAD", "NOKCHF", "NOKAUD", "NOKNZD", "NOKSGD", "NOKRUB", "NOKSEK", "NOKTRY", "NOKZAR", "NOKHKD", "NOKCNH", "NOKDKK", "NOKMXN", "NOKPLN", "NOKXAG", "NOKXAU", "NOKBTC", "NOKETH", "NOKLTC", "NOKXRP", "NOKDSH", "NOKBCH", "RUBEUR", "RUBUSD", "RUBJPY", "RUBGBP", "RUBCAD", "RUBCHF", "RUBAUD", "RUBNZD", "RUBSGD", "RUBNOK", "RUBSEK", "RUBTRY", "RUBZAR", "RUBHKD", "RUBCNH", "RUBDKK", "RUBMXN", "RUBPLN", "RUBXAG", "RUBXAU", "RUBBTC", "RUBETH", "RUBLTC", "RUBXRP", "RUBDSH", "RUBBCH", "SEKEUR", "SEKUSD", "SEKJPY", "SEKGBP", "SEKCAD", "SEKCHF", "SEKAUD", "SEKNZD", "SEKSGD", "SEKNOK", "SEKRUB", "SEKTRY", "SEKZAR", "SEKHKD", "SEKCNH", "SEKDKK", "SEKMXN", "SEKPLN", "SEKXAG", "SEKXAU", "SEKBTC", "SEKETH", "SEKLTC", "SEKXRP", "SEKDSH", "SEKBCH", "TRYEUR", "TRYUSD", "TRYJPY", "TRYGBP", "TRYCAD", "TRYCHF", "TRYAUD", "TRYNZD", "TRYSGD", "TRYNOK", "TRYRUB", "TRYSEK", "TRYZAR", "TRYHKD", "TRYCNH", "TRYDKK", "TRYMXN", "TRYPLN", "TRYXAG", "TRYXAU", "TRYBTC", "TRYETH", "TRYLTC", "TRYXRP", "TRYDSH", "TRYBCH", "ZAREUR", "ZARUSD", "ZARJPY", "ZARGBP", "ZARCAD", "ZARCHF", "ZARAUD", "ZARNZD", "ZARSGD", "ZARNOK", "ZARRUB", "ZARSEK", "ZARTRY", "ZARHKD", "ZARCNH", "ZARDKK", "ZARMXN", "ZARPLN", "ZARXAG", "ZARXAU", "ZARBTC", "ZARETH", "ZARLTC", "ZARXRP", "ZARDSH", "ZARBCH", "HKDEUR", "HKDUSD", "HKDJPY", "HKDGBP", "HKDCAD", "HKDCHF", "HKDAUD", "HKDNZD", "HKDSGD", "HKDNOK", "HKDRUB", "HKDSEK", "HKDTRY", "HKDZAR", "HKDCNH", "HKDDKK", "HKDMXN", "HKDPLN", "HKDXAG", "HKDXAU", "HKDBTC", "HKDETH", "HKDLTC", "HKDXRP", "HKDDSH", "HKDBCH", "CNHEUR", "CNHUSD", "CNHJPY", "CNHGBP", "CNHCAD", "CNHCHF", "CNHAUD", "CNHNZD", "CNHSGD", "CNHNOK", "CNHRUB", "CNHSEK", "CNHTRY", "CNHZAR", "CNHHKD", "CNHDKK", "CNHMXN", "CNHPLN", "CNHXAG", "CNHXAU", "CNHBTC", "CNHETH", "CNHLTC", "CNHXRP", "CNHDSH", "CNHBCH", "DKKEUR", "DKKUSD", "DKKJPY", "DKKGBP", "DKKCAD", "DKKCHF", "DKKAUD", "DKKNZD", "DKKSGD", "DKKNOK", "DKKRUB", "DKKSEK", "DKKTRY", "DKKZAR", "DKKHKD", "DKKCNH", "DKKMXN", "DKKPLN", "DKKXAG", "DKKXAU", "DKKBTC", "DKKETH", "DKKLTC", "DKKXRP", "DKKDSH", "DKKBCH", "MXNEUR", "MXNUSD", "MXNJPY", "MXNGBP", "MXNCAD", "MXNCHF", "MXNAUD", "MXNNZD", "MXNSGD", "MXNNOK", "MXNRUB", "MXNSEK", "MXNTRY", "MXNZAR", "MXNHKD", "MXNCNH", "MXNDKK", "MXNPLN", "MXNXAG", "MXNXAU", "MXNBTC", "MXNETH", "MXNLTC", "MXNXRP", "MXNDSH", "MXNBCH", "PLNEUR", "PLNUSD", "PLNJPY", "PLNGBP", "PLNCAD", "PLNCHF", "PLNAUD", "PLNNZD", "PLNSGD", "PLNNOK", "PLNRUB", "PLNSEK", "PLNTRY", "PLNZAR", "PLNHKD", "PLNCNH", "PLNDKK", "PLNMXN", "PLNXAG", "PLNXAU", "PLNBTC", "PLNETH", "PLNLTC", "PLNXRP", "PLNDSH", "PLNBCH", "XAGJPY", "XAGGBP", "XAGCAD", "XAGCHF", "XAGAUD", "XAGNZD", "XAGSGD", "XAGNOK", "XAGRUB", "XAGSEK", "XAGTRY", "XAGZAR", "XAGHKD", "XAGCNH", "XAGDKK", "XAGMXN", "XAGPLN", "XAGXAU", "XAGBTC", "XAGETH", "XAGLTC", "XAGXRP", "XAGDSH", "XAGBCH", "XAUEUR", "XAUJPY", "XAUGBP", "XAUCAD", "XAUCHF", "XAUAUD", "XAUNZD", "XAUSGD", "XAUNOK", "XAURUB", "XAUSEK", "XAUTRY", "XAUZAR", "XAUHKD", "XAUCNH", "XAUDKK", "XAUMXN", "XAUPLN", "XAUXAG", "XAUBTC", "XAUETH", "XAULTC", "XAUXRP", "XAUDSH", "XAUBCH", "BTCEUR", "BTCJPY", "BTCGBP", "BTCCAD", "BTCCHF", "BTCAUD", "BTCNZD", "BTCSGD", "BTCNOK", "BTCRUB", "BTCSEK", "BTCTRY", "BTCZAR", "BTCHKD", "BTCCNH", "BTCDKK", "BTCMXN", "BTCPLN", "BTCXAG", "BTCXAU", "BTCETH", "BTCLTC", "BTCXRP", "BTCDSH", "BTCBCH", "ETHEUR", "ETHJPY", "ETHGBP", "ETHCAD", "ETHCHF", "ETHAUD", "ETHNZD", "ETHSGD", "ETHNOK", "ETHRUB", "ETHSEK", "ETHTRY", "ETHZAR", "ETHHKD", "ETHCNH", "ETHDKK", "ETHMXN", "ETHPLN", "ETHXAG", "ETHXAU", "ETHLTC", "ETHXRP", "ETHDSH", "ETHBCH", "LTCEUR", "LTCJPY", "LTCGBP", "LTCCAD", "LTCCHF", "LTCAUD", "LTCNZD", "LTCSGD", "LTCNOK", "LTCRUB", "LTCSEK", "LTCTRY", "LTCZAR", "LTCHKD", "LTCCNH", "LTCDKK", "LTCMXN", "LTCPLN", "LTCXAG", "LTCXAU", "LTCETH", "LTCXRP", "LTCDSH", "LTCBCH", "XRPEUR", "XRPJPY", "XRPGBP", "XRPCAD", "XRPCHF", "XRPAUD", "XRPNZD", "XRPSGD", "XRPNOK", "XRPRUB", "XRPSEK", "XRPTRY", "XRPZAR", "XRPHKD", "XRPCNH", "XRPDKK", "XRPMXN", "XRPPLN", "XRPXAG", "XRPXAU", "XRPETH", "XRPLTC", "XRPDSH", "XRPBCH", "DSHEUR", "DSHJPY", "DSHGBP", "DSHCAD", "DSHCHF", "DSHAUD", "DSHNZD", "DSHSGD", "DSHNOK", "DSHRUB", "DSHSEK", "DSHTRY", "DSHZAR", "DSHHKD", "DSHCNH", "DSHDKK", "DSHMXN", "DSHPLN", "DSHXAG", "DSHXAU", "DSHETH", "DSHLTC", "DSHXRP", "DSHBCH", "BCHEUR", "BCHJPY", "BCHGBP", "BCHCAD", "BCHCHF", "BCHAUD", "BCHNZD", "BCHSGD", "BCHNOK", "BCHRUB", "BCHSEK", "BCHTRY", "BCHZAR", "BCHHKD", "BCHCNH", "BCHDKK", "BCHMXN", "BCHPLN", "BCHXAG", "BCHXAU", "BCHETH", "BCHLTC", "BCHXRP", "BCHDSH", "EURUSD", "USDJPY", "GBPUSD", "USDCAD", "USDCHF", "AUDUSD", "NZDUSD", "EURGBP", "EURCHF", "EURCAD", "EURAUD", "EURNZD", "EURJPY", "GBPJPY", "CHFJPY", "CADJPY", "AUDJPY", "NZDJPY", "GBPCHF", "GBPAUD", "GBPCAD", "GBPNZD", "AUDCAD", "AUDCHF", "AUDNZD", "CADCHF", "AUDSGD", "CHFSGD", "EURNOK", "EURRUB", "EURSEK", "EURSGD", "EURTRY", "EURZAR", "GBPHKD", "GBPNOK", "GBPSEK", "GBPSGD", "NOKJPY", "NZDCAD", "NZDCHF", "SGDJPY", "USDCNH", "USDDKK", "USDHKD", "USDMXN", "USDNOK", "USDPLN", "USDRUB", "USDSEK", "USDSGD", "USDTRY", "USDZAR", "XAGEUR", "XAGUSD", "XAUUSD", "BTCUSD", "ETHBTC", "ETHUSD", "LTCBTC", "LTCUSD", "XRPUSD", "XRPBTC", "DSHUSD", "DSHBTC", "BCHUSD", "BCHBTC"]')

    def test_get_quotes(self):
        forge = Forge()
        specified_symbols = ['EURUSD', 'GBPJPY']
        quotes = forge.get_quotes(specified_symbols)
        # print(quotes)
        output_string = quotes
        self.assertNotEqual(output_string, '[{"ask": 1.15113, "timestamp": 1538593632, "symbol": "EURUSD", "price": 1.15112, "bid": 1.15111}, {"ask": 148.351, "timestamp": 1538593632, "symbol": "GBPJPY", "price": 148.3485, "bid": 148.346}]')

    def test_get_quota(self):
        forge = Forge()
        quota = forge.quota()
        output_string = quota
        self.assertNotEqual(output_string, '{"hours_until_reset": 9, "quota_used": 45, "quota_remaining": 951, "quota_limit": 1000}')

    def test_convert(self):
        forge = Forge()
        from_currency = 'EUR'
        to_currency = 'USD'
        from_currency_value = 100
        conversion = forge.convert(from_currency, to_currency, from_currency_value)
        output_string = conversion
        self.assertNotEqual(output_string, """{"text": "100 EUR is worth 115.152 USD", "value": 115.152, "timestamp": 1538595009}""")


if __name__ == '__main__':
    unittest.main(verbosity=2)
