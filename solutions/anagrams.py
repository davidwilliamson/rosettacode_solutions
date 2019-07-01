#!/usr/bin/env python

"""Anagrams

https://rosettacode.org/wiki/Anagrams

Task: Using the word list at  http://wiki.puzzlers.org/pub/wordlists/unixdict.txt,
find the sets of words that share the same characters that contain the most words
in them.

Program will read data from a file and print out the word(s) with the largest
number of anagrams.
"""

# defaultdict is our friend here. It behaves like a dict, with the added benefit
# of allowing us to create a default value when a new key is encountered.
# That is, if we insert a new key we can have python automatically create a
# default value for the key (e.g., an empty list, an integer with value of 0)
#
# replaces this code:
# my_list =[('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
# grouped = dict()
# for key, value in my_list:
#     if key in grouped:
#         grouped[key].append(value)
#     else:
#         grouped[key] = [value]
# with:
# grouped = defaultdict(list)
# for key, value in my_list:
#    grouped[key].append(value)
# https://docs.python.org/3.7/library/collections.html#collections.defaultdict
from collections import defaultdict


def get_wordlist(file_name):
    """Read the wordlist from disk. Assumes the words are seperated by newlines:
    bar
    baz
    foo

    :param: file_name (str) full path to the wordlist file on disk.
    :return: generator that produces the next word in the file.
    """
    with open(file_name, 'r') as handle:
        for word in handle:
            yield word.strip()


def main():
    """main"""
    anagrams = defaultdict(list)
    for word in get_wordlist('input_data/unixdict.txt'):
        # anagrams = { 'foo': ['foo', 'oof'], 'bar': ['bar'], ... }
        # sorted(word) will group words by anagram; since sorted(str) returns
        # list and lists aren't hashable, convert it to a tuple. Could also
        # convert back to a string, i.e., "".join(sorted(word))
        anagrams[tuple(sorted(word))].append(word)
    largest_num_of_anagrams = max(len(anagram) for anagram in anagrams.values())
    most_common = [
        word for word in anagrams.values()
        if len(word) >= largest_num_of_anagrams
    ]
    print("Words with the largest number of anagrams in data set:")
    for item in most_common:
        print(str(item))


if __name__ == '__main__':
    main()
