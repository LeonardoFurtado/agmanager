import pytest
from rest_framework import status


@pytest.mark.django_db
def test_create_profile(api_client):
    data = {
        "name": "Harry Potter",
        "city": "Godric's Hollow",
        "state": "Cornwall",
        "country": "England",
        "active": True
    }
    response = api_client.post('/api/customers/', data=data)
    assert response.status_code == status.HTTP_201_CREATED


@pytest.mark.django_db
def test_update_profile(api_client, random_customer):
    response = api_client.patch('/api/customers/1/', data={'name': "Parry Hotter"})
    assert response.status_code == status.HTTP_200_OK
    assert response.data['name'] == "Parry Hotter"


@pytest.mark.django_db
def test_delete_profile(api_client, random_customer):
    response = api_client.delete('/api/customers/1/')
    assert response.status_code == status.HTTP_204_NO_CONTENT
    assert response.data is None


@pytest.mark.django_db
def test_list_customers(api_client, random_customer, random_customer_2):
    response = api_client.get('/api/customers/')
    assert response.status_code == status.HTTP_200_OK
    assert response.data["count"] == 2


@pytest.mark.django_db
def test_retrieve_customer(api_client, random_customer):
    response = api_client.get('/api/customers/1/')
    assert response.status_code == status.HTTP_200_OK
    assert response.data["id"] == random_customer.id
    assert response.data["name"] == random_customer.name
    assert response.data["city"] == random_customer.city
    assert response.data["state"] == random_customer.state
    assert response.data["country"] == random_customer.country
