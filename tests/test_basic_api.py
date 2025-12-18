"""
Tests for the JSONPlaceholder API

Covers basic testing for GET and POST requests
"""

import requests

TEST_URL = "https://jsonplaceholder.typicode.com"
TEST_USER = "users"
TEST_POST = "posts"
TEST_USER_SUCCESS = 1
TEST_USER_SUCCESS_FIELDS = (TEST_USER_SUCCESS, "Leanne Graham", "Sincere@april.biz")
TEST_USER_FAIL = 999
REQUEST_SUCCESS = 200
REQUEST_CREATED = 201
POST_DATA = {"id": 101, "name": "Dan", "email": "DanTest@fake.com"}
REQUEST_NOT_FOUND = 404


class TestJSONPlaceholderAPI:

    def test_get_user_success(self):
        """
        Test that produces a successful GET request on the users endpoint
        """
        # put together URL and make get request
        url = f"{TEST_URL}/{TEST_USER}/{TEST_USER_SUCCESS}"
        response = requests.get(url)

        # parse data
        data = response.json()

        # confirm our response was successful
        assert response.status_code == REQUEST_SUCCESS

        # confirm that all fields match for requested user!
        assert (data["id"], data["name"], data["email"]) == TEST_USER_SUCCESS_FIELDS

    def test_post_success(self):
        """
        Test that produces succesful POST request
        """
        # construct our post request url
        url = f"{TEST_URL}/{TEST_POST}"

        # create post request function call with post data payload
        response = requests.post(url, json=POST_DATA)

        # check that we got a created staus code
        assert response.status_code == REQUEST_CREATED

        data = response.json()

        # confirm that our data was sent
        for key in POST_DATA:
            assert data[key] == POST_DATA[key]

    def test_get_user_fail(self):
        """
        Test that tries to request for a non existent user id
        """
        # construct our bad url and make get request
        url = f"{TEST_URL}/{TEST_USER}/{TEST_USER_FAIL}"

        response = requests.get(url)

        # check that our status code reflects a 404: not found
        assert response.status_code == REQUEST_NOT_FOUND
