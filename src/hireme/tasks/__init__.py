# -*- coding: utf-8 -*-

import flask


def render_task(func):
    def rendered():
        params = func()
        if not isinstance(params, dict):
            raise TypeError('Tasks must return data of type dict.')
        return flask.render_template('task.html', **params)
    return rendered
