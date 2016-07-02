import unittest
from users.user import Twidiot


class TestTwidiot(unittest.TestCase):

    def setUp(self):
        self.t = Twidiot()
        self.get_recent_activity = self.t.get_recent_activity('@Claudie4')
        self.u_not_found = self.t.get_recent_activity('@ssadasihnlkhdoisyfoih')
        self.get_user_type_error = self.t.get_recent_activity('dfh aja')

        self.liked_by = self.t.liked_by('745892215969423360')
        self.t_not_found = self.t.liked_by('745892215969423')
        self.get_type_error = self.t.liked_by(74589221596942)

        self.get_r_users = self.t.retweeted_by('745892215969423360')
        self.get_r_false_id = self.t.retweeted_by('745892215969423')
        self.get_r_type_error = self.t.retweeted_by(74589221596942)

    def test_get_recent_activity(self):
        self.assertEqual(list, type(self.get_recent_activity))
        self.assertEqual("Page Not Found", self.u_not_found)
        self.assertRaises(TypeError, self.get_user_type_error)

    def test_liked_by(self):
        self.assertEqual(list, type(self.liked_by))
        self.assertEqual('Tweet Not Found', self.t_not_found)
        self.assertRaises(TypeError, self.get_type_error)

    def test_retweeted_by(self):
        self.assertEqual(list, type(self.get_r_users))
        self.assertEqual('Tweet Not Found', self.get_r_false_id)
        self.assertRaises(TypeError, self.get_r_type_error)
