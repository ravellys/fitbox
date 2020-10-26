import pytest
from django.test import Client


@pytest.fixture
def resp(client: Client):
    resp = client.get('/')
    return resp


def test_status_code(resp):
    assert resp.status_code == 200
