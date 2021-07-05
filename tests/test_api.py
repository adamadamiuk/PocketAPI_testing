import unittest
import resources
unittest.TestLoader.sortTestMethodsUsing = None

import client.api_requests
from tests.test_base import BaseTest


api_request = client.api_requests.ApiRequests
"""
Testing main functionalities of the Pocket API
"""

class TestingAPI(BaseTest):
    def test_add(self):
        url = 'http://www.onet.pl'
        title = 'Onet.pl website'
        response = api_request.add(self.code, self.access, url, title)
        self.assertEqual("http://onet.pl", str(response['item']['normal_url']))

    def test_list(self):
        response = api_request.retrieve_list(self.code, self.access)
        self.assertEqual("<Response [200]>", str(response))
        # checking if the list of all items can be obtained

    def test_add_tags(self):
        response = api_request.add_tags(self.code, self.access, 'stackoverflow tag', self.pg_id)
        self.assertEqual("<Response [200]>", str(response))
        print(response.json())

    def test_add_multiple_items(self):
        # adding a batch of url addresses
        batch = resources.batch
        response = api_request.add_batch(self.code, self.access, batch)
        self.assertEqual("<Response [200]>", str(response))

        # testing that all urls have been added
        results = response.json()
        batch_element = 0
        for r in results['action_results']:
            batch_element = batch_element + 1
            self.assertEqual(r['normal_url'], batch[batch_element - 1]['url'])

    def test_retrieve_tagged_list(self):
        resp = api_request.retrieve_list_tagged(self.code, self.access, 'test tag')
        checking_tag = resp.json()['list']
        self.assertTrue(checking_tag)
        # if "test tag" has been used, the list is not empty and therefore "True"

    def test_archive(self):
        response = api_request.archive(self.code, self.access, self.pg_id)
        self.assertEqual("<Response [200]>", str(response))
        arch_list = api_request.retrieve_list_archived(self.code, self.access)
        self.assertEqual('https://stackoverflow.com', str(arch_list['list'][str(self.pg_id)]['given_url']))

    def test_delete(self):
        response = api_request.delete(self.code, self.access, self.pg_id)
        self.assertEqual("<Response [200]>", str(response))

    def test_favorite(self):
        response = api_request.favourite(self.code, self.access, self.pg_id)
        self.assertEqual("<Response [200]>", str(response))







