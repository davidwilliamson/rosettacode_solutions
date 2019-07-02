#! /usr/bin/env python

"""Reverse characters in a string

https://rosettacode.org/wiki/Reverse_a_string

let's do this the old-school way: no using reversed() or string slices
"""


def get_data_set():
    """Produce our data set
    :return: (str) a multi-line string of words to reverse
    """
    return """Fire and Ice

Some say the world will end in fire,
Some say in ice.
From what I've tasted of desire
I hold with those who favor fire.

... last paragraph elided ...

Robert Frost"""


def reverse_string(my_str):
    """Reverse a string

    Uses C-style indexing instead of reversed()
    :param: my_str(str)

    :return: (str) the input string with characters revered.
    """
    # print("input: {}".format(my_str))
    reversed_str = list()
    for index in range(0, len(my_str)):
        # print("{0}/{1} : {2}".format(index, len(my_str)-1, my_str[index]))
        reversed_str.append(my_str[len(my_str) - 1 - index])
    return "".join(reversed_str)


def main():
    """main"""
    data = get_data_set()
    for line in data.splitlines():
        rev_line = reverse_string(line)
        print(rev_line)


if __name__ == '__main__':
    main()
