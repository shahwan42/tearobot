import requests


def crypto_news(CAP):
    '''Latest news for cryptocurrency'''
    response = requests.get(
        'https://min-api.cryptocompare.com/data/v2/news/?lang=EN',
        params={'api_key': CAP})
    content = response.json().get('Data')[-5:]

    if response.status_code == 200:
        result = []
        for el in content:
            result.append(el['title'])
            result.append(el['url'])
        return '\n'.join(result)
    else:
        result = "We are very sorry. Error Happend, try again later."
        return result


# for development testing
if __name__ == '__main__':
    print(crypto_news('TOKEN HERE'))
