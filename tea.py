# --------- libraries
import requests
import time
import sys
import urllib

# --------- project modules
import const
# --------- services
from services.translate import translate
from services.google import google_search
from services.weather import weather
from services.latest_news import latest_news
from services.crypto_price import crypto_price
from services.crypto_news import crypto_news
from services.tweet import tweet
from services.calculator import calculate

# base url for our requests to the telegram APIs
URL = f'https://api.telegram.org/bot{const.TOKEN}/'


def dict_from_url(url):
    '''return json response in form of python dictionary'''
    return requests.get(url).json()  # return the result as a python dictionary


def get_updates(offset=None):
    '''Get updates after the offset'''
    # timeout will keep the pipe open and tell us when there're new updates
    url = URL + 'getUpdates?timeout=90'
    if offset:
        url += f'&offset={offset}'  # add offset if exists
    return dict_from_url(url)  # return dict of latest updates


def send_message(chat_id, text):
    '''Encoeds ``text`` using url-based encoding and send it to ``chat_id``'''
    requests.get(URL + f'sendMessage?chat_id={chat_id}&text={urllib.parse.quote_plus(text)}')


def last_update_id(updates):
    '''takes dict of updates and return the id of last one'''
    update_ids = []
    for update in updates['result']:
        update_ids.append(int(update['update_id']))
    return max(update_ids)  # the last update is the higher one


def handle_updates(updates):
    '''handles updates from different users, parses the commands and sends the proper message'''
    for update in updates['result']:
        text = None  # msg text
        chat = None  # chat_id
        if 'message' in update:
            chat = update['message']['chat']['id']
            if 'text' in update['message']:
                text = update['message']['text']  # extract msg text
        if 'edited_message' in update:
            chat = update['edited_message']['chat']['id']
            if 'text' in update['edited_message']:
                text = update['edited_message']['text']

        if text and chat:
            if not text.startswith('/'):  # if no command provided
                send_message(chat, 'Please use one of the defined commands')

            elif text == '/start':  # handle /start command
                send_message(
                    chat,
                    'Welcome to TBot.\n'
                    'usage:\n'
                    '/help - show help message\n'
                    '/translate - translate message from english to arabic\n'
                    '/google - Google search\n'
                    '/crypto_price - get price for a crypto currency using its symbol\n'
                    '/crypto_news - Latest cryptocurrency news\n'
                    '/news - Latest news from BBC\n'
                    '/weather - Temperature in Zagazig now\n'
                    '/calculate - Calculate mathematical expression\n'
                    '/tweet - Tweet to our Twitter account\n')

            elif text == '/help':  # handle /help command
                send_message(
                    chat,
                    'Available commands:\n'
                    '/help - show this message\n'
                    '/translate - translate message from english to arabic\n'
                    '/google - Google search\n'
                    '/crypto_price - get price for a crypto currency using its symbol\n'
                    '/crypto_news - Latest cryptocurrency news\n'
                    '/news - Latest news from BBC\n'
                    '/weather - Temperature in Zagazig now\n'
                    '/calculate - Calculate mathematical expression\n'
                    '/tweet - Tweet to our Twitter account\n')

            elif text.startswith('/translate '):  # /translate command
                send_message(chat, translate(const.YANDEX, ' '.join(text.split(' ')[1:])))

            elif text.startswith('/google '):  # /google command
                send_message(chat, google_search(' '.join(text.split(' ')[1:])))

            elif text.startswith('/weather'):  # weather command
                send_message(chat, f'The temperature in Zagazig now is: {weather()}')

            elif text.startswith('/news'):  # news command
                send_message(chat, latest_news())

            elif text.startswith('/crypto_price '):  # /crypto_price command
                send_message(chat, crypto_price(const.CAP, text.split(' ')[1]))

            elif text == '/crypto_news':  # crypto_news command
                send_message(chat, crypto_news(const.CAP))

            elif text.startswith('/tweet '):  # tweet command
                result = tweet(
                    const.T_API, const.T_API_SECRET, const.T_TOKEN, const.T_TOKEN_SECRET,
                    ' '.join(text.split(' ')[1:]))
                send_message(chat, result)

            elif text.startswith('/calculate '):  # Calculate command
                send_message(chat, calculate(' '.join(text.split(' ')[1:])))

            # Add your Commands Below in the following form
            # elif text.startswith('yourCommand '):
            #     statements to do
            #     send_message(chat, result)

            else:  # if command wasn't provided correctly
                send_message(chat, 'Please use one of the defined commands correctly!')
        else:  # in case of files/images
            send_message(chat, 'Currently, I handle text messages only!')


def main():
    updates_offset = None  # track last_update_id to use it as offset
    while True:
        try:
            print('getting updates...')
            updates = get_updates(updates_offset)
            if 'result' in updates:  # to prevent KeyError exception
                if len(updates['result']) > 0:
                    updates_offset = last_update_id(updates) + 1
                    handle_updates(updates)
            time.sleep(0.5)
        except KeyboardInterrupt:  # handle Ctrl-C
            print('\nquiting...')
            sys.exit(0)


if __name__ == '__main__':
    main()
