import pytest
from rest_framework import status


@pytest.mark.django_db
def test_should_create_activity_if_project_and_customer_are_correctly(api_client, random_project, random_customer):
    data = {
        "title": "Random activity",
        "description": "This is a description",
        "project": random_project.id,
        "customer": random_customer.id,
        "start_date": "2023-10-10",
    }
    response = api_client.post('/api/activities/', data=data)
    assert response.status_code == status.HTTP_201_CREATED
    assert response.json()['title'] == data['title']


@pytest.mark.django_db
def test_should_fail_when_create_activity_with_nonexistent_project(api_client, random_customer):
    data = {
        "title": "Random activity",
        "description": "This is a description",
        "project": 999,
        "customer": random_customer.id,
        "start_date": "2023-10-10",
    }
    response = api_client.post('/api/activities/', data=data)
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert response.data['project'][0] == 'Invalid pk "999" - object does not exist.'


@pytest.mark.django_db
def test_should_fail_when_create_activity_with_nonexistent_customer(api_client, random_project):
    data = {
        "title": "Random activity",
        "description": "This is a description",
        "project": random_project.id,
        "customer": 999,
        "start_date": "2023-10-10",
    }
    response = api_client.post('/api/activities/', data=data)
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert response.data['customer'][0] == 'Invalid pk "999" - object does not exist.'


@pytest.mark.django_db
def test_should_list_activities_if_project_and_customer_are_correctly(api_client, random_project, random_customer, random_activity):
    response = api_client.get(f'/api/customers/{random_customer.id}/projects/{random_project.id}/activities/')
    assert response.status_code == status.HTTP_200_OK
    assert response.data['count'] == 1


@pytest.mark.django_db
def test_should_fail_when_list_activities_if_nonexistent_customer(api_client, random_project, random_activity):
    response = api_client.get(f'/api/customers/999/projects/{random_project.id}/activities/')
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.data['detail'] == 'Customer not found.'


@pytest.mark.django_db
def test_should_fail_when_list_activities_if_nonexistent_project(api_client, random_customer):
    response = api_client.get(f'/api/customers/{random_customer.id}/projects/999/activities/')
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.data['detail'] == 'Project not found for the given customer.'


@pytest.mark.django_db
def test_should_fail_when_list_activities_if_nonexistent_project_on_direct_url(api_client, random_customer):
    response = api_client.get(f'/api/projects/999/activities/')
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.data['detail'] == 'Project not found.'


@pytest.mark.django_db
def test_should_fail_when_create_activity_with_project_from_wrong_customer(api_client, random_project, random_customer, random_customer_2):
    data = {
        "title": "Random activity",
        "description": "This is a description",
        "project": random_project.id,
        "customer": random_customer_2.id,
        "start_date": "2023-10-10",
    }
    response = api_client.post('/api/activities/', data=data)
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.data['detail'] == 'Project not found for the given customer.'
