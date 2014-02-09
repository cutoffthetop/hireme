# -*- coding: utf-8 -*-

import flask

from tasks import task1, task2


def render_index():
    return flask.render_template('index.html', title='index')


def app_factory():
    app = flask.Flask(import_name=__package__)
    app.add_url_rule('/', 'index', render_index)
    app.add_url_rule('/task1', 'task1', task1.solve, methods=['GET', 'POST'])
    app.add_url_rule('/task2', 'task2', task2.solve, methods=['GET', 'POST'])
    return app


def run_local(*args, **kwargs):
    app = app_factory()
    app.debug = True
    app.run()
