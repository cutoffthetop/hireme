# -*- coding: utf-8 -*-

from . import render_task

@render_task
def solve():
    return dict(
        solution='42',
        title='task1'
        )