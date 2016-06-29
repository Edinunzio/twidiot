import unittest
from users.user import get_users_by_liked_tweet


class TestUser(unittest.TestCase):

    def setUp(self):
        self.get_users = get_users_by_liked_tweet('745892215969423360')
        self.get_false_id = get_users_by_liked_tweet('745892215969423')
        self.get_type_error = get_users_by_liked_tweet(74589221596942)
        self.expected_list = [u'@Claudie4', u'@FancyFreeSydney', u'@GGG_says', u'@renzocapetti29', u'@daniellstevens', u'@TenorioPraxGab', u'@mr_preface', u'@ncartwright34', u'@hrlaube', u'@OkemwaNeaman', u'@JohnnySoftware', u'@momo24k5', u'@davemoskowitz10', u'@SidSeven777']

    def test_get_users_1(self):
        self.assertEqual(list, type(self.get_users))
        self.assertEqual(self.expected_list, self.get_users)
        self.assertEqual('Tweet Not Found', self.get_false_id)
        self.assertRaises(TypeError, self.get_type_error)