#! /usr/bin/env python

"""Caesar cipher

https://rosettacode.org/wiki/Caesar_cipher

Implement a Caesar cipher, both encoding and decoding.
The key is an integer from 1 to 25.

This cipher rotates (either towards left or right) the letters of the alphabet
(A to Z).

The encoding replaces each letter with the 1st to 25th next letter in the
alphabet (wrapping Z to A).

So key 2 encrypts "HI" to "JK", but key 20 encrypts "HI" to "BC".

"""

import random


def rot(char, key):
    """rotate character char by key letters
    :param: char (string with exactly one character
    :param: key (int) number of characters to rotate

    :return: the rotated character
    """
    # ord('A') is 65; ord('Z') is 90
    char = char.upper()
    if char > 'Z' or char < 'A':
        return char
    key = key % 26
    rotated = ord(char) + key
    if rotated > ord('Z'):
        #         |- 'zero' -|   |--how far we overshot
        rotated = ord('A') - 1 + (rotated % ord('Z'))
    elif rotated < ord('A'):
        #         |- 'zero' -|   |-how far we undershot
        rotated = ord('Z') + 1 - (ord('A') % rotated)
    return chr(rotated)


def encode(msg, key):
    """encode the message using the key
    :param: msg (str)
    :param: key (int)
    :return: (str) encoded message
    """
    assert key > 0
    return ''.join(rot(char, key) for char in msg)


def decode(encoded, key):
    """decode the message using the key
    :param: encoded (str)
    :param: key (int)
    :return: (str) decoded message
    """
    assert key > 0
    return ''.join(rot(char, -key) for char in encoded)


def main():
    """main"""
    message = 'the quick brown fox jumped over the lazy dog'
    key = random.randint(1, 25)
    print("Key is {0}".format(key))
    secret = encode(message, key)
    decoded = decode(secret, key)
    print("{0} ->\n{1} ->\n{2}".format(message, secret, decoded))


if __name__ == '__main__':
    main()
