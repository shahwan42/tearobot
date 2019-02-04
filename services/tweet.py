import tweepy
import os
import random
import string


def tweet(t_api, t_api_secret, t_token, t_token_secret, text):
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


# for development testing
if __name__ == '__main__':
    T_API = os.environ.get('T_API')
    T_API_SECRET = os.environ.get('T_API_SECRET')
    T_TOKEN = os.environ.get('T_TOKEN')
    T_TOKEN_SECRET = os.environ.get('T_TOKEN_SECRET')
    text = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))  # Random text generation
    result = tweet(T_API, T_API_SECRET, T_TOKEN, T_TOKEN_SECRET, text)
    print(result)
