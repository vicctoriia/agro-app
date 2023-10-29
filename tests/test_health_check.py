from http import HTTPStatus

from ward import test

from tests.fixtures import client


@test('Should return status code 200')
def _(client=client):
    assert client.get('/health-check').status_code == HTTPStatus.OK


@test('Should return expected message')
def _(client=client):
    assert client.get('/health-check').json == {'status': 'Ok'}
