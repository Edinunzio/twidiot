import requests
from bs4 import BeautifulSoup

FAVORITED_URL = 'https://twitter.com/i/activity/favorited_popup?id='

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

