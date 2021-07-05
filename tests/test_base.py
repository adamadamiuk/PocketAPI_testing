from unittest import TestCase

from client.authorization import auth_code, access_token, KEY
from client.api_requests import ApiRequests

"""
Setting up the entire testing process and each test separately
"""

class BaseTest(TestCase):
    @classmethod
    def setUpClass(cls):
        # authorization before tests start
        # it is necessary to send requests to the API
        global access
        cls.access = access_token(auth_code())
        cls.code = KEY
        access = cls.access

    @classmethod
    def tearDownClass(cls):
        # removing all entries once testing is completed
        cls.code = KEY
        resp = ApiRequests.retrieve_list(cls.code, access)
        for i in resp.json()['list']:
            ApiRequests.delete(cls.code, access, i)


    def setUp(cls):
        # creating an entry before each test
        url = 'https://stackoverflow.com'
        title = 'StackOverflow board'
        resp = ApiRequests.add(cls.code, cls.access, url, title)
        cls.pg_id = int(resp["item"]["item_id"])
        ApiRequests.add_tags(cls.code, cls.access, "test tag", cls.pg_id)


    def tearDown(cls):
        # removing the entry after each test
        ApiRequests.delete(cls.code, cls.access, cls.pg_id)



