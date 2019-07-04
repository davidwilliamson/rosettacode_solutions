#! /usr/bin/env python

"""N-Queens problem

https://en.wikipedia.org/wiki/Eight_queens_puzzle

The eight queens puzzle has 92 distinct solutions. If solutions that differ
only by the symmetry operations of rotation and reflection of the board are
counted as one, the puzzle has 12 solutions. 

The following tables give the number of solutions for placing n queens on an
n×n board, both fundamental (sequence A002562 in the OEIS) and all (sequence
A000170 in the OEIS), for n = 1–10

n             1     2     3     4     5     6     7     8     9     10     ...
fundamental   1     0     0     1     2     1     6    12    46     92     ...
all           1     0     0     2    10     4    40    92   352    724     ...
"""

import copy


class Queen():
    def __init__(self, index):
        self.index = index
    def __str__(self):
        return chr(ord('A') + self.index)

class Cell():
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self._occupant = ""
        self._attacker = ""

    @property
    def free(self):
        return not self.occupied and not self.attacked

    @property
    def occupied(self):
        return bool(self._occupant)

    @property
    def attacked(self):
        return bool(self._attacker)

    def occupy(self, queen):
        assert not self.occupied, "Occupy: Cell ({0},{1}) already occupied by {2}".format(
            self.row, self.col, str(self._occupant))
        assert not self.attacked, "Occupy: Cell ({0},{1}) already attacked by {2}".format(
            self.row, self.col, str(self._attacker))
        self._occupant = queen
    def attack(self, queen):
        assert not self.occupied, "Attack Cell ({0},{1}) already occupied by {2}".format(
            self.row, self.col, str(self._occupant))
        if not self.attacked:
            self._attacker = queen
    @property
    def occupant(self):
        return self._occupant

    def __str__(self):
        if self.occupied:
            return str(self._occupant).upper()
        #if self.attacked:
        #    return str(self._attacker).lower()
        return ' '


class Board():
    """
    tiles[row][col] is:

    [['0,0', '0,1', '0,2', '0,3'],
     ['1,0', '1,1', '1,2', '1,3'],
     ['2,0', '2,1', '2,2', '2,3'],
     ['3,0', '3,1', '3,2', '3,3']]
    """
    def __init__(self, size=8):
        self.size = size
        self.tiles = [
            [Cell(row, col) for col in range(0, self.size)]
            for row in range(0, self.size)
        ]
    def place_queen(self, queen, candidate_row=0):
        our_col = queen.index
        placed = False
        if self.tiles[candidate_row][our_col].free:
            our_row = candidate_row
            self.tiles[our_row][our_col].occupy(queen)
            # attack all rows in our column
            for row in range(0, self.size):
                if row == our_row:
                    continue
                self.tiles[row][our_col].attack(queen)
            # attack all columns in our row
            for col in range(0, self.size):
                if col == our_col:
                    continue
                self.tiles[our_row][col].attack(queen)
            # TODO attack diagonals
            return True
        return False

    def __str__(self):
        out_str = ''
        for row in range(0, self.size):
            out_str += '\n' + '+---' * self.size + '+'
            out_str += '\n|'
            for col in range(0, self.size):
                out_str += ' {} |'.format(str(self.tiles[row][col]))
        out_str += '\n' + '+---' * self.size + '+'
        return out_str

def main():
    """main"""
    """
    every time we place a queen, make a copy of the board.
      save the board, and the index of the NEXT queen.
      if there are no more queens to place, it is a solution.
    if we fail to place a queen in any row, throw away the board 
    as long as there are saved boards:
        resume trying to place the next queen, starting with the first row.    
      

    """
    size = 4
    solutions = list()
    queens = [Queen(index) for index in range(0, size)]
    active_boards = list()
    # prime the pump with the possible locations for the first queen
    for row in range(0, size):
        this_queen = 0
        next_queen = this_queen + 1
        board = Board(size=size)
        if board.place_queen(queens[this_queen], row):
            active_boards.append({"board": copy.deepcopy(board), "next_queen": next_queen})

    while active_boards:
        print("------------------------------------------------------------")
        print("Active boards: {}".format(len(active_boards)))
        board_info = active_boards.pop()
        for row in range(0, size):
            this_queen = queens[board_info["next_queen"]]
            original_board = board_info['board']
            board = copy.deepcopy(original_board)
            print("queen {0} trying row {1}".format(this_queen.index, row))
            # print(str(board))
            next_queen = this_queen.index + 1
            if board.place_queen(this_queen, row):
                if next_queen >= len(queens):
                    print("queen {0} got a solution (row {1})".format(this_queen.index, row))
                    # print(str(board))
                    solutions.append(board)
                else:
                    print("Queen {0} appending board for queen {1}".format(this_queen.index, next_queen))
                    # print(str(board))
                    active_boards.append({"board": copy.deepcopy(board), "next_queen": next_queen})
            else:
                print("queen {0} cannot place on row {1}".format(this_queen.index, row))
    print("solutions:")
    for solution_board in solutions:
        print(str(solution_board))

if __name__ == '__main__':
    main()
