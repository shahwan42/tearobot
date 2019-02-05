import requests
import os
import sys


def crypto_price(coin_symbol):
    '''cryptocurrency price for ``coin_symbol'''
    api_key = os.environ.get('CRYPTOCOMPARE_API_KEY')
    if not api_key:
        sys.stderr.write('Please provide CryptoCompare api key.')
    response = requests.get('https://min-api.cryptocompare.com/data/price',
                            params={'fsym': coin_symbol.upper(), 'tsyms': 'USD,JPY,EUR', 'api_key': api_key})
    content = response.json()  # dictionary of json

    if content.get('Response') == 'Error':
        sys.stderr.write(f'CryptoCurrency Error: {content.get("Message")}')
        return 'Use a valid currency symbol!'
    else:
        return f'${content.get("USD")}'


if __name__ == '__main__':
    print(crypto_price('BTC'))
