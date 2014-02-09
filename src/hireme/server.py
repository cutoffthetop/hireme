# -*- coding: utf-8 -*-

import flask

from tasks import task1, task2


def render_index():
    """Render the index page template."""
    return flask.render_template('index.html', title='index')


def app_factory():
    """Create a new Flask instance and configure the URL map."""
    app = flask.Flask(import_name=__package__)
    app.add_url_rule('/', 'index', render_index)
    app.add_url_rule('/task1', 'task1', task1.solve, methods=['GET', 'POST'])
    app.add_url_rule('/task2', 'task2', task2.solve, methods=['GET', 'POST'])
    return app


def run_local(*args, **kwargs):
    """Run the app on a local development server with debugging enabled."""
    app = app_factory()
    app.debug = True
    app.run()
