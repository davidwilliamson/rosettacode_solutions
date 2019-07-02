#! /usr/bin/env python

"""Sleep Sort

In general, sleep sort works by starting a separate task for each item to be
sorted, where each task sleeps for an interval corresponding to the item's sort
key, then emits the item. Items are then collected sequentially in time.

Task: Write a program that implements sleep sort. Have it accept non-negative
integers on the command line and print the integers in sorted order. If this
is not idomatic in your language or environment, input and output may be done
differently.

https://rosettacode.org/wiki/Sorting_algorithms/Sleep_sort

"""

# https://docs.python.org/3.7/library/concurrent.futures.html
import random
import time
import concurrent.futures


def generate_random_list():
    """Generate a list of integers on range 1..20 with no duplicates
    :return: list of integers
    """
    rand_list = [num for num in range(1, 21)]
    random.shuffle(rand_list)
    return rand_list


def do_sleep(delay):
    """sleep for a the specified delay. When the delay is over, we quietly return.

    :param: delay (int) Amount of time to sleep in 10th's of a second.
                        So delay=20 means sleep 0.2 seconds (200 msec)
    :return: the input (int)
    """
    delay_msec = float(delay)/10.0
    time.sleep(delay_msec)
    return delay


def list_to_str(items):
    """A convenience function to convert a list to a comma seperated string.

    [1, 2, 3, 4] -> '1, 2, 3, 4'
    :param: a list. This program uses list of ints.
    :return: a string, with commas seperating the list elements
    """
    return ", ".join([str(item) for item in items])


def main():
    """main"""
    random_ints = generate_random_list()
    print("inputs: {}".format(list_to_str(random_ints)))
    print("GO!")
    sorted_ints = list()
    # This is the sleep sort. We start a thread for every element in the random_ints
    # list, and collect the output (which is the integer input each thread was
    # given to sleep on) from each thread as it completes.
    num_workers = len(random_ints)
    with concurrent.futures.ThreadPoolExecutor(max_workers=num_workers) as executor:
        # dict of {executor: delay, ...}
        runner_map = {executor.submit(do_sleep, val): val for val in random_ints}
        # Since every delay is different, the threads will complete at different
        # times. We collect each thread in the order they complete, and end up
        # with a sorted list.
        for future in concurrent.futures.as_completed(runner_map):
            # We could just capture the value of this dict element (which is the
            # delay for this completed thread) but let's use the returned result
            # from the thread, (which is also the value of the delay)
            # sorted_ints.append(runner[future])
            sorted_ints.append(future.result())
    print("sorted: {}".format(list_to_str(sorted_ints)))


if __name__ == '__main__':
    main()
