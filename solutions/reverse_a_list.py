#! /usr/bin/env python

"""Reverse an list

Given a list, produce a list with the elements reversed

"""

def list_reverser(input_list):
    """list_reverser accepts a python list and returns the reversed
    version of the list

    :param: input_list (list) any python list
    :return: The list in reversed order
    :raises: TypeError if the input parameter is not a list
    """
    if not isinstance(input_list, list):
        raise TypeError("list_reverser: input {0} not a list".format(input_list))
    # could simply use python slicing
    # return input_list[::-1]

    # range(first, last, increment)
    # where 'last' means 'not to exceed'
    # So for an input_list with 3 elements (which has indices 0, 1, 2), produces 2, 1, 0
    return [input_list[index] for index in range(len(input_list)-1, -1, -1)]

    
def main():
    """main is the entrypoint to the program. It takes no arguments
    and does not return anything
    """
    test_cases = [
        {
            "name": "test_001_empty_list",
            "input": [],
            "expected": []
        },
        {
            "name": "test_002_ints",
            "input": [1, 2, 3],
            "expected": [3, 2, 1]
        },
        {
            "name": "test_003_even",
            "input": [1, 2, 3, 4],
            "expected": [4, 3, 2, 1]
        },
        {
            "name": "test_004_nested",
            "input": [1, 2, 3, [4]],
            "expected": [[4], 3, 2, 1]},
    ]
    for test_case in test_cases:
        print(test_case['name'])
        result = list_reverser(test_case['input'])
        assert result == test_case['expected'], "FAIL: Got '{0}' expected {1}'".format(
            result, test_case['expected'])

    

if __name__ == '__main__':
    main()
