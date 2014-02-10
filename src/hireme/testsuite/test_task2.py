# -*- coding: utf-8 -*-

import json
import os

from nose.tools import assert_raises
from werkzeug.exceptions import BadRequest

from ..task2 import solve
from . import ctx_setter



@ctx_setter(method='POST', data={'input': ''})
def test_too_few_cases():
    expected = 'You need to enter 0 < T < 6 test cases.'
    with assert_raises(BadRequest) as cm:
        solve()
    assert expected in cm.exception.description


@ctx_setter(method='POST', data={'input': '6'})
def test_too_many_cases():
    expected = 'You need to enter 0 < T < 6 test cases.'
    with assert_raises(BadRequest) as cm:
        solve()
    assert expected in cm.exception.description


@ctx_setter(method='POST', data={'input': '3'})
def test_cases_overspecified():
    expected = 'Specified 3 cases, but only provided 0.'
    with assert_raises(BadRequest) as cm:
        solve()
    assert expected in cm.exception.description


@ctx_setter(method='POST', data={'input': '1\n0'})
def test_matrix_underspecified():
    expected = 'You need to enter 0 < N < 1009 dim. matrices.'
    with assert_raises(BadRequest) as cm:
        solve()
    assert expected in cm.exception.description


@ctx_setter(method='POST', data={'input': '1\n1009'})
def test_matrix_overspecified():
    expected = 'You need to enter 0 < N < 1009 dim. matrices.'
    with assert_raises(BadRequest) as cm:
        solve()
    assert expected in cm.exception.description


@ctx_setter(method='POST', data={'input': '1\n3\n10\n01'})
def test_matrix_overspecified():
    expected = 'Expected uniform 3-D matrix for case 1.'
    with assert_raises(BadRequest) as cm:
        solve()
    assert expected in cm.exception.description


@ctx_setter(method='POST', data={'input': '1\n2\n100\n010\n001'})
def test_matrix_underspecified():
    expected = 'Expected uniform 2-D matrix for case 1.'
    with assert_raises(BadRequest) as cm:
        solve()
    assert expected in cm.exception.description


@ctx_setter(method='POST', data={'input': '1\n3\n111\n00\n100'})
def test_matrix_non_uniform():
    expected = 'Expected uniform 3-D matrix for case 1.'
    with assert_raises(BadRequest) as cm:
        solve()
    assert expected in cm.exception.description


@ctx_setter(method='POST', data={'input': '1\n3\n100\n001\n100'})
def test_clusters_found():
    expected = '<pre>3</pre>'
    assert expected in solve()


path = os.path.dirname(os.path.abspath(__file__))
sample = json.load(open(path + '/sample_input.json'))['task2']


@ctx_setter(method='POST', data={'input': '\n'.join(sample['input_lines'])})
def test_solve_sample():
    expected = '<pre>%s</pre>' % '\n'.join(sample['output_lines'])
    assert expected in solve()
