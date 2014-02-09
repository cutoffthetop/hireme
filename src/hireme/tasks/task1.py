# -*- coding: utf-8 -*-

import re

from flask import request
from werkzeug import exceptions
import numpy as np

from . import render_task

@render_task
def solve():
    input_data = request.form.get('input')
    method = request.method
    title = 'task1'

    if method == 'GET':
        return dict(
            title=title
            )

    # TODO: Remove instead of replace special chars.
    paragraphs = input_data.lower().split('\n')

    if len(paragraphs) < 3:
        raise exceptions.BadRequest(
            description='You need to enter at least 3 paragraphs.'
            )

    word_count = re.sub('[^0-9]+', '', paragraphs[1])

    if not word_count.isdigit():
        raise exceptions.BadRequest(
            description='The second paragraph must be an digit.'
            )

    word_count = int(word_count)
    query = set(re.sub('[^a-zA-Z" "]+', '', w) for w in paragraphs[2:])
    text = re.sub('[^a-zA-Z" "]+', '', paragraphs[0])
    text_split = text.split()
    tokens = sorted(set(text_split))

    if word_count != len(query):
        raise exceptions.BadRequest(
            description='Expected %s words, got %s.' % (word_count, len(query))
            )

    text_num = np.array([tokens.index(i) for i in text_split])

    # TODO: Fallback if not all tokens are found.
    # fallback = 'KEIN ABSCHNITT GEFUNDEN'

    occurances = dict()
    for i in query:
        index = tokens.index(i)
        occurance = np.where(text_num == index)[0].tolist()
        occurances[index] = occurance

    global SHORTEST, PATH
    SHORTEST = len(text_split)
    PATH = None

    def find_shortest(path, opt, first, last):
        global SHORTEST, PATH
        if len(opt) == 0:
            if last - first < SHORTEST:
                SHORTEST, PATH = last - first, path
        else:
            for i in opt[0]:
                min_fist = min(i, first)
                max_last = max(i, last)
                if max_last - min_fist > SHORTEST:
                    continue
                find_shortest(path + [i], opt[1:], min_fist, max_last)

    find_shortest([], occurances.values(), SHORTEST, 0)
    solution = '\n'.join(text_split[min(PATH) - 1:max(PATH) + 1])

    return dict(
        input=input_data,
        solution=solution,
        title=title
        )
