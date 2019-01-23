import requests


def crypto_price(CAP, coin):
    '''cryptocurrency price for ``coin``'''
    response = requests.get(
        'https://min-api.cryptocompare.com/data/price',
        params={'fsym': coin,
                'tsyms': 'USD,JPY,EUR',
                'api_key': CAP})
    content = response.json()

    if content.get('Response') == "Error":
        result = content.get("Message")
    else:
        result = content.get("USD")
    return result


# for development testing
if __name__ == '__main__':
    print(crypto_price(
        'TOKEN HERE',
        'BTC'
    ))
