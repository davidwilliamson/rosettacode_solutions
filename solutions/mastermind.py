#! /usr/bin/env python

"""Mastermind

https://rosettacode.org/wiki/Mastermind

Create a simple version of the board game: Mastermind.
https://en.wikipedia.org/wiki/Mastermind_(board_game)

It must be possible to:

* choose  the number of colors will be used in the game (2 - 20)
* choose the color code length (4 - 10)
* choose the maximum number of guesses the player has (7 - 20)
* choose whether or not will be repeated colors in the code


The game should display all the player guesses and the results of that guess.

Display
Feature 	            Text Version
Player guess                Alphabet letters
Correct color & position    X
Correct color 	            O
None 	                    -

A text version example:
1: ADEF - XXO-
^  ^^^^   ^^^^
|   |      |
|   |      result: two correct colors and spot,
|   |              one correct color/wrong spot one color is not in the code.
|   +----- the four colors(ADEF)
+--------- first guess

-------------------------------------------
Gameplay and rules

The game is played using:

* a decoding board, with a shield at one end covering a row of four large holes,
  and twelve (or ten, or eight, or six) additional rows containing four large
  holes next to a set of four small holes;
* code pegs of six different colors (or more; see Variations below), with round
  heads, which will be placed in the large holes on the board; and
* key pegs, some colored black, some white, which are flat-headed and smaller
  than the code pegs; they will be placed in the small holes on the board.

The codemaker chooses a pattern of four code pegs. Duplicates and blanks are
allowed depending on player choice, so the player could even choose four code
pegs of the same color.

The codebreaker tries to guess the pattern, in both order and color, within
twelve (or ten, or eight) turns.

If there are duplicate colours in the guess, they cannot all be awarded a key peg
unless they correspond to the same number of duplicate colours in the hidden
code. For example, if the hidden code is white-white-black-black and the player
guesses white-white-white-black, the codemaker will award two colored key pegs
for the two correct whites, nothing for the third white as there is not a third
white in the code, and a colored key peg for the black. No indication is given
of the fact that the code also includes a second black.

Once feedback is provided, another guess is made; guesses and feedback continue
to alternate until either the codebreaker guesses correctly, or twelve (or ten,
or eight) incorrect guesses are made.

-------------------------------------------

Algorithms

With four pegs and six colors, there are 6**4 = 1296 different patterns (allowing
duplicate colors).

In 1977, Donald Knuth demonstrated that the codebreaker can solve the pattern
in five moves or fewer, using an algorithm that progressively reduced the numbe
of possible patterns.
"""


def main():
    """main"""
    raise NotImplementedError("Mastermind is WIP")


if __name__ == '__main__':
    main()
