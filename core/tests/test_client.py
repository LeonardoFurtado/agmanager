import pytest


@pytest.mark.django_db
def test_create_profile(api_client):
    data = {
        "name": "Harry Potter",
        "city": "Godric's Hollow",
        "state": "Cornwall",
        "country": "England"
    }
    response = api_client.post('/api/clients/', data=data)
    assert response.status_code == 201


@pytest.mark.django_db
def test_update_profile(api_client, random_client):
    response = api_client.patch('/api/clients/1/', data={'name': "Parry Hotter"})
    assert response.status_code == 200
    assert response.data['name'] == "Parry Hotter"


@pytest.mark.django_db
def test_delete_profile(api_client, random_client):
    response = api_client.delete('/api/clients/1/')
    assert response.status_code == 204
    assert response.data is None


@pytest.mark.django_db
def test_list_clients(api_client, random_client, random_client_2):
    response = api_client.get('/api/clients/')
    assert response.status_code == 200
    assert response.data["count"] == 2


@pytest.mark.django_db
def test_retrieve_client(api_client, random_client):
    response = api_client.get('/api/clients/1/')
    assert response.status_code == 200
    assert response.data["id"] == random_client.id
    assert response.data["name"] == random_client.name
    assert response.data["city"] == random_client.city
    assert response.data["state"] == random_client.state
    assert response.data["country"] == random_client.country

