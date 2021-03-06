# -*- coding: utf-8 -*-

import flask

from . import rendering
from . import task1, task2


def app_factory(*args, **kwargs):
    """Create a new Flask instance and configure the URL map."""
    app = flask.Flask(import_name=__package__)
    app.add_url_rule('/', 'index', rendering.render_index)
    app.add_url_rule('/task1', 'task1', task1.solve, methods=['GET', 'POST'])
    app.add_url_rule('/task2', 'task2', task2.solve, methods=['GET', 'POST'])
    return app


def run_local(*args, **kwargs):
    """Run the app on a local development server with debugging enabled."""
    app = app_factory()
    app.debug = True
    app.run()
