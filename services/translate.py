import requests
import os


def translate(yandex_token, message):
    '''Translate ``message`` from english to arabic'''
    response = requests.post(
        'https://translate.yandex.net/api/v1.5/tr.json/translate',
        params={'key': yandex_token, 'text': message, 'lang': 'en-ar'})
    jsdict = response.json()
    if response.status_code == 200:
        return jsdict.get('text')[0]  # get text list then get element 0 of it
    else:
        return 'Error Happend, try again later.'


# for development testing
if __name__ == '__main__':
    yandex = os.environ.get('YANDEX')
    print(translate(yandex, 'Can you translate me?'))
