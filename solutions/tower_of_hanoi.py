#! /usr/bin/env python

"""Tower of Hanoi

The Tower of Hanoi is a mathematical game or puzzle. It consists of three rods and a number
of disks of different sizes, which can slide onto any rod. The puzzle starts with the
disks in a neat stack in ascending order of size on one rod, the smallest at the
top, thus making a conical shape.

The objective of the puzzle is to move the entire stack to another rod, obeying
the following simple rules:

*   Only one disk can be moved at a time.
*   Each move consists of taking the upper disk from one of the stacks and placing it
      on top of another stack or on an empty rod.
*   No larger disk may be placed on top of a smaller disk.

With 3 disks, the puzzle can be solved in 7 moves. The minimal number of moves required to solve a Tower of Hanoi puzzle is 2n − 1, where n is the number of disks.

The puzzle can be played with any number of disks, although many toy versions have
around 7 to 9 of them.
"""

import pprint

def print_pegs(num_disks, pegs):
    print("------------------------------")
    
    for row in range(num_disks):
        out_str = ''
        for peg in pegs:
            try:
                disk = str(peg[row])
            except IndexError:
                disk = '|'
            out_str += "   " + disk
        print(out_str)


def solved(pegs):
    # we are solved if none of the left-most pegs have any disks
    # (and by corallary, the right most peg has all the disks.)
    return all([len(pegs[peg]) == 0 for peg in range(len(pegs) - 1)]) 
    
def move_disk(from_peg, to_peg):
    disk = from_peg.pop(0)
    to_peg.insert(0, disk)

def top_disk(peg):
    return peg[0]

def legal_move(from_peg, to_peg):
    if not from_peg:
        return False
    if not to_peg:
        return True
    if top_disk(from_peg) < top_disk(to_peg):
        return True
    return False

def move_between_pair_of_pegs(peg_1, peg_2):
    if legal_move(peg_1, peg_2):
        move_disk(peg_1, peg_2)
    elif legal_move(peg_2, peg_1):
        move_disk(peg_2, peg_1)

def main():
    """main"""
    num_disks = 5
    peg_a = list(range(1, num_disks+1))
    peg_b = list()
    peg_c = list()
    print_pegs(num_disks, [peg_a, peg_b, peg_c])
    moves = 0

    if num_disks % 2 == 0:
        while not solved([peg_a, peg_b, peg_c]):
            move_between_pair_of_pegs(peg_a, peg_b)
            moves += 1
            print_pegs(num_disks, [peg_a, peg_b, peg_c])
            if solved([peg_a, peg_b, peg_c]):
                break

            move_between_pair_of_pegs(peg_a, peg_c)
            moves += 1
            print_pegs(num_disks, [peg_a, peg_b, peg_c])
            if solved([peg_a, peg_b, peg_c]):
                break

            move_between_pair_of_pegs(peg_b, peg_c)
            moves += 1
            print_pegs(num_disks, [peg_a, peg_b, peg_c])
            if solved([peg_a, peg_b, peg_c]):
                break

            if moves > 2**num_disks - 1:
                print("Fail {} moves".format(moves))
                break
    else:
        while not solved([peg_a, peg_b, peg_c]):
            move_between_pair_of_pegs(peg_a, peg_c)
            moves += 1
            print_pegs(num_disks, [peg_a, peg_b, peg_c])
            if solved([peg_a, peg_b, peg_c]):
                break

            move_between_pair_of_pegs(peg_a, peg_b)
            moves += 1
            print_pegs(num_disks, [peg_a, peg_b, peg_c])
            if solved([peg_a, peg_b, peg_c]):
                break

            move_between_pair_of_pegs(peg_b, peg_c)
            moves += 1
            print_pegs(num_disks, [peg_a, peg_b, peg_c])
            if solved([peg_a, peg_b, peg_c]):
                break

            if moves > 2**num_disks - 1:
                print("Fail {} moves".format(moves))
                break


if __name__ == '__main__':
    main()
