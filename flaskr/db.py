"""
db.py
2023-01-28
Contributors: Levi Purdy
Handles the interaction with the database

Disclaimers: Constructed from the flask tutorial at:
https://flask.palletsprojects.com/en/2.2.x/tutorial/database/
"""

"""
Import block:
"""
import sqlite3

import click
from flask import current_app, g


def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row

    return g.db


def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()


def my_function():
    print("Python is running!")


if __name__ == '__main__':
    my_function()
