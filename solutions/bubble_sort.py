#! /usr/bin/env python

"""Bubble sort

https://rosettacode.org/wiki/Sorting_algorithms/Bubble_sort

Sort an array of elements using the bubble sort algorithm.
The elements must have a total order and the index of the array can be of any
discrete type.

Because of its abysmal O(n2) performance, it is not used often for large (or even
medium-sized) datasets.

The bubble sort works by passing sequentially over a list, comparing each value to
the one immediately after it. If the first value is greater than the second, their
positions are switched. Over a number of passes, at most equal to the number of
elements in the list, all of the values drift into their correct positions (large
values "bubble" rapidly toward the end, pushing others down around them). Because
each pass finds the maximum item and puts it at the end, the portion of the list to
be sorted can be reduced at each pass. A boolean variable is used to track whether
any changes have been made in the current pass; when a pass completes without
changing anything, the algorithm exits.

This can be expressed in pseudo-code as follows (assuming 1-based indexing):

repeat
    if itemCount <= 1
        return
    hasChanged := false
    decrement itemCount
    repeat with index from 1 to itemCount
        if (item at index) > (item at (index + 1))
            swap (item at index) with (item at (index + 1))
            hasChanged := true
until hasChanged = false

"""

import random


# Some data types to sort
def random_chars():
    """Return a list of chars 'A' through 'Z' in random order.
    ['C', 'F', ...]
    """
    a_thru_z = [chr(o) for o in range(ord('A'), ord('Z')+1)]
    random.shuffle(a_thru_z)
    return a_thru_z


def random_ints():
    """Return a list of ints in random order"""
    ints = list(range(1, 20))
    random.shuffle(ints)
    return ints


def random_words():
    """Return a list of strings in random order"""
    words = ['able', 'baker', 'dog', 'easy', 'fox', 'george', 'how', 'item']
    random.shuffle(words)
    random.shuffle(words)
    return words


class Shape():
    """Shape
    :param: name (str) name of shape
    :number_of_sides (int) number of sides the shape has.
    """
    def __init__(self, name, number_of_sides):
        self.name = name
        self.sides = number_of_sides

    def __lt__(self, other):
        """implement less than"""
        return self.sides < other.sides

    def __gt__(self, other):
        """implement greater than"""
        return self.sides > other.sides

    def __eq__(self, other):
        """implement equal"""
        return self.sides == other.sides

    def __ne__(self, other):
        """implement not equal"""
        return self.sides != other.sides

    def __str__(self):
        """response to str() """
        return self.name


def random_shapes():
    """Return a list of Shape objects in random order"""
    shapes = [
        Shape('circle', 0),
        Shape('triangle', 3),
        Shape('square', 4),
        Shape('pentagon', 5),
        Shape('hexagon', 6),
        Shape('octogon', 8),
        Shape('enneaogon', 9)
    ]
    random.shuffle(shapes)
    random.shuffle(shapes)
    return shapes


def bubble_sort(data):
    """implement the bubble sort algorithm. Data is sorted in place

    Assumes list elements are all of same type, and elements support
    compare (<, >, =) operations.

    :param: data (list).
    """
    has_changed = True
    item_count = len(data) - 1
    if item_count <= 0:
        return
    # Keep going until no more swaps
    while has_changed is True:
        has_changed = False
        # loop thru a[0], a[1], ... a[n-1]
        for index in range(0, item_count):
            if data[index] > data[index+1]:
                # swap lelements
                temp = data[index]
                data[index] = data[index+1]
                data[index+1] = temp
                has_changed = True


def main():
    """main"""
    for data in [random_chars(), random_ints(), random_words(), random_shapes()]:
        print("\nBefore:\n{0}".format(
            ", ".join([str(x) for x in data])))
        bubble_sort(data)
        print("After :\n{0}".format(
            ", ".join([str(x) for x in data])))


if __name__ == '__main__':
    main()
