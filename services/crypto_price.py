import requests


def crypto_price(CAP, coin):
    '''cryptocurrency price for ``coin``'''
    response = requests.get('https://min-api.cryptocompare.com/data/price',
                            params={'fsym': coin.upper(), 'tsyms': 'USD,JPY,EUR', 'api_key': CAP})
    content = response.json()  # dictionary of json

    if content.get('Response') == 'Error':
        return content.get('Message')
    else:
        return f'${content.get("USD")}'


# for development testing
if __name__ == '__main__':
    print(crypto_price(
        'TOKEN HERE',
        'BTC'
    ))
