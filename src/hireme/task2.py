# -*- coding: utf-8 -*-

import re

from werkzeug.exceptions import BadRequest
import numpy as np

from .rendering import render_task


@render_task
def solve(input_data):
    """Solve task 2 in accordance to the ZON code ninja program task sheet."""

    # Clean input data and split by linebreaks.
    lines = [re.sub('[^0-9]+', '', i) for i in input_data.split('\n')]

    # Determine number of test cases and init solution list.
    cases = int(0 if not lines else lines.pop(0))
    counts = [1] * cases

    # Enforce test case limit constraint.
    if cases <= 0 or cases >= 6:
        raise BadRequest('You need to enter 0 < T < 6 test cases.')

    for case in xrange(cases):
        if not len(lines):
            raise BadRequest('Specified %s cases, but only provided %s.' %
                             (cases, case))

        dimension = int(lines.pop(0))

        # Enforce dimensional constraint.
        if dimension <= 0 or dimension >= 1009:
            raise BadRequest('You need to enter 0 < N < 1009 dim. matrices.')

        # The line array is consumed according to the dimension spec.
        matrix = np.array([[int(n) for n in m] for m in lines[:dimension]])
        lines = lines[dimension:]
        cluster_ids = []

        if not matrix.shape == (dimension,) * 2:
            raise BadRequest('Expected %s-D matrix for case %s, got %s.' %
                             (dimension, case + 1, matrix.shape))

        def neighbours(idx, cluster_id):
            # Return all 1s in the up to 8 fields adjacent to idx.
            def along_axis(axis):
                # Discover candidate fields based on matrix dimensionality.
                for offset in (-1, 0, 1):
                    candidate = idx[axis] + offset
                    if candidate >= 0 and candidate < dimension:
                        yield candidate
            hood = []
            for x in along_axis(0):
                for y in along_axis(1):
                    if (x, y) != idx and matrix[x, y] == 1:
                        hood.append((x, y))
                    elif matrix[x, y] > 1 and matrix[x, y] != cluster_id:
                        # Claim fields of neighbouring cluster.
                        if matrix[x, y] in cluster_ids:
                            del cluster_ids[cluster_ids.index(matrix[x, y])]
                        matrix[matrix == matrix[x, y]] == cluster_id
            return hood

        # Generate initial list of fields with value 1.
        untouched = zip(*[idx.tolist() for idx in np.where(matrix == 1)])

        while untouched:
            cluster_ids
            # Every cluster gets an ID, which is stored in the matrix instead
            # of the value 1. Therefore, we loop until there are only zeroes
            # and cluster IDs left.
            def expand(resident, cluster_id):
                matrix[resident] = cluster_id #counts[case]
                hood = neighbours(resident, cluster_id)
                if hood:
                    for neighbour in hood:
                        try:
                            expand(neighbour, cluster_id)
                        except RuntimeError:
                            # Incase we run into recursion depth issues, let
                            # the next iteration handle this neighbourhood.
                            return

            # Increase cluster ID and recursivly explore neighbours.
            cluster_ids.append(max(cluster_ids or [1]) + 1)
            expand(untouched[0], cluster_ids[-1])

            # Recalculate list of fields with value 1.
            untouched = zip(*[idx.tolist() for idx in np.where(matrix == 1)])

        counts[case] = len(cluster_ids)

    return '\n'.join([str(c) for c in counts])
