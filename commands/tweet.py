import tweepy
import os
import random
import string
import sys


def tweet(text):
    '''Tweet ``text`` to tiwtter account'''
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


if __name__ == '__main__':
    text = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))  # Random text generation
    result = tweet(text)
    print(result)
