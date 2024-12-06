import pytest
from utils.apis import APIClient
import uuid

@pytest.fixture(scope="module")
def api_client():
    return APIClient()

def test_get_users(api_client):
    response = api_client.get("users")
    print(response.json())
    assert response.status_code == 200
    assert len(response.json()) > 0

def test_create_users(api_client):
    user_data={
        "name":"laxmi",
        "username":"lax@123",
        "email": "laxpanwar@gmail.com"
    }
    response = api_client.post("users", user_data)
    print(response.json())
    assert response.status_code == 201
    assert response.json()['name']== "laxmi"
    # -- to verify if the data is coming correct or not we will use get method to verify after post
    id = response.json()["id"]
    responseget = api_client.get("users/10")
    print(responseget.json())
    assert responseget.status_code == 200
    assert responseget.json()['name']== "Clementina DuBuque"

def test_update_users(api_client):
    user_data={
        "name":"laxmi pan",
        "username":"lax@123",
        "email": "laxpanwar@gmail.com"
    }
    response = api_client.put("users/1", user_data)
    print(response.json())
    assert response.status_code == 200
    assert response.json()['name']== "laxmi pan"

def test_delete_users(api_client):
    response = api_client.delete("users/1")
    print(response.json())
    assert response.status_code == 200