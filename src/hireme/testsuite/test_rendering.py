# -*- coding: utf-8 -*-

import types

from nose.tools import with_setup
import flask
import werkzeug.test

from ..rendering import render_index
from ..rendering import render_task
from ..server import app_factory


def setup_func():
    app = app_factory()
    app_ctx = flask.ctx.AppContext(app)
    app_ctx.push()

    builder = werkzeug.test.EnvironBuilder(
        method='POST',
        data={'input': 'Lorem ipsum dolor set.'}
        )
    env = builder.get_environ()
    req_ctx = flask.ctx.RequestContext(app, env)
    req_ctx.push()


@with_setup(setup_func)
def test_render_index():
    assert isinstance(render_index(), basestring)


@with_setup(setup_func)
def test_render_task():
    dummy_task = lambda *args, **kwargs: ''
    decorated_task = render_task(dummy_task)
    assert isinstance(decorated_task, types.FunctionType)
    assert isinstance(decorated_task(), basestring)
