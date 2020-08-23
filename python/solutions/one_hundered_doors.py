#! /usr/bin/env python

"""
https://rosettacode.org/wiki/100_doors

There are 100 doors in a row that are all initially closed.

You make 100 passes by the doors.

The first time through, visit every door and toggle the door (if the door is
closed, open it; if it is open, close it).

The second time, only visit every 2nd door (door #2, #4, #6, ...), and toggle it.

The third time, visit every 3rd door (door #3, #6, #9, ...), etc, until you
only visit the 100th door.


Task

Answer the question: what state are the doors in after the last pass? Which are
open, which are closed?
"""


def main():
    """main"""
    num_doors = 100
    opened = True
    closed = False
    doors = [closed for _ in range(0, num_doors)]
    for cycle in range(1, num_doors+1):
        for door in range(0, num_doors, cycle):
            doors[door] = not doors[door]

    open_doors = [door for door in range(0, num_doors) if doors[door] == opened]
    print("{0} open doors: {1}".format(len(open_doors), open_doors))


if __name__ == '__main__':
    main()
