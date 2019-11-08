#!/usr/bin/env python

"""
 determine the array element(s) at specified indices
"""

import logging
import unittest


LOG_LEVEL = logging.DEBUG


def list_indices(input_list, indices):
    """determine the value of input_list at the specified indices
    example:
                         0    1    2    3
    given input_list = ['a', 'b', 'c', 'd']
    and indices = [0, 3]
    return [input_list[0], input_list[3]] = ['a', 'd']
    """
    logging.debug("list %s indices %s", input_list, indices)
    # sanity check inputs:
    if not isinstance(input_list, list) or not input_list:
        raise TypeError("input list must be a list. got {0}".format(input_list))
    if not isinstance(indices, list):
        raise TypeError("indices must be a list. Got {0}".format(indices))
    if not all([isinstance(index, int) for index in indices]):
        raise ValueError("indices must be integers got {0}".format(indices))
    # results = []
    # for index in indices:
    #    index = index % len(input_list)
    #    results.append(input_list[index])
    results = [input_list[index % len(input_list)] for index in indices]
    logging.debug("result: %s", results)
    return results


class ListIndicesTest(unittest.TestCase):
    def test_001_functionality(self):
        test_cases = [
            # basic happy path
            {"list": ['a', 'b', 'c', ], "indices": [0, 2], "expected": ['a', 'c']},
            # single index
            {"list": [1, 2, 3, 4], "indices": [1], "expected": [2]},
            # empty indices
            {"list": [1, 2, 3, 4], "indices": [], "expected": []},
            # indices wrap around in positive sense
            {"list": [1, 2, 3, 4], "indices": [0, 7], "expected": [1, 4]},
            # indices wrap around in negative sense
            {"list": [1, 2, 3, 4], "indices": [-4, 7], "expected": [1, 4]},
            # single list element
            {"list": [1], "indices": [0, 4365, -1305], "expected": [1, 1, 1]},
        ]
        for index, test_case in enumerate(test_cases):
            logging.debug("Test %d", index)
            result = list_indices(test_case['list'], test_case['indices'])
            self.assertEqual(result, test_case['expected'])

    def test_002_invalid_inputs(self):
        test_cases = [
            # input list is not a list
            {"list": 'x', "indices": [0], "type": TypeError},
            # input list is empty list
            {"list": [], "indices": [0], "type": TypeError},
            # indices are not a list
            {"list": ['x'], "indices": 3, "type": TypeError},
            # indices is a list, but list elelements are not ints
            {"list": ['x'], "indices": ['a'], "type": ValueError},
        ]
        for index, test_case in enumerate(test_cases):
            logging.debug("Test %d", index)
            with self.assertRaises(test_case['type']) as exc:
                _ = list_indices(test_case['list'], test_case['indices'])
            logging.debug("Caught exception: %s", str(exc.exception))


if __name__ == '__main__':
    logging.basicConfig(level=LOG_LEVEL, format="%(message)s")
    unittest.main(verbosity=2, failfast=True)
