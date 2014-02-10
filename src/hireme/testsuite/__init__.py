# -*- coding: utf-8 -*-

import flask
import nose
import nose.tools
import werkzeug.test


def ctx_setter(*args, **kwargs):
    """Setup a flask app and request context and pass parameters to the env."""
    from ..server import app_factory

    def setup_ctx():
        app = app_factory()
        app_ctx = flask.ctx.AppContext(app)
        app_ctx.push()

        env = werkzeug.test.EnvironBuilder(*args, **kwargs).get_environ()
        req_ctx = flask.ctx.RequestContext(app, env)
        req_ctx.push()

    return nose.tools.with_setup(setup_ctx)


def main():
    nose.main()


if __name__ == '__main__':
    main()
