import requests


def crypto_news(CAP):
    '''Latest news for cryptocurrency'''
    response = requests.get(f'https://min-api.cryptocompare.com/data/v2/news/?lang=EN&api_key={CAP}')
    content = response.json().get('Data')[-5:]  # latest 5 news only

    if response.status_code == 200:
        result = []
        for el in content:
            result.append(el['title'])
            result.append(el['url'])
        return '\n'.join(result)
    else:
        return 'Error Happend. Try again later.'


# for development testing
if __name__ == '__main__':
    print(crypto_news('TOKEN HERE'))
