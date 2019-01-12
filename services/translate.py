import requests
import json


def translate(yandex_token, word):
    '''Translate ``word`` from english to arabic'''
    url = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
    url += f'?key={yandex_token}'
    url += f'&text={word}'
    url += f'&lang=en-ar'
    response = requests.post(url)  # post request
    content = response.content.decode('utf8')  # convert to str
    # convert to dict then get text list then get element 0 of text list
    result = json.loads(content).get('text')[0]
    return result
