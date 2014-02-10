# -*- coding: utf-8 -*-

import types

from . import ctx_setter
from ..rendering import render_index
from ..rendering import render_task


@ctx_setter()
def test_render_index():
    assert isinstance(render_index(), unicode)


@ctx_setter()
def test_render_task():
    dummy_task = lambda *args, **kwargs: unicode()
    decorated_task = render_task(dummy_task)
    assert isinstance(decorated_task, types.FunctionType)
    assert isinstance(decorated_task(), unicode)
