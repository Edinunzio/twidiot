import unittest
from users.user import Twidiot


class TestTwidiot(unittest.TestCase):

    def setUp(self):
        self.t = Twidiot()

    def test_get_recent_activity(self):
        self.assertEqual(list, type(self.t.get_recent_activity('@Claudie4')))
        self.assertEqual("Page Not Found", self.t.get_recent_activity('@ssadasihnlkhdoisyfoih'))
        self.assertRaises(TypeError, self.t.get_recent_activity('dfh aja'))

    def test_liked_by(self):
        self.assertEqual(list, type(self.t.liked_by('745892215969423360')))
        self.assertEqual('Tweet Not Found', self.t.liked_by('745892215969423'))
        self.assertRaises(TypeError, self.t.liked_by(74589221596942))

    def test_retweeted_by(self):
        self.assertEqual(list, type(self.t.retweeted_by('745892215969423360')))
        self.assertEqual('Tweet Not Found', self.t.retweeted_by('745892215969423'))
        self.assertRaises(TypeError, self.t.retweeted_by(74589221596942))

    def test_get_request(self):
        self.assertEqual("<class 'requests.models.Response'>", str(type(self.t._get_request(self.t.FAVORITED_URL, '745892215969423360'))))
