import requests
import json
import urllib
# import os  # uncomment for development


def translate(yandex_token, message):
    '''Translate ``message`` from english to arabic'''
    text = urllib.parse.quote_plus(message)
    url = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
    url += f'?key={yandex_token}'
    url += f'&text={text}'
    url += f'&lang=en-ar'
    response = requests.post(url)  # post request
    content = response.content.decode('utf8')  # convert to str
    js = json.loads(content)
    if js.get('code') == 200:
        # convert to dict then get text list then get element 0 of text list
        result = json.loads(content).get('text')[0]
    else:
        result = 'We are very sorry. Error Happend, try again later.'
    return result


# uncomment for development
# if __name__ == '__main__':
    # yandex = 'yandex token' or os.environ.get('YANDEX')
    # print(translate(yandex, 'translate me'))
