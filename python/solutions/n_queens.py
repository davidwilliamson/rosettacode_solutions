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
    """Queen is a representation of the quuen
    :param: index (int) used to identify the queen
    """
    # pylint: disable=too-few-public-methods
    def __init__(self, index):
        self.index = index

    def __str__(self):
        return chr(ord('A') + self.index)


class Cell():
    """Cell is a single location on the Board"""
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self._occupant = ""
        self._attacker = ""

    @property
    def free(self):
        """Return True if the cell is neither occupied nor attacked by a Queen"""
        return not self.occupied and not self.attacked

    @property
    def occupied(self):
        """Return True if the cell is currently occupied"""
        return bool(self._occupant)

    @property
    def attacked(self):
        """Return True if the cell can be attacked by another queen"""
        return bool(self._attacker)

    def occupy(self, queen):
        """Place a queen in this Cell"""
        assert not self.occupied, "Occupy: Cell ({0},{1}) occupied by {2}".format(
            self.row, self.col, str(self._occupant))
        assert not self.attacked, "Occupy: Cell ({0},{1}) attacked by {2}".format(
            self.row, self.col, str(self._attacker))
        self._occupant = queen

    def attack(self, queen):
        """Mark this cell as attackable by a Queen"""
        assert not self.occupied, "Attack Cell ({0},{1}) occupied by {2}".format(
            self.row, self.col, str(self._occupant))
        if not self.attacked:
            self._attacker = queen

    @property
    def occupant(self):
        """Return the Queen object that occupies this Cell, if any"""
        return self._occupant

    def __str__(self):
        if self.occupied:
            return 'Q'
        # Debug: this code write the Queen's name if it is occupied,
        # and thelower case letter of the name if it is attacked.
        # if self.occupied:
        #     return str(self._occupant).upper()
        # if self.attacked:
        #     return str(self._attacker).lower()
        return ' '


class Board():
    """
    The chess board.
    :param: size (int) number of rows & columns in the board. (It is square)

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
        """Attempt to place a Queen in a given location on the Board.

        :param: queen . since only one queen may occupy a given column,
                        and the queen's ID is defined as the column the queen
                        occupies, the queen makes the column fixed.
        :param: candidate_row (int) . The corresponding row to try and
                                      place the queen.
        :return: True if the queen was placed
        """
        our_col = queen.index
        if self.tiles[candidate_row][our_col].free:
            our_row = candidate_row
            self.tiles[our_row][our_col].occupy(queen)
            self._attack_rows(queen, our_row, our_col)
            self._attack_cols(queen, our_row, our_col)
            # attack along diagonals
            self._attack_southeast(queen, our_row, our_col)
            self._attack_northeast(queen, our_row, our_col)
            self._attack_southwest(queen, our_row, our_col)
            self._attack_norhtwest(queen, our_row, our_col)
            return True
        return False

    def __str__(self):
        out_str = ''
        for row in range(0, self.size):
            if row != 0:
                out_str += '\n'
            # out_str += '\n' + '+---' * self.size + '+'
            out_str += '+---' * self.size + '+\n|'
            for col in range(0, self.size):
                out_str += ' {} |'.format(str(self.tiles[row][col]))
        out_str += '\n' + '+---' * self.size + '+'
        return out_str

    def _attack_rows(self, queen, our_row, our_col):
        for row in range(0, self.size):
            if row == our_row:
                continue
            self.tiles[row][our_col].attack(queen)

    def _attack_cols(self, queen, our_row, our_col):
        for col in range(0, self.size):
            if col == our_col:
                continue
            self.tiles[our_row][col].attack(queen)

    def _attack_southeast(self, queen, our_row, our_col):
        for row, col in zip([r for r in range(our_row, self.size)],
                            [c for c in range(our_col, self.size)]):
            if row != our_row and col != our_col:
                self.tiles[row][col].attack(queen)

    def _attack_northeast(self, queen, our_row, our_col):
        for row, col in zip([r for r in reversed(range(0, our_row+1))],
                            [c for c in range(our_col, self.size)]):
            if row != our_row and col != our_col:
                self.tiles[row][col].attack(queen)

    def _attack_southwest(self, queen, our_row, our_col):
        for row, col in zip([r for r in range(our_row, self.size)],
                            [c for c in reversed(range(0, our_col+1))]):
            if row != our_row and col != our_col:
                self.tiles[row][col].attack(queen)

    def _attack_norhtwest(self, queen, our_row, our_col):
        for row, col in zip([r for r in reversed(range(0, our_row+1))],
                            [c for c in reversed(range(0, our_col+1))]):
            if row != our_row and col != our_col:
                self.tiles[row][col].attack(queen)


def main():
    """main"""
    size = 5
    solutions = list()
    queens = [Queen(index) for index in range(0, size)]
    active_boards = list()
    # prime the pump with the possible locations for the first queen
    for row in range(0, size):
        this_queen = 0
        next_queen = this_queen + 1
        board = Board(size=size)
        if board.place_queen(queens[this_queen], row):
            active_boards.append(
                {"board": copy.deepcopy(board), "next_queen": next_queen})

    while active_boards:
        board_info = active_boards.pop()
        for row in range(0, size):
            this_queen = queens[board_info["next_queen"]]
            original_board = board_info['board']
            board = copy.deepcopy(original_board)
            next_queen = this_queen.index + 1
            if board.place_queen(this_queen, row):
                if next_queen >= len(queens):
                    solutions.append(board)
                else:
                    active_boards.append(
                        {"board": copy.deepcopy(board), "next_queen": next_queen})
            # else:
                # print("queen {0} cannot place on row {1}".format(
                #     this_queen.index, row))
    print("Board Size of {0}. Solutions:".format(size))
    for index, solution_board in enumerate(solutions):
        print("\nsolution {0} of {1}".format(index+1, len(solutions)))
        print(str(solution_board))


if __name__ == '__main__':
    main()
