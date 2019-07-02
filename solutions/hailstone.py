#! /usr/bin/env python

"""Hailstone Sequence

https://rosettacode.org/wiki/Hailstone_sequence

The Hailstone sequence of numbers can be generated from a starting positive
integer, n by:

*  If  n  is   1    then the sequence ends.
*  If  n  is   even then the next n of the sequence = n/2
*  If  n  is   odd  then the next n of the sequence = (3 * n) + 1

Task

1. Create a routine to generate the hailstone sequence for a number.
2. Use the routine to show that the hailstone sequence for the number 27 has
   112 elements starting with 27, 82, 41, 124 and ending with 8, 4, 2, 1
3. Show the number less than 100,000 which has the longest hailstone sequence
   together with that sequence's length.
"""

import time


def generate_hailstones(start):
    """Generate the hailstone sequence for a given number.
    :param: start (int) a positive integer
    :return; list of int.
    """
    assert start > 0, "Start must be a positive integer. got {}".format(start)
    num = start
    hailstones = [start]
    while num != 1:
        if num % 2 == 0:
            # even
            num = int(num / 2)
        else:
            # odd
            num = (3 * num) + 1
        hailstones.append(num)
    return hailstones


def stones_stats(start, hailstones):
    """print stats about the list of hailstones"""
    print("{0:5d} : Found {1} stones. Starting: {2} Ending: {3}".format(
        start,
        len(hailstones),
        ", ".join([str(stone) for stone in hailstones[:4]]),
        ", ".join([str(stone) for stone in hailstones[-4:]])))


def main():
    """main"""

    # Task 2
    test_value = 27
    hailstones = generate_hailstones(test_value)
    stones_stats(test_value, hailstones)
    assert len(hailstones) == 112, "{0} should have 122 stones got {1}".format(
        test_value, len(hailstones))

    # Task 3
    # Note that timing tests show that this approach executes as fast as the
    # accepted approach (below). On python 3.7.1 (1.8 GHz Core i5)
    # both algorithms require approx. 3.75 seconds +/- .05 seconds to cmplete.
    start_time = time.perf_counter()
    most_stones = 0
    input_for_most_stones = 0
    limit = 100000
    for test_value in range(1, limit):
        hailstones = generate_hailstones(test_value)
        if len(hailstones) > most_stones:
            input_for_most_stones = test_value
            most_stones = len(hailstones)
    elapsed_time_seconds = time.perf_counter() - start_time
    print("Most stones: {0} ({1} elements) Compute time {2:5.2f} secs".format(
        input_for_most_stones, most_stones, elapsed_time_seconds))

    # This is the accepted solution for python. It is clearly more compact,
    # although (arguably) less obvious, since max() is applied to a list of tuples
    # and one must know that the default sort key for a tuple is the zeroeth
    # element. That is, this use of max() only works becuase we ordered the list of
    # tuples so that they are (length-of-list, val), and not (val, length-of-list)
    start_time = time.perf_counter()
    most_stones = max(
        (len(generate_hailstones(val)), val)
        for val in range(1, limit)
    )
    elapsed_time_seconds = time.perf_counter() - start_time
    print("Most stones: {1} ({0} elements) Compute time {2:5.2f} secs".format(
        *most_stones, elapsed_time_seconds))


if __name__ == '__main__':
    main()
