# -*- coding: utf-8 -*-

import re

from werkzeug.exceptions import BadRequest
import numpy as np

from . import render_task


@render_task
def solve(input_data):
    """Solve task 1 in accordance to the ZON code ninja program task sheet."""

    # Split the input data by linebreaks.
    lines = input_data.split('\n')

    if len(lines) < 3:
        raise BadRequest('You need to enter at least 3 lines.')

    # Enforce character limit constraint.
    if len(lines[0]) == 0 or len(lines[0]) > 200000:
        raise BadRequest('You need to enter 0 < k < 200000 chars in line 1.')

    # Normalize the text of the first line and extract unique tokens.
    text = re.sub('[^a-zA-Z" "]+', '', lines[0])
    text_list = text.lower().split()
    tokens = sorted(set(text_list))

    # Normalize the query words and insure they match the specified amount.
    try:
        query_len = int(lines[1])
    except ValueError:
        raise BadRequest('The second paragraph must be an digit.')

    query = [re.sub('[^a-zA-Z" "]+', '', i.lower()) for i in lines[2:]]

    if query_len != len(query):
        raise BadRequest('Less words were provided than specified.')

    # Convert the text to a numerical numpy array for faster comparisons.
    text_vector = np.array([tokens.index(i) for i in text_list])

    # Use single value lists to escape closure scope.
    SHORTEST, PATH = [len(text_list)], [None]

    def find_shortest(path, opt, first, last):
        # Recursively traverse options tree to find the shortest path.
        if len(opt) == 0:
            if last - first < SHORTEST[0]:
                SHORTEST[0], PATH[0] = last - first, path
        else:
            for i in opt[0]:
                min_fist = min(i, first)
                max_last = max(i, last)
                if max_last - min_fist > SHORTEST[0]:
                    continue
                find_shortest(path + [i], opt[1:], min_fist, max_last)

    # Determine the occurances of query words in the text vector.
    occurances = []
    for i in query:
        if i not in tokens:
            return 'KEIN ABSCHNITT GEFUNDEN'
        occurances.append(np.where(text_vector == tokens.index(i))[0].tolist())

    find_shortest([], occurances, SHORTEST[0], 0)

    return ' '.join(text.split()[min(PATH[0]):max(PATH[0]) + 1])
