import requests
import os
import sys


def translate(message):
    '''Translate ``message`` from english to arabic'''
    yandex_token = os.environ.get('YANDEX_TRANSLATE_TOKEN')
    if not yandex_token:
        sys.stderr.write('Please Provide Yandex Translate Token')
        sys.exit(1)
    response = requests.post(
        'https://translate.yandex.net/api/v1.5/tr.json/translate',
        params={'key': yandex_token, 'text': message, 'lang': 'en-ar'})
    jsdict = response.json()
    if response.status_code == 200:
        return jsdict.get('text')[0]  # get text list then get element 0 of it
    else:
        return 'Error Happend, try again later.'


if __name__ == '__main__':
    print(translate('Can you translate me?'))
