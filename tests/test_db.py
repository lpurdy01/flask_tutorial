"""
test_db.py
2023-01-28
Contributors: Levi Purdy
Tests for the db file

Disclaimers: Constructed from the flask tutorial at:
https://flask.palletsprojects.com/en/2.2.x
"""

"""
Import block:
"""

import sqlite3

import pytest
from flaskr.db import get_db


def test_get_close_db(app):
    with app.app_context():
        db = get_db()
        assert db is get_db()

    with pytest.raises(sqlite3.ProgrammingError) as e:
        db.execute('SELECT 1')

    assert 'closed' in str(e.value)


def test_init_db_command(runner, monkeypatch):
    class Recorder(object):
        called = False

    def fake_init_db():
        Recorder.called = True

    monkeypatch.setattr('flaskr.db.init_db', fake_init_db)
    result = runner.invoke(args=['init-db'])
    assert 'Initialized' in result.output
    assert Recorder.called


def my_function():
    print("Python is running!")


if __name__ == '__main__':
    my_function()
