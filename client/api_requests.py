import json
import requests

from resources import BASE_URL
"""
Posting requests to the Pocket API
"""

pageid = 0

class ApiRequests:
    page_id = 0
    req_headers = {"X-Accept": "application/json",
                       "Content-Type": "application/json"}

    def __init__(self, key, access):
        self.key = key
        self.access = access

    @staticmethod
    def add(key, access, url, title):
        # Adding an entry

        payload = {
            "consumer_key": key,
            "access_token": access,
            "url": url,
            "title": title
        }

        response = requests.post(f"{BASE_URL}/v3/add", data=payload)
        print("Added item number: "
              + response.json()["item"]["item_id"] + ". Url: " + response.json()["item"]["normal_url"])
        global pageid
        pageid = int(response.json()["item"]["item_id"])
        return response.json()

    @staticmethod
    def add_tags(key, access, tag, page_id):
        # adding tags to an entry specified by page id

        url = f"{BASE_URL}/v3/send"

        actions_add_tags = [
            {
                "action": "tags_add",
                "item_id": page_id,
                "tags": tag,
            }
        ]

        payload = {
            "consumer_key": key,
            "access_token": access,
            "actions": json.dumps(actions_add_tags)
        }

        response = requests.post(url, data=payload)
        return response

    @staticmethod
    def archive(key, access, page_id):
        # archiving an entry specified by page id

        url = "https://getpocket.com/v3/send"

        arch = [
            {
                "action": "archive",
                "item_id": int(page_id),
            }
        ]

        payload = {
            "actions": json.dumps(arch),
            "access_token": access,
            "consumer_key": key,
        }

        response = requests.post(url, data=payload)
        return response


    @staticmethod
    def retrieve_list(key, access):
        # Retrieving an entire list of bookmarks
        url = f"{BASE_URL}/v3/get"
        payload = {
            "consumer_key": key,
            "access_token": access,
            "state": "all"
        }
        response = requests.post(url, data=payload)
        return response

    @staticmethod
    def retrieve_list_tagged(key, access, tag):
        # Retrieving a list of all tagged entries
        url = f"{BASE_URL}/v3/get"
        payload = {
            "consumer_key": key,
            "access_token": access,
            "tag": tag
        }
        response = requests.post(url, data=payload)
        return response

    @staticmethod
    def retrieve_list_archived(key, access):
        # Retrieving a list of all archived entries
        url = f"{BASE_URL}/v3/get"
        payload = {
            "consumer_key": key,
            "access_token": access,
            "state": "archive"
        }
        response = requests.post(url, data=payload)
        return response.json()

    @staticmethod
    def delete(key, access, page_id):
        # Removing an entry specified by page id
        # print(f"Deleting {page_id}")

        url = f"{BASE_URL}/v3/send"

        delete = [
            {
                "action": "delete",
                "item_id": int(page_id),
            }
        ]

        payload = {
            "actions": json.dumps(delete),
            "access_token": access,
            "consumer_key": key,
        }

        response = requests.post(url, data=payload)
        return response

    @staticmethod
    def add_batch(key, access, batch):
        url = f"{BASE_URL}/v3/send"

        dataload = []
        for elem in batch:
            dataload.append(elem)

        payload = {
            "actions": json.dumps(dataload),
            "access_token": access,
            "consumer_key": key,
        }

        response = requests.post(url, data=payload)
        return response

    @staticmethod
    def favourite(key, access, page_id):

        url = f"{BASE_URL}/v3/send"
        fav = [
            {
                "action": "favorite",
                "item_id": int(page_id),
            }
        ]

        payload = {
            "actions": json.dumps(fav),
            "access_token": access,
            "consumer_key": key,
        }

        response = requests.post(url, data=payload)
        return response