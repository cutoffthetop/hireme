# -*- coding: utf-8 -*-

import flask

from ..server import app_factory


def test_app_factory():
    app = app_factory()
    assert isinstance(app, flask.Flask)
    assert app.import_name == app_factory.__module__.split('.')[0]
    endpoints = {'index', 'task1', 'task2', 'static'}
    assert set(app.url_map._rules_by_endpoint.keys()) == endpoints
