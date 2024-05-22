import pytest
from rest_framework import status


@pytest.mark.django_db
def test_create_project(api_client, random_customer):
    data = {
        "name": "Order of the phoenix",
        "description": "Random description",
        "customer": random_customer.id,
        "status": "in_progress",
    }
    response = api_client.post('/api/projects/', data=data)
    assert response.status_code == status.HTTP_201_CREATED


@pytest.mark.django_db
def test_create_should_fail_if_customer_is_inactive(api_client, inactive_customer):
    data = {
        "name": "Order of the phoenix",
        "description": "Random description",
        "customer": inactive_customer.id,
        "status": "in_progress",
    }
    response = api_client.post('/api/projects/', data=data)
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert 'customer' in response.data
    assert response.data['customer'][0] == "The customer is not active."


@pytest.mark.django_db
def test_should_update_project_name(api_client, random_project):
    response = api_client.patch('/api/projects/1/', data={'name': "Not Order of the phoenix"})
    assert response.status_code == status.HTTP_200_OK
    assert response.data['name'] == "Not Order of the phoenix"


@pytest.mark.django_db
def test_should_fail_when_trying_to_change_active_customer_to_inactive_customer(api_client, random_project, inactive_customer):
    response = api_client.patch('/api/projects/1/', data={'customer': inactive_customer.id})
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert response.data['customer'][0] == "The customer is not active."
