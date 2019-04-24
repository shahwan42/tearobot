"""
    Commands Module
"""

import os
import sys
import urllib
import requests
import tweepy
from .db import DBHelper
# from .utils import formating


def help_command():
    """Returns available commands with their help messages"""
    return "Available commands:\n" \
        "/help - Show this message\n" \
        "/weather - Weather in `Zagazig, Egypt` now\n" \
        "/translate - Translate message from english to arabic\n" \
        "/calculate - Calculate a mathematical expression\n" \
        "/tweet - Tweet on our Twitter account\n" \
        "/ocr_url - Extract text from image\n"\
        "/schedule - Show the college schedule and importnat events\n" \
        "/stop - Stop using bot\n" \
        "/start - Start using bot"


def start_command(db:DBHelper, user_id: int, updated: int, active: bool):

    db.set_user_status(user_id, updated, active)
    """Returns start command message"""
    return "Welcome to TBot.\n" \
        "Usage:\n" \
        "/help - Show help message\n" \
        "/weather - Weather in `Zagazig, Egypt` now\n" \
        "/translate - Translate message from English to Arabic\n" \
        "/calculate - Calculate a mathematical expression\n" \
        "/tweet - Tweet on our Twitter account\n" \
        "/ocr_url - Extract text from image\n" \
        "/schedule - Show the college schedule and importnat events\n" \
        "/stop - Stop using bot\n" \
        "/start - Start using bot"



def calculate(expr):
    """Calculates ``expr`` and returns the result"""
    response = requests.get(f"http://api.mathjs.org/v4/?expr={urllib.parse.quote(expr)}")
    if response.status_code == 200:
        return f"Result: {response.text}"
    return "Error happened. Use a valid expression"


def ocr_url(url, overlay=False, language="eng"):
    """OCR from image using its ``url``"""
    api_key = os.environ.get("OCR_API")
    payload = {"url": url, "isOverlayRequired": overlay, "apikey": api_key, "language": language, }
    r = requests.post("https://api.ocr.space/parse/image", data=payload,)
    results = r.json()
    try:
        return results["ParsedResults"][0]["ParsedText"]
    except Exception:
        return "Error. Please provide a valid URL"


def translate(message):
    """Translate ``message`` from english to arabic"""
    yandex_token = os.environ.get("YANDEX_TRANSLATE_TOKEN")
    if not yandex_token:
        sys.stderr.write("Please Provide Yandex Translate Token")
        sys.exit(1)
    response = requests.post(
        "https://translate.yandex.net/api/v1.5/tr.json/translate",
        params={"key": yandex_token, "text": message, "lang": "en-ar"})
    jsdict = response.json()
    if response.status_code == 200:
        return jsdict.get("text")[0]  # get text list then get element 0 of it
    else:
        return "Error Happend, try again later."


def tweet(text):
    """Tweet ``text`` to twitter account"""
    t_api = os.environ.get("TWITTER_API")
    t_api_secret = os.environ.get("TWITTER_API_SECRET")
    t_token = os.environ.get("TWITTER_TOKEN")
    t_token_secret = os.environ.get("TWITTER_TOKEN_SECRET")
    if not t_api or not t_api_secret or not t_token or not t_token_secret:
        sys.stderr.write("Please provide twitter tokens.")
        sys.exit(1)

    auth = tweepy.OAuthHandler(t_api, t_api_secret)
    auth.set_access_token(t_token, t_token_secret)
    api = tweepy.API(auth)
    result = ""
    try:
        response = api.update_status(text)
        tweet_id = response._json["id_str"]
        tweet_link = f"https://twitter.com/tbot60/status/{tweet_id}"
        result = f"Your tweet: {tweet_link}"
    except tweepy.error.TweepError:
        result = "Do not repeat the same tweet"
    return result


def weather():
    """Returns weather in Zagazig, Egypt"""
    location_key = 127335  # Zagazig location key
    url = f"http://dataservice.accuweather.com/forecasts/v1/hourly/1hour/{location_key}"
    parameters = {
        "apikey": os.environ.get("ACCUWEATHER"),
        "metric": True
    }
    data = requests.get(url, params=parameters).json()[0]
    temperature = data["Temperature"]["Value"]
    atm_status = data["IconPhrase"]
    location = "Zagazig, Egypt"
    return f"Weather is {atm_status} in {location}.\nAnd it currently feels like {temperature} °C"


def schedule():
    """Returns events from schedule table"""
    db = DBHelper()
    x = db.get_data() # x -> list of tuples 
    x_list = [list(i) for i in x] # convert list of tuples to list of lists to deal with 
    y = ''
    for i in range(len(x_list)): 
        #print the list of lists 
        y = str(y) + 'Date:  ' +str(x_list[i][1]) + '\n' +  'Importance:  ' +str(x_list[i][2]) + '\n' +str(x_list[i][0]) + '\n' + '---------------------------' + '\n'
    return str(y)





def stop(db: DBHelper, user_id: int, updated: int, active: bool):
    db.set_user_status(user_id, updated, active)


