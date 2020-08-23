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
    'hello world' -> 'dlrow olleh'
    :param: my_str(str)

    :return: (str) the input string with characters revered.
    """
    # could simply use python slicing (works on strings as well as lists)
    # return my_str[::-1]

    # print("input: {}".format(my_str))
    reversed_str = ''
    # range(start,stop,step). To iterate from last to first, we use:
    # start = last element in my_str         -> len(my_str) - 1
    # stop  = 'not to go past' first element -> -1
    # step  = 'backwards'                    -> -1
    # (note that strings are zero-indexed. The first char is at my_str[0])
    for index in range(len(my_str)-1, -1, -1):
        reversed_str += my_str[index]
    return reversed_str


def main():
    """main"""
    data = get_data_set()
    for line in data.splitlines():
        rev_line = reverse_string(line)
        print(rev_line)


if __name__ == '__main__':
    main()
