# -*- coding: utf-8 -*-

import re

from werkzeug.exceptions import BadRequest
import numpy as np

from . import render_task


@render_task
def solve(input_data):

    lines = [re.sub('[^0-9]+', '', i) for i in input_data.split('\n')]
    cases = int(0 if not lines else lines.pop(0))
    counts = [1] * cases

    for case in xrange(cases):
        if not len(lines):
            raise BadRequest('Specified %s cases, but only provided %s.' %
                             (cases, case))

        dimension = int(lines.pop(0))
        matrix = np.array([[int(n) for n in m] for m in lines[:dimension]])
        lines = lines[dimension:]

        if not matrix.shape == (dimension,) * 2:
            raise BadRequest('Expected %s-dimensional matrix for case %s.' %
                             (dimension, case + 1))

        def neighbours(idx):
            def along_axis(axis):
                for offset in (-1, 0, 1):
                    candidate = idx[axis] + offset
                    if candidate >= 0 and candidate < dimension:
                        yield candidate
            hood = []
            for x in along_axis(0):
                for y in along_axis(1):
                    if (x, y) != idx and matrix[x, y] == 1:
                        hood.append((x, y))
            return hood

        untouched = zip(*[idx.tolist() for idx in np.where(matrix == 1)])

        while untouched:
            def expand(resident):
                matrix[resident] = counts[case]
                hood = neighbours(resident)
                if hood:
                    for neighbour in hood:
                        expand(neighbour)

            counts[case] += 1
            expand(untouched[0])
            untouched = zip(*[idx.tolist() for idx in np.where(matrix == 1)])

    return '\n'.join([str(c - 1) for c in counts])
