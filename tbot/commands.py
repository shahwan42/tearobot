import os
import sys
import urllib
import requests
import tweepy

from bs4 import BeautifulSoup


def help_command():
    """Returns available commands with their help messages"""
    return 'Available commands:\n' \
        '/help - Show this message\n' \
        '/translate - Translate message from english to arabic\n' \
        '/google - Google search\n' \
        '/crypto_price - Get price for a crypto currency using its symbol\n' \
        '/crypto_news - Latest cryptocurrency news\n' \
        '/news - Latest news from BBC\n' \
        '/weather - Temperature in Zagazig now\n' \
        '/calculate - Calculate a mathematical expression\n' \
        '/tweet - Tweet to our Twitter account\n' \
        '/ocr  - convert image to text\n'


def start_command():
    """Returns start command message"""
    return 'Welcome to TBot.\n' \
        'Usage:\n' \
        '/help - Show help message\n' \
        '/translate - Translate message from english to arabic\n' \
        '/google - Google search\n' \
        '/crypto_price - Get price for a crypto currency using its symbol\n' \
        '/crypto_news - Latest cryptocurrency news\n' \
        '/news - Latest news from BBC\n' \
        '/weather - Temperature in Zagazig now\n' \
        '/calculate - Calculate mathematical expression\n' \
        '/tweet - Tweet to our Twitter account\n' \
        '/ocr  - convert image to text\n'


def calculate(expr):
    """Calculates ``expr`` and returns the result"""
    response = requests.get(f'http://api.mathjs.org/v4/?expr={urllib.parse.quote(expr)}')
    if response.status_code == 200:
        return f'Result: {response.text}'
    return 'Error happened. Use a valid expression'


def crypto_news():
    """Latest news for cryptocurrency"""
    api_key = os.environ.get('CRYPTOCOMPARE_API_KEY')
    if not api_key:
        sys.stderr.write('Please provide CryptoCompare api key.')
        sys.exit(1)
    response = requests.get(f'https://min-api.cryptocompare.com/data/v2/news/?lang=EN&api_key={api_key}')
    content = response.json().get('Data')[-5:]  # latest 5 news only

    if response.status_code == 200:
        result = []
        for el in content:
            result.append(el['title'])
            result.append(el['url'])
            result.append('\n')
        return '\n'.join(result)
    else:
        return 'Error Happend. Try again later.'


def crypto_price(coin_symbol):
    """cryptocurrency price for ``coin_symbol"""
    api_key = os.environ.get('CRYPTOCOMPARE_API_KEY')
    if not api_key:
        sys.stderr.write('Please provide CryptoCompare api key.')
    response = requests.get('https://min-api.cryptocompare.com/data/price',
                            params={'fsym': coin_symbol.upper(), 'tsyms': 'USD,JPY,EUR', 'api_key': api_key})
    content = response.json()  # dictionary of json

    if content.get('Response') == 'Error':
        sys.stderr.write(f'CryptoCurrency Error: {content.get("Message")}')
        return 'Use a valid currency symbol!'
    else:
        return f'${content.get("USD")}'


def google_search(message):
    """google for ``message``"""
    page = requests.get('https://www.google.com/search', params={'q': message})
    soup = BeautifulSoup(page.content, 'html.parser')  # WebPage in HTML
    links = soup.findAll('cite')  # links list
    descriptions = soup.findAll('span', {'class': 'st'})  # descriptions list

    if len(links) == 0:  # if no results found
        return 'No results found for your search query. Try another meaningfull one.'

    result = []  # result to be returned link+description
    for idx, link in enumerate(links):  # loop over the links (whatever their length is)
        result.append(link.text)  # current link
        result.append(descriptions[idx].text)  # current link description
        result.append('\n')  # new line

    return '\n'.join(result)


def latest_news():
    """Latest news from bbc"""
    url = 'https://www.bbc.com'
    page = requests.get(url)

    # parse the whole page in html
    soup = BeautifulSoup(page.content, 'html.parser')
    # get all  news links (tag 'a') in class "media__link"
    news = soup.findAll('a', {'class': 'media__link'})

    result = []
    for el in news:
        if not str(el['href']).startswith('https://'):
            result.append(url + el['href'])
        result.append(el.text.strip())

    return '\n'.join(result[:10])


def ocr_space_url(url, overlay=False, language='eng'):
    api_key = os.environ.get('OCR_API')
    payload = {'url': url, 'isOverlayRequired': overlay, 'apikey': api_key, 'language': language, }
    r = requests.post('https://api.ocr.space/parse/image', data=payload,)
    results = r.json()
    return results['ParsedResults'][0]['ParsedText']


def ocr_space_file(filename, overlay=False, language='eng'):
    api_key = os.environ.get('OCR_API')
    payload = {'isOverlayRequired': overlay, 'apikey': api_key, 'language': language, }
    with open(filename, 'rb') as f:
        r = requests.post('https://api.ocr.space/parse/image', files={filename: f}, data=payload,)
    results = r.json()
    return results['ParsedResults'][0]['ParsedText']


def translate(message):
    """Translate ``message`` from english to arabic"""
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


def tweet(text):
    """Tweet ``text`` to twitter account"""
    t_api = os.environ.get('TWITTER_API')
    t_api_secret = os.environ.get('TWITTER_API_SECRET')
    t_token = os.environ.get('TWITTER_TOKEN')
    t_token_secret = os.environ.get('TWITTER_TOKEN_SECRET')
    if not t_api or not t_api_secret or not t_token or not t_token_secret:
        sys.stderr.write('Please provide twitter tokens.')
        sys.exit(1)

    auth = tweepy.OAuthHandler(t_api, t_api_secret)
    auth.set_access_token(t_token, t_token_secret)
    api = tweepy.API(auth)
    result = ''
    try:
        response = api.update_status(text)
        tweet_id = response._json['id_str']
        tweet_link = f'https://twitter.com/tbot60/status/{tweet_id}'
        result = f'Your tweet: {tweet_link}'
    except tweepy.error.TweepError:
        result = 'Do not repeat the same tweet'
    return result


def weather():
    """Returns weather in zagazig now"""
    page = requests.get('https://www.google.com/search?q=weather+zagazig&oq=weather&lang=en-GB')
    temperature = BeautifulSoup(page.content, 'html.parser').findAll('span', {'class': 'wob_t'})[0].text
    return f'The temperature in Zagazig now is: {temperature}'
