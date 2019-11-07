#! /usr/bin/env python

"""Reverse an list

Given a list, produce a list with the elements reversed

"""
import unittest
import logging


LOG_LEVEL = logging.INFO


def list_reverser(input_list):
    """list_reverser accepts a python list and returns the reversed
    version of the list. if the input is a string, will return a reversed
    string.

    :param: input_list (list) any python list
    :return: The list in reversed order
    :raises: TypeError if the input parameter is not a list
    """
    if not isinstance(input_list, (str, list)):
        raise TypeError("list_reverser: input {0} not a list".format(input_list))
    # could simply use python slicing
    # return input_list[::-1]

    # range(first, last, increment)
    # where 'last' means 'not to exceed'
    # For an input_list with 3 elements (has indices 0, 1, 2), produces 2, 1, 0
    reversed_list = [input_list[index]
                     for index in range(len(input_list)-1, -1, -1)]
    if isinstance(input_list, str):
        return "".join(reversed_list)
    return reversed_list


class ListReverserTest(unittest.TestCase):
    """Unit test cases for the list_reverser func"""
    def test_001_positive_cases(self):
        """ListReverserTest:test_positive_cases"""
        test_cases = [
            {"input": [], "expected": []},
            {"input": [1], "expected": [1]},
            {"input": [1, 2, 3], "expected": [3, 2, 1]},
            {"input": [1, 2, 3, 4], "expected": [4, 3, 2, 1]},
            {"input": [1, 2, 3, [4]], "expected": [[4], 3, 2, 1]},
            {"input": ["foo", 3, [1]], "expected": [[1], 3, "foo"]},
            {"input": "hello world", "expected": "dlrow olleh"},
        ]
        for index, test_case in enumerate(test_cases):
            result = list_reverser(test_case['input'])
            logging.debug(
                "test %d | input: %s, result: %s expected: %s",
                index, test_case['input'], result, test_case['expected'])
            self.assertEqual(result, test_case['expected'])

    def test_002_negative_cases(self):
        """ListReverserTest:test_negative_cases"""
        test_cases = [
            3,
            -1,
            set([1, 2, 3])
        ]
        for index, test_case in enumerate(test_cases):
            logging.debug(
                "test %d | input %s should raise an exception",
                index, str(test_case))
            with self.assertRaises(TypeError):
                _ = list_reverser(test_case)


if __name__ == '__main__':
    logging.basicConfig(level=LOG_LEVEL, format="%(message)s")
    unittest.main(verbosity=5, failfast=False)
