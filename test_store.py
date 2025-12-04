 import pytest
import requests
import time

url = "https://petstore.swagger.io/v2/store/order"

@pytest.fixture
def test_order():
    return {
        "id": 20,
        "petId": 101,
        "quantity": 1,
        "shipDate": "2025-02-02T10:00:00.000Z",
        "status": "placed",
        "complete": True
    }


def test_post(test_order):
    time.sleep(1)
    response = requests.post(url, json=test_order)
    assert response.status_code == 200




def test_get(test_order):
    time.sleep(1)
    order_id = test_order["id"]
    response = requests.get(f"{url}/{order_id}")
    assert response.status_code == 200

    assert response.json()["id"] == 20
    assert response.json()["petId"] == test_order["petId"]


def test_delete(test_order):
    time.sleep(1)
    order_id = test_order["id"]
    response = requests.delete(f"{url}/{order_id}")
    assert response.status_code == 200

    get_response = requests.get(f"{url}/{order_id}")
    assert get_response.status_code == 404


def test_inventory():
    time.sleep(1)
    response = requests.get("https://petstore.swagger.io/v2/store/inventory")
    assert response.status_code == 200

    assert response.json()["available"] > 0
