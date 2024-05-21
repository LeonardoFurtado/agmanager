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
