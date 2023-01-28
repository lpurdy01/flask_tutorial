"""
test_factory.py
2023-01-28
Contributors: Levi Purdy
Test factory

Disclaimers:Constructed from the flask tutorial at:
https://flask.palletsprojects.com/en/2.2.x
"""

"""
Import block:
"""

from flaskr import create_app


def test_config():
    assert not create_app().testing
    assert create_app({'TESTING': True}).testing


def test_hello(client):
    response = client.get('/hello')
    assert response.data == b'Hello, World!'




def my_function():
    print("Python is running!")


if __name__ == '__main__':
    my_function()
