import json
import pytest
from unittest.mock import patch
from rest_framework.test import APIClient
from core.models import Client


@pytest.fixture
def api_client():
    client = APIClient()
    headers = {"HTTP_AUTHORIZATION": f"Token Teste"}
    client.credentials(**headers)
    return client


@pytest.fixture
def random_client():
    payload = {
        "name": "Harry Potter",
        "city": "Godric's Hollow",
        "state": "Cornwall",
        "country": "England"
    }
    record = Client.objects.create(**payload)
    return record
