import requests
import os


def translate(yandex_token, message):
    '''Translate ``message`` from english to arabic'''
    res = requests.post(
        'https://translate.yandex.net/api/v1.5/tr.json/translate',
        params={'key': yandex_token, 'text': message, 'lang': 'en-ar'})
    jsdict = res.json()  # dict of the response's json
    if res.status_code == 200:
        # get text list then get element 0 of it
        result = jsdict.get('text')[0]
    else:
        result = 'We are very sorry. Error Happend, try again later.'
    return result


# for development testing
if __name__ == '__main__':
    yandex = os.environ.get('YANDEX')
    print(translate(yandex, 'Can you translate me?'))
