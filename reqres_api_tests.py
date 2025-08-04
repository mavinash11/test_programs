

import time
import pytest
import requests
from logging_test import logger
import json
import urllib3

urllib3.disable_warnings()
reqres_url = "https://reqres.in/api/users"
# headers = {"content-type": "application/json", "foobar": "raboof", "x-api-key": "reqres-free-v1"}
headers = {"content-type": "application/json", "foobar": "raboof"}
api_key = "reqres-free-v1"



@pytest.mark.reqres
def test_create_new_user():
    data = {
        "name": "Paulo Oliveira",
        "movies": ["I Love You Man", "Role Models"]
    }
    response = requests.post(reqres_url, data=data, headers=headers)
    assert response.status_code == 200
    time.sleep(5)
    response = requests.get(url=reqres_url, headers=headers, verify=False)
    for data in response.json():
        logger.info(data)


def test_update_user():
    data = {
        "name": "Testabcd"
    }
    reqres_url = "http://reqres.in/api/users/2"
    response = requests.put(url=reqres_url, data=data, headers=headers)
    logger.info(response.status_code)
    logger.info(response.json())


def test_register_new_user():
    data = {
        "name":"testuser",
        "email": "eve.holt@reqres.in",
        "password": "pistol"
    }
    reqres_url = "http://reqres.in/api/register"
    response = requests.post(url=reqres_url, data=data, headers=headers)
    logger.info(response.json())


if __name__ == "__main__":
    test_get_single_post()
    test_get_list_of_users()