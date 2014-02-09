# -*- coding: utf-8 -*-

from flask import render_template
from flask import request


def render_task(func):
    def rendered():
        params = dict(title=func.__module__.split('.')[-1] or '')
        if request.method == 'POST':
            input_data = request.form.get('input')
            params['input_data'] = input_data
            params['solution'] = func(input_data)
        return render_template('task.html', **params)

    return rendered
