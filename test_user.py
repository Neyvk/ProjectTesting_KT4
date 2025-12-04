import pytest
import requests
import time

url = "https://petstore.swagger.io/v2/user"

@pytest.fixture
def test_user():
    return {
        "id": 88,
        "username": "shpatovich",
        "firstName": "Andrew",
        "lastName": "S",
        "email": "shpatovichad@ithub.ru",
        "password": "12345",
        "phone": "",
        "userStatus": 1
    }

def test_post(test_user):
    time.sleep(1)
    response = requests.post(url, json = test_user)
    assert response.status_code == 200

def test_get(test_user):
    time.sleep(1)
    username = test_user["username"]
    response = requests.get(f"{url}/{username}")
    assert response.status_code == 200

    assert response.json()["username"] == username
    assert response.json()["email"] == test_user["email"]

def test_put(test_user):
    time.sleep(1)
    username = test_user["username"]
    newuser = test_user.copy()
    newuser["firstName"] = "Maomao"
    response = requests.put(f"{url}/{username}", json=newuser)
    assert response.status_code == 200
    get_response = requests.get(f"{url}/{username}")
    time.sleep(3)
    assert get_response.json()["firstName"] == "Maomao"

def test_delete(test_user):
    time.sleep(1)
    username = test_user["username"]
    response = requests.delete(f"{url}/{username}")
    assert response.status_code == 200

    get_response = requests.get(f"{url}/{username}")
    assert get_response.status_code == 404
