import pytest
import requests
import time

url = "https://petstore.swagger.io/v2/pet"

@pytest.fixture
def test_pet():
    return {
        "id": 101,
        "category": {"id": 1, "name": "dogs"},
        "name": "Rex",
        "photoUrls": ["https://example.com/rex.jpg"],
        "tags": [{"id": 1, "name": "friendly"}],
        "status": "available"
    }


def test_post(test_pet):
    time.sleep(1)
    response = requests.post(url, json = test_pet)
    assert response.status_code == 200

def test_get(test_pet):
    time.sleep(1)
    id = test_pet["id"]
    response = requests.get(f"{url}/{id}")
    assert response.status_code == 200

    assert response.json()["id"] == 101
    assert response.json()["name"] == test_pet["name"]

def test_put(test_pet):
    time.sleep(1)
    newpet = test_pet.copy()
    newpet["name"] = "Max"
    response = requests.put(url, json=newpet)
    assert response.status_code == 200
    get_response = requests.get(f"{url}/{test_pet['id']}")
    time.sleep(1)
    assert get_response.json()["name"] == "Max"

def test_delete(test_pet):
    time.sleep(1)
    pet = test_pet["id"]
    response = requests.delete(f"{url}/{pet}")
    assert response.status_code == 200

    get_response = requests.get(f"{url}/{pet}")
    assert get_response.status_code == 404
