import requests
from bs4 import BeautifulSoup

PREFIX = 'https://twitter.com/'
FAVORITED_URL = PREFIX + 'i/activity/favorited_popup?id='
RETWEETED_URL = PREFIX + '/i/activity/retweeted_popup?id='
USER_ACTIVITY = '/with_replies'


def get_users_by_liked_tweet(tweet_id):
    try:
        url = FAVORITED_URL + tweet_id
    except TypeError:
        url = FAVORITED_URL + str(tweet_id)

    r = requests.get(url)
    if r.status_code == 200:
        parsed_json = r.json()
        html = parsed_json['htmlUsers'].encode('ascii', 'ignore')
        soup = BeautifulSoup(html, "html.parser")
        usernames = soup.select('.username')
        liked_by = [u.get_text() for u in usernames]
        return liked_by
    elif r.status_code == 404:
        return 'Tweet Not Found'
    else:
        return 'An unknown error occured'


def get_users_by_retweets(tweet_id):
    try:
        url = RETWEETED_URL + tweet_id
    except TypeError:
        url = RETWEETED_URL + str(tweet_id)

    r = requests.get(url)
    if r.status_code == 200:
        parsed_json = r.json()
        html = parsed_json['htmlUsers'].encode('ascii', 'ignore')
        soup = BeautifulSoup(html, "html.parser")
        usernames = soup.select('.username')
        retweeted_by = [u.get_text() for u in usernames]
        return retweeted_by
    elif r.status_code == 404:
        return 'Tweet Not Found'
    else:
        return 'An unknown error occured'

def get_users_tweets(handle):
    try:
        url = PREFIX + handle[1:] + USER_ACTIVITY
    except TypeError:
        url = PREFIX + str(handle[1:]) + USER_ACTIVITY
    r = requests.get(url)
    if r.status_code == 200:
        soup = BeautifulSoup(r.content, 'html.parser')
        stream = soup.select('.stream-items')[0]
        li = stream.select('li.stream-item')
        contents = [l.contents[1] for l in li]
        tweets = []
        for c in contents:
            if c['data-screen-name'] == handle[1:]:
                txt = c.text.split(handle[1:])
                tweets.append(txt[1])
        return tweets
    elif r.status_code == 404:
        return 'Page Not Found'
    else:
        return 'An unknown error occured'