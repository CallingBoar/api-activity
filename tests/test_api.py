# first import built in fixtures, then third parties, then your own

import pytest
from api_activity.app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_hello(client):
    response = client.get('/')
    assert response.status_code == 200
    assert response.json == {'message': 'Hello World!'}

def test_square(client):
    response = client.get('/square/12')
    assert response.status_code == 200
    assert response.json == {"Shape": "Square", "Area": 144}

def test_echo(client):
    response = client.get('/echo?arg1=oooohletsgo&arg2=itworked')
    assert response.status_code == 200
    assert response.json == {
    "arg1": "oooohletsgo",
    "arg2": "itworked"
    }