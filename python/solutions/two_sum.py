#! /usr/bin/env python

"""two-sum

https://leetcode.com/problems/two-sum/

Given an array of integers, return indices of the two numbers such that they
add up to a specific target.

You may assume that each input would have exactly one solution, and you may
not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""


def test_result(input_array, target, expected_result):
    """Test our solution.
    :param: input_array (list of int)
    :param: target (int)
    :param: expected_result (int)

    :return: bool.
    """
    result = sum([input_array[index] for index in expected_result])
    return result == target


def find_two_sum(input_array, target):
    """find two elements in input_array that sum to target.
    :param: input_array (list of int)
    :param: target (int)

    :return: list of int. The indices of input_array whose elements
                          sum to target.
    :raise: AssertionError if no soluiton found
    """
    for i, first in enumerate(input_array):
        for j, second in enumerate(input_array):
            if first == second:
                continue
            if first + second == target:
                print("{0} + {1} == {2}".format(first, second, target))
                return [i, j]
    # should not happen per assumptions of problem.
    raise AssertionError("No solution found")


def main():
    """main"""
    test_data = [
        {"input": [2, 7, 11, 15], "target": 9},
        {"input": [11, 2, 15, 7], "target": 9},
        {"input": [11, 2, 15, 7], "target": 17}
    ]
    for test in test_data:
        solution = find_two_sum(test['input'], test['target'])
        assert test_result(test['input'], test['target'], solution)


if __name__ == '__main__':
    main()
