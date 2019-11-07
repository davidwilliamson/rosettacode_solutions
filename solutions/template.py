#!/usr/bin/env python

""" Module docstring here """

import logging
import unittest


LOG_LEVEL = logging.DEBUG


def add(inputs):
    """docstring goes here"""
    logging.debug("Adding %s", inputs)
    return sum(inputs)


class AddTest(unittest.TestCase):
    """Unit test for func"""
    def test_001_functionality(self):
        """AddTest:test_001_functionality"""
        test_cases = [
            {'input': [1, 2], 'expected': 3},
        ]
        for index, test_case in enumerate(test_cases):
            logging.debug("Test %d", index)
            result = add(test_case['input'])
            self.assertEqual(result, test_case['expected'])


if __name__ == '__main__':
    logging.basicConfig(level=LOG_LEVEL, format="%(message)s")
    unittest.main(verbosity=2, failfast=True)
