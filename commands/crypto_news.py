import requests
import os
import sys


def crypto_news():
    '''Latest news for cryptocurrency'''
    api_key = os.environ.get('CRYPTOCOMPARE_API_KEY')
    if not api_key:
        sys.stderr.write('Please provide CryptoCompare api key.')
        sys.exit(1)
    response = requests.get(f'https://min-api.cryptocompare.com/data/v2/news/?lang=EN&api_key={api_key}')
    content = response.json().get('Data')[-5:]  # latest 5 news only

    if response.status_code == 200:
        result = []
        for el in content:
            result.append(el['title'])
            result.append(el['url'])
        return '\n'.join(result)
    else:
        return 'Error Happend. Try again later.'


if __name__ == '__main__':
    print(crypto_news())
