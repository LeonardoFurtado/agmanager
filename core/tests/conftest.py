import pytest
from rest_framework.test import APIClient
from core.models import Customer, Project


@pytest.fixture
def api_client():
    client = APIClient()
    headers = {"HTTP_AUTHORIZATION": f"Token Teste"}
    client.credentials(**headers)
    return client


@pytest.fixture
def random_customer():
    payload = {
        "name": "Harry Potter",
        "city": "Godric's Hollow",
        "state": "Cornwall",
        "country": "England",
        "active": True
    }
    record = Customer.objects.create(**payload)
    return record


@pytest.fixture
def random_customer_2():
    payload = {
        "name": "Albus Dumbledore",
        "city": "Mould-on-the-Wold",
        "state": "Gloucestershire",
        "country": "England",
        "active": True
    }
    record = Client.objects.create(**payload)
    return record
