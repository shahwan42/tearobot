import json
import requests
import time
import sys
import os
import urllib
# import config  # uncomment for development
from services.translate import translate
from services.google import google_search
# provide bot token from TOKEN envVar or config file
TOKEN = os.environ.get('TOKEN')  # or config.TOKEN  # uncomment for dev
# other services tokens
YANDEX = os.environ.get('YANDEX')  # or config.YANDEX  # uncomment for dev
if not TOKEN:
    print('Please provied your tokens. Refer to the README file')
    sys.exit(0)
# base url for our request to the telegram APIs
URL = f'https://api.telegram.org/bot{TOKEN}/'


def get_url(url):
    '''Send GET request to url and return a unicode utf8 string'''
    response = requests.get(url)  # get response
    content = response.content.decode('utf8')  # decode response to utf8
    return content  # json string


def json_from_url(url):
    '''return json string form provided url
    depends on get_url(url) function'''
    content = get_url(url)  # get content as text
    js = json.loads(content)  # json string to python dictionary
    return js  # return the result dictionary


def get_updates(offset=None):
    '''Get updates after the offset'''
    # timeout will keep the pipe open and tell us when there're new updates
    method = 'getUpdates'  # telegram method to get latest updates
    timeout = 90  # inseconds
    url = URL + f'{method}?timeout={timeout}'
    if offset:
        url += f'&offset={offset}'
    js = json_from_url(url)  # dict of latest updates
    return js


def last_chat_id_and_text(updates):
    '''takes last``updates`` as dict
    and returns last ``(chat_id, text)`` as tuple'''
    updates_num = len(updates['result'])
    last_update = updates_num - 1
    chat_id = updates['result'][last_update]['message']['chat']['id']
    text = updates['result'][last_update]['message']['text']
    return (chat_id, text)


def send_message(chat_id, text):
    '''Encoeds ``text`` using url-based encoding and send it to
    ``chat_id``'''
    text = urllib.parse.quote_plus(text)  # url-encoding
    method = 'sendMessage'  # telegram method to use in the url
    # url + parameters (query string)
    url = URL + f'{method}?chat_id={chat_id}&text={text}'
    get_url(url)  # send the GET request


def last_update_id(updates):
    '''takes dict of updates and return the id of last one'''
    update_ids = []
    for update in updates['result']:
        update_ids.append(int(update['update_id']))
    return max(update_ids)  # the last update is the higher one


def handle_updates(updates):
    '''handles last updates from different users,
    parses the commands and send the proper message'''
    for update in updates['result']:
        text = update['message']['text']  # extract msg text
        chat = update['message']['chat']['id']  # extract chat_id
        if not text.startswith('/'):  # if no command provided
            send_message(chat, 'Please use one of the defined commands')
        elif text == '/start':  # handle /start command
            send_message(chat, 'Welcome to TBot.\nusage:\n'
                         '/translate [message] - to translate '
                         'a message from english to arabic')
        elif text == '/help':  # handle /help command
            send_message(chat,
                         'Available commands:\n'
                         '/help - show this message\n'
                         '/translate [message] - translate message '
                         'from english to arabic')
        elif text.startswith('/translate '):  # /translate command
            message = ' '.join(text.split(' ')[1:])  # get message to translate
            result = translate(YANDEX, message)
            send_message(chat, result)
        elif text.startswith('/google '):  # /google command
            result = google_search(text)
            result = '\n'.join(result)
            send_message(chat,result)

        # Add your Commands Below in the following form
        # elif text.startswith('yourCommand '):
        #     statements to do
        #     send_message(chat, result)
        else:  # if command wasn't provided correctly
            send_message(chat,
                         'Please use one of the defined commands correctly!')


def main():
    updates_offset = None  # track last_update_id to use it as offset
    while True:
        try:
            print('getting updates...')
            updates = get_updates(updates_offset)
            if updates['result']:  # to prevent KeyError exception
                if len(updates['result']) > 0:
                    updates_offset = last_update_id(updates) + 1
                    handle_updates(updates)
            time.sleep(0.5)
        except KeyboardInterrupt:
            print('\nquiting...')
            sys.exit(0)


if __name__ == '__main__':
    main()
