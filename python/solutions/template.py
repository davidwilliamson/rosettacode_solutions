#!/usr/bin/env python

"""module DOCSTRING goes here """

import logging
import unittest


def sut_func(inputs):
    """func DOCSTRING goes here """
    logging.debug("inputs %s", inputs)
    result = sum(inputs)
    logging.debug("result %s", str(result))
    return result


class FooTest(unittest.TestCase):
    """class DOCSTRING goes here """
    def test_001_functionality(self):
        """func DOCSTRING goes here """
        # table driven test cases
        test_cases = [
            {'input': [1, 2], 'expected': 3},
        ]
        for index, test_case in enumerate(test_cases):
            logging.debug("Test %d", index)
            result = sut_func(test_case['input'])
            self.assertEqual(result, test_case['expected'])


if __name__ == '__main__':
    LOG_LEVEL = logging.DEBUG
    logging.basicConfig(level=LOG_LEVEL, format="%(message)s")
    unittest.main(verbosity=2, failfast=True)
