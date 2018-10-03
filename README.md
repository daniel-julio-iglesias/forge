# myforge

This is my personal working repository.
For original repository see at 

https://1forge.com/forex-data-api/api-documentation

and 

https://github.com/1Forge/python-forex-quotes



# python_forex_quotes

python_forex_quotes is a Python Library for fetching realtime forex quotes

# Table of Contents

- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
    - [List of Symbols available](#get-the-list-of-available-symbols)
    - [Get quotes for specific symbols](#get-quotes-for-specified-symbols)
    - [Convert from one currency to another](#convert-from-one-currency-to-another)
- [Contributing](#contributing)
- [Support / Contact](#support-and-contact)
- [License / Terms](#license-and-terms)

## Requirements
* Python 2.7.*
* An API key which you can obtain for free at http://1forge.com/forex-data-api

## Installation
```
$ git clone https://github.com/daniel-julio-iglesias/forge.git
or
$ mkdir forge
and copy provided files into forge folder

$ cd forge

Install the virtual environment
and activate it

(venv) $ pip install python_forex_quotes

Edit the config.py file:

- Set the FORGE_API_KEY environment variable in your operating system, or
write down the value for YOUR_API_KEY (not recommended for sharing)
You can get an API key for free at 1forge.com

self.FORGE_API_KEY = os.environ.get('FORGE_API_KEY') or 'YOUR_API_KEY'

- If behind a proxy uncomment and adapt the next lines

# os.environ['http_proxy'] = 'http://username:password@Proxyadresse:Proxyport'
# os.environ['https_proxy'] = 'https://username:password@Proxyadresse:Proxyport'
```

## Usage
```
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
```

### Usage Sample
```
# Running the next command results in sending request to the following endpoint 
# https://forex.1forge.com/1.0.3/quotes?pairs=EURUSD with pairs=EURUSD as query argument
# and saving output data to output.csv file.
# https://forex.1forge.com/1.0.3/quotes?pairs=EURUSD
# --debug turns debug mode of the script
 
python forge_api_script.py -f output.csv -p EURUSD -d

# Other Usage Samples
# Get quota and conversion
python forge_api_script.py -f output.csv -c EUR USD 100 -q -d
# Get quota
python forge_api_script.py -q
```

### Get the list of available symbols:

```
python forge_api_script.py -f output.csv -s -d
```

### Get quotes for specified symbols:
```
python forge_api_script.py -f output.csv -p EURUSD -p GBPJPY -d
```

### Convert from one currency to another:
```
python forge_api_script.py -f output.csv -c EUR USD 100 -d
```

### Check if the market is open:
```
python forge_api_script.py -f output.csv -m -d
```

### Check your usage / quota limit:
```
python forge_api_script.py -f output.csv -q -d
```


## Support and Contact
This is a copy of the original python_forex_quotes

For any contact, please navigate to the original 
python_forex_quotes repository version - 

https://github.com/1Forge/python-forex-quotes


## License and Terms
This library is provided without warranty under the MIT license.
