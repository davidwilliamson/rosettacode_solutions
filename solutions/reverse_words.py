#! /usr/bin/env python

"""Reverse words in a (possibly multi-line) string

Reverse the order of all tokens in each of a number of strings and display
the result; the order of characters within a token should not be modified.

Example

Hey you, Bub!   would be shown reversed as:   Bub! you, Hey

https://rosettacode.org/wiki/Reverse_words_in_a_string
"""


def get_data_set():
    """Produce our data set
    :return: (str) a multi-line string of words to reverse
    """
    return """Ice and Fire

fire, in end will world the say Some
ice. in say Some
desire of tasted I've what From
fire. favor who those with hold I

... elided paragraph last ...

Frost Robert"""


def main():
    """main"""
    data = get_data_set()
    for line in data.splitlines():
        rev_line = " ".join([token for token in reversed(line.split())])
        print(rev_line)


if __name__ == '__main__':
    main()
