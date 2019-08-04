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
|   |      result: two correct colors and spot   (XX)
|   |              one correct color/wrong spot  (O)
|   |              one color is not in the code. (-)
|   +----- Guess: the four colors (ADEF)
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


import random
from collections import Counter


# ['A', 'B', 'C' ... 'Z']
ALL_PEGS = [chr(letter) for letter in range(ord('A'), ord('Z') + 1)]


def generate_code(num_colors, code_length):
    """Generate a new secret code.
    :return: (str)
    """
    # limit to first num_colors. i.e., ['A', 'B', 'C']
    peg_choices = ALL_PEGS[:num_colors]
    # a string, e.g., "FEDD"
    return "".join([random.choice(peg_choices) for _ in range(code_length)])


def _count_correct_color_and_spot(code, guess):
    results = Counter([code[i] == guess[i] for i in range(len(code))])
    return results[True] if True in results else 0


def _count_correct_color(code, guess):
    code_bins = Counter(code)
    guess_bins = Counter(guess)
    correct_color_count = 0
    for key in guess_bins:
        if key in code_bins:
            correct_color_count += min(code_bins[key], guess_bins[key])
    return correct_color_count


def score_guess(code, guess):
    """Score the guess.

    :return: (str) of 'X', 'O' and '-'
    """
    correct = _count_correct_color_and_spot(code, guess)
    color_only = _count_correct_color(code, guess)
    # color_only includes correct (color and location are right).
    # since we want the additional items that have color correct but
    # not the location, subtract off the correct count
    partially_correct = color_only - correct
    incorrect = len(code) - color_only
    return 'X' * correct + 'O' * partially_correct + '-' * incorrect


def is_winner(code, guess):
    """Return True if the guess matches the code exactly"""
    return score_guess(code, guess) == 'X' * len(code)


def get_guess(num_colors, code_length):
    """Prompt user for guess and validate their entry

    :return: a validated guess
    """
    happy = False
    peg_choices = ALL_PEGS[:num_colors]
    while not happy:
        print("\nChoose {0} chars from '{1}' (duplicates allowed)".format(
            code_length, ', '.join(peg_choices)))
        guess = input("Enter guess -> ")
        guess = str(guess).upper()
        if len(guess) != code_length:
            print("{0} should be {1} chars".format(guess, code_length))
            continue
        happy = all([guess[i] in peg_choices for i in range(code_length)])
    return guess


def play_one_game(num_colors, code_length, max_guesses):
    """Play one game.

    :return: True if the player won
    """
    code = generate_code(num_colors, code_length)
    # print(code)
    guesses = 1
    while guesses < max_guesses:
        guess = get_guess(num_colors, code_length)
        score = score_guess(code, guess)
        if is_winner(code, guess):
            print("{0} == {1} WINNER!!".format(code, guess))
            return True
        print("{0:2d}: {1} = {2}".format(guesses, guess, score))
        guesses += 1
    print("You lose. Code was {0}".format(code))
    return False


def main():
    """main"""
    # Number of different colored pegs
    num_colors = 6
    # How many pegs are in the code
    code_length = 4
    # how many incorrect guesses before player loses.
    max_guesses = 10
    play_one_game(num_colors, code_length, max_guesses)


if __name__ == '__main__':
    main()
