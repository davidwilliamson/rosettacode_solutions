#! /usr/bin/env python

"""Merge two lists

Given two sorted lists, merge list 2 into list 1

"""

import unittest


def merge_lists(list_1, list_2):
    """Given two lists, both sorted, merge the elements of list 2 into list 1,
    producting a single sorted list. 

    Note: alters the contents of both list_1 and list-2!
          list_1 is the resulting merged list, and list_2 is empty.
    """
    print("\nMerge {0} into {1}".format(list_2, list_1))
    print("Merge {0} items into {1} item list".format(len(list_2), len(list_1)))
    print("O(n^2) would be: {0} operations".format(o_nsq(list_1, list_2)))
    # use operations to determine algorithmic complexity
    operations = 0
    # The current index into list_1 where we are checking to insert.
    lower_bound = 0
    while list_2:
        # pop() is destructive. list_2 shrinks each time we call this.
        item = list_2.pop(0)
        merged = False
        # Figure out where to insert this item.
        # We use lower_bound to track where in list_1 we are currently looking.
        # That is, since list_1 is sorted, we don't need to start at the front of
        # list_1 each time.
        for index in range(lower_bound, len(list_1)):
            operations += 1
            if item < list_1[index]:
                list_1.insert(index, item)
                # lower bound is the place *after* where we inserted.
                # That is, we inserted at index, so index + 1 is the
                # next spot to check (the item after the one we just inserted)
                # print(list_1)
                lower_bound = index + 1
                merged = True
                break
        if not merged:
            # Current item and all remaining elements of list_2 can be placed at
            # the end of list_1 and we are done.
            list_1 += [item] + list_2
            break
    print("result ({0} ops): {1}".format(operations, list_1))
    return list_1


def o_nsq(list_1, list_2):
    """A simple example of O(n^2).

    :return: the number of operations required to traverse a nested for loop
    involving both lists
    """
    operations = 0
    for _ in list_1:
        for _ in list_2:
            operations += 1
    return operations


class MergeListsTest(unittest.TestCase):
    """MergeListsTest"""
    def test_001_merge_list2_into_list1(self):
        """test_001_merges"""
        test_cases = [
            # insert at start, append at end
            {
                "list1": [2, 4, 6, 8],
                "list2": [1, 3, 5, 7, 9, 10, 11],
                "expected": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
            },
            # no insert at start, append at end
            {
                "list1": [2, 4, 6, 8],
                "list2": [3, 5, 7, 9],
                "expected": [2, 3, 4, 5, 6, 7, 8, 9]
            },
            # list 2 ends up inside list 1
            {
                "list1": [2, 4, 6, 8],
                "list2": [3, 5, 7],
                "expected": [2, 3, 4, 5, 6, 7, 8]
            },
            # consecutive list2 elements to insert
            {
                "list1": [2, 8],
                "list2": [3, 4, 5, 6, 7],
                "expected": [2, 3, 4, 5, 6, 7, 8]
            },
            # multiple list1 elements to skip
            {
                "list1": [2, 3, 4, 5, 6, 8],
                "list2": [1, 7],
                "expected": [1, 2, 3, 4, 5, 6, 7, 8]
            },
        ]

        for test_case in test_cases:
            result = merge_lists(test_case['list1'], test_case['list2'])
            self.assertEqual(test_case['expected'], result)


if __name__ == '__main__':
    unittest.main()
