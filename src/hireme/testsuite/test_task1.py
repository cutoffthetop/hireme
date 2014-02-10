# -*- coding: utf-8 -*-

import json
import os

from nose.tools import assert_raises
from werkzeug.exceptions import BadRequest

from ..task1 import solve
from . import ctx_setter


@ctx_setter(method='POST', data={'input': ''})
def test_too_few_lines():
    expected = 'You need to enter at least 3 lines.'
    with assert_raises(BadRequest) as cm:
        solve()
    assert expected in cm.exception.description


@ctx_setter(method='POST', data={'input': 'A' * 200001 + '\n1\nA'})
def test_too_many_chars():
    expected = 'You need to enter 0 < k < 200000 chars in line 1.'
    with assert_raises(BadRequest) as cm:
        solve()
    assert expected in cm.exception.description


@ctx_setter(method='POST', data={'input': 'A\nA\nA'})
def test_non_int_query_lenght():
    expected = 'The second line must be an integer.'
    with assert_raises(BadRequest) as cm:
        solve()
    assert expected in cm.exception.description


@ctx_setter(method='POST', data={'input': 'A\n2\nA'})
def test_query_too_short():
    expected = 'Less words were provided than specified.'
    with assert_raises(BadRequest) as cm:
        solve()
    assert expected in cm.exception.description


@ctx_setter(method='POST', data={'input': 'A B C\n1\nD'})
def test_nothing_found():
    expected = '<pre>KEIN ABSCHNITT GEFUNDEN</pre>'
    assert expected in solve()


@ctx_setter(method='POST', data={'input': 'A C B A\n2\nA\nB'})
def test_shortest_found():
    expected = '<pre>B A</pre>'
    assert expected in solve()


@ctx_setter(method='POST', data={'input': 'A c b a\n2\na\nB'})
def test_title_case_ignored():
    expected = '<pre>b a</pre>'
    assert expected in solve()


@ctx_setter(method='POST', data={'input': 'A! CŒ § Böb @A\n2\nA\nBB'})
def test_special_chars_ignored():
    expected = '<pre>Bb A</pre>'
    assert expected in solve()


path = os.path.dirname(os.path.abspath(__file__))
sample = json.load(open(path + '/sample_input.json'))['task1']


@ctx_setter(method='POST', data={'input': '\n'.join(sample['input_lines'])})
def test_solve_sample():
    expected = '<pre>%s</pre>' % '\n'.join(sample['output_lines'])
    assert expected in solve()
