import requests
from bs4 import BeautifulSoup


class Twidiot(object):

    def __init__(self):
        self.PREFIX = 'https://twitter.com/'
        self.FAVORITED_URL = self.PREFIX + 'i/activity/favorited_popup?id='
        self.RETWEETED_URL = self.PREFIX + '/i/activity/retweeted_popup?id='
        self.USER_ACTIVITY = '/with_replies'

    def get_recent_activity(self, handle):
        handle = self.PREFIX + str(handle[1:])  # trim @
        r = self._get_request(handle, self.USER_ACTIVITY)
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

    def liked_by(self, tweet_id):
        r = self._get_request(self.FAVORITED_URL, tweet_id)
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

    def retweeted_by(self, tweet_id):
        r = self._get_request(self.RETWEETED_URL, tweet_id)
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

    @staticmethod
    def _get_request(prefix, ending):
        try:
            url = prefix + ending
        except TypeError:
            url = prefix + str(ending)
        r = requests.get(url)
        return r
