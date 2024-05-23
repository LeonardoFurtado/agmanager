import pytest
from rest_framework.test import APIClient
from core.models import Customer, Project, Activity


@pytest.fixture
def api_client():
    client = APIClient()
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
    record = Customer.objects.create(**payload)
    return record


@pytest.fixture
def inactive_customer():
    payload = {
        "name": "Harry Potter",
        "city": "Godric's Hollow",
        "state": "Cornwall",
        "country": "England",
        "active": False
    }
    record = Customer.objects.create(**payload)
    return record


@pytest.fixture
def random_project(random_customer):
    payload = {
        "name": "Order of the phoenix",
        "description": "Random description",
        "customer": random_customer,
        "status": "in_progress",
    }
    record = Project.objects.create(**payload)
    return record


@pytest.fixture
def completed_project(random_customer):
    payload = {
        "name": "completed project",
        "description": "Random description",
        "customer": random_customer,
        "status": "completed",
    }
    record = Project.objects.create(**payload)
    return record


@pytest.fixture
def random_activity(random_customer, random_project):
    data = {
        "title": "Random activity",
        "description": "This is a description",
        "project": random_project,
        "customer": random_customer,
        "start_date": "2023-10-10",
    }
    record = Activity.objects.create(**data)
    return record

