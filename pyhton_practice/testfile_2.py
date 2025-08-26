# try get api, post api
# try logging
# try pytest

import time
import pytest
import requests
from logging_test import logger
import json
import urllib3

urllib3.disable_warnings()
# headers = {"content-type": "application/json", "foobar": "raboof", "x-api-key": "reqres-free-v1"}
headers = {"content-type": "application/json", "foobar": "raboof", "User-Agent":"MyApp/1.0.0"}
api_key = "reqres-free-v1"

demokey= "DEMO_KEY"
url = 'http://jsonplaceholder.typicode.com'

@pytest.mark.jsonplaceholder
def test_get_all_posts():
    logger.info("get full list of posts in api output")
    response = requests.get(url=url+"/posts", headers=headers, verify=False)
    assert response.status_code == 200
    logger.debug(response.json())


@pytest.mark.jsonplaceholder
def test_get_single_post():
    response = requests.get(url=url+"/posts/1", verify=False)
    logger.info(response)
    assert response.status_code == 200
    json_data = json.dumps(response.json())
    logger.info(json_data)


@pytest.mark.jsonplaceholder
def test_get_comments_for_a_single_post(postid=str(1)):
    response = requests.get(url=url+"/posts/"+postid+"/comments", verify=False)
    logger.info(response)
    assert response.status_code == 200
    json_data = json.dumps(response.json())
    logger.info(json_data)


@pytest.mark.jsonplaceholder
def test_get_comments_for_the_given_post_id(postid=str(1)):
    response = requests.get(url=url+"/comments?postId="+postid, verify=False)
    logger.info(response)
    assert response.status_code == 200
    json_data = json.dumps(response.json())
    logger.info(json_data)


@pytest.mark.jsonplaceholder
def test_post_new_comment_for_post_id(postid=str(1)):
    data={"title": "test title",
          "body": "sigma 123",
          "user_id":postid}
    data_1 = json.dumps(data)
    response = requests.post(url=url+"/posts", data=data_1, headers=headers, verify=False)
    logger.info(response.status_code)
    assert response.status_code == 201
    logger.info(json.dumps(response.json()))


@pytest.mark.jsonplaceholder
def test_update_comment_for_post_id(postid=str(10)):
    data={"name": "xyz",
          "email": "test.abc@waino.me",
          "title": "test title",
          "body": "sigma 123",
          "user_id":postid}
    data_1 = json.dumps(data)
    response = requests.put(url=url+"/posts/"+postid, data=data_1, headers=headers, verify=False)
    logger.info(response.status_code)
    assert response.status_code == 200
    logger.info(json.dumps(response.json()))
    response = requests.get(url=url+"/comments?postId="+postid, headers=headers, verify=False)
    logger.info(response)
    assert response.status_code == 200
    json_data = json.dumps(response.json())
    logger.info(json_data)