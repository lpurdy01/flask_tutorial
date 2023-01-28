"""
__init__.py
2023-01-28
Contributors: Levi Purdy
Inits the flaskr app

Disclaimers: Constructed from the flask tutorial at:
https://flask.palletsprojects.com/en/2.2.x/tutorial/database/

"""

"""
Import block:
"""

import os

from flask import Flask


def create_app(test_config=None):
    """
    Create and configure an instance of the Flask application.
    :param test_config:
    :return:
    """

    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # register the database commands
    from . import db
    db.init_app(app)

    # register the auth blueprint
    from . import auth
    app.register_blueprint(auth.bp)

    # register the blog blueprint
    from . import blog
    app.register_blueprint(blog.bp)
    app.add_url_rule('/', endpoint='index')

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    return app