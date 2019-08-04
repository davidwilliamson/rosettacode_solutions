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


DEBUG = False


def debug(msg):
    """Poor man's debug logging"""
    if DEBUG:
        print(msg)


def binary_search(mylist, choice):
    """do a binary search

    :param: mylist (list) a sorted list of ints
    :param: choice the int we are tryng to locate in mylist

    :return: (int) the location in mylist where choice is found.
    """
    # TODO check this algorithm for correctness
    midpoint = int(len(mylist) / 2)
    previous = len(mylist)
    done = False
    tries = 0
    while not done:
        tries += 1
        debug("{0} Midpoint: {1} Choice {2}".format(tries, midpoint, choice))
        if mylist[midpoint] == choice:
            print("{0} tries: {1} is mylist[{2}] == {3}".format(
                tries, choice, midpoint, mylist[midpoint]))
            done = True
        else:
            window = max(1, int(abs(previous - midpoint) / 2))
            previous = midpoint
            debug("window: {0} previous: {1} midpoint {2}".format(
                window, previous, midpoint))
            if mylist[midpoint] < choice:
                midpoint = midpoint + window
            elif mylist[midpoint] > choice:
                midpoint = midpoint - window
        if tries > 10:
            raise Exception("Search for {0} failed".format(choice))
    return midpoint


def main():
    """main"""
    mylist = list(range(1, 21, 2))
    for choice in mylist:
        print("\n{0}\nChoice is {1}".format('-' * 20, choice))
        binary_search(mylist, choice)


if __name__ == '__main__':
    main()
