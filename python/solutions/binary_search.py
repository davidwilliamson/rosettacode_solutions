#! /usr/bin/env python

"""Binary search

https://rosettacode.org/wiki/Binary_search

A binary search divides a range of values into halves, and continues to narrow
down the field of search until the unknown value is found. It is the classic
example of a "divide and conquer" algorithm.

As an analogy, consider the children's game "guess a number." The scorer has
a secret number, and will only tell the player if their guessed number is higher
than, lower than, or equal to the secret number. The player then uses this
information to guess a new number.

As the player, an optimal strategy for the general case is to start by choosing
the range's midpoint as the guess, and then asking whether the guess was higher,
lower, or equal to the secret number. If the guess was too high, one would select
the point exactly between the range midpoint and the beginning of the range.
If the original guess was too low, one would ask about the point exactly
between the range midpoint and the end of the range. This process repeats until
one has reached the secret number.


Task

Given the starting point of a range, the ending point of a range, and the "secret
value", implement a binary search through a sorted integer array for a certain
number. Implementations can be recursive or iterative (both if you can). Print
out whether or not the number was in the array afterwards. If it was, print
the index also.
"""

import unittest


def binary_search(input_list, search_item):
    """Search for search_item in input_list. Assumes input_list is sorted
    in ascending order, the list is homogonous, and the item is present.

    Note: this is the same as
    return input_list.index(search_item)

    :param: input_list a python list
    :param: search_item an item in the list to locate
    :return: the index (zero based) of the item
    """
    if search_item not in input_list:
        raise ValueError(f"{search_item} not in {input_list}")
    print("given: {0} find {1}".format(input_list, search_item))
    #  0  1  2  3  4
    # [3, 4, 5, 6, 7]
    #        ^
    #        |-- midpoint = 2
    midpoint = int(len(input_list)/2)
    print("midpoint is {0} value is {1}".format(midpoint, input_list[midpoint]))
    if search_item < input_list[midpoint]:
        return binary_search(input_list[0:midpoint], search_item)
    if search_item > input_list[midpoint]:
        # Since we are shrinking the list, must add value of midpoint so we
        # will return the index of the original list, not the shrunken list.
        return (binary_search(input_list[midpoint:len(input_list)], search_item) +
                midpoint)
    return midpoint


class BinarySearchTest(unittest.TestCase):
    """BinarySearchTest"""
    def test_001_binary_search(self):
        """BinarySearchTest:test_001_binary_search"""
        test_cases = [
            {"input": [1, 2, 3, 4, 5, 6, 7], "search_item": 1, "expected": 0},
            {"input": [1, 2, 3, 4, 5, 6, 7], "search_item": 2, "expected": 1},
            {"input": [1, 2, 3, 4, 5, 6, 7], "search_item": 3, "expected": 2},
            {"input": [1, 2, 3, 4, 5, 6, 7], "search_item": 4, "expected": 3},
            {"input": [1, 2, 3, 4, 5, 6, 7], "search_item": 5, "expected": 4},
            {"input": [1, 2, 3, 4, 5, 6, 7], "search_item": 6, "expected": 5},
            {"input": [1, 2, 3, 4, 5, 6, 7], "search_item": 7, "expected": 6},
            # Sparse list
            {"input": [1, 3, 5, 7, 9, 10, 11], "search_item": 5, "expected": 2},
            {"input": [1, 3, 5, 7, 9, 10, 11], "search_item": 9, "expected": 4},
            # List with even number of items
            {"input": [1, 2, 3, 4], "search_item": 2, "expected": 1},
            # List with exactly one item
            {"input": [1], "search_item": 1, "expected": 0},
        ]

        for test_case in test_cases:
            print("\nTest: binary_search({0}, {1})".format(
                test_case['input'], test_case['search_item']))
            result = binary_search(test_case['input'], test_case['search_item'])
            self.assertEqual(result, test_case['expected'])

    def test_002_binary_search_errors(self):
        """BinarySearchTest:test_002_binary_search_errors"""
        test_cases = [
            {"input": [1, 2, 3, 4, 5, 6, 7], "search_item": -1, "expected": 0},
        ]

        for test_case in test_cases:
            print("\nTest: binary_search({0}, {1})".format(
                test_case['input'], test_case['search_item']))
            with self.assertRaises(ValueError) as ctx:
                binary_search(test_case['input'], test_case['search_item'])
            print("got exception {0}".format(str(ctx.exception)))


if __name__ == '__main__':
    unittest.main()
