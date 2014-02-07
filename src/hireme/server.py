# -*- coding: utf-8 -*-

from tasks import task1, task2
import flask


def index():
    return flask.render_template('index.html', title='index')


def app_factory():
    app = flask.Flask(import_name=__package__)
    app.add_url_rule('/', 'index', index)
    app.add_url_rule('/task1', 'task1', task1.solve)
    app.add_url_rule('/task2', 'task2', task2.solve)
    return app


def run_local(*args, **kwargs):
    app = app_factory()
    app.run()
