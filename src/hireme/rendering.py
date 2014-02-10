# -*- coding: utf-8 -*-

from flask import render_template
from flask import request


def render_index():
    """Render the index page template."""
    return render_template('index.html', title='index')


def render_task(func):
    """Decorator for task solving functions. Provides raw form data from the
    request and expects a string formatted return value."""

    def rendered():
        params = dict(title=func.__module__.split('.')[-1] or '')
        if request.method == 'POST':
            input_data = request.values.get('input')
            params['input'] = input_data
            params['solution'] = func(input_data)
        return render_template('task.html', **params)

    return rendered
