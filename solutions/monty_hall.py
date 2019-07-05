#! /usr/bin/env python

"""
https://rosettacode.org/wiki/Monty_Hall_problem

Run random simulations of the Monty Hall game. Show the effects of a strategy of
the contestant always keeping his first guess so it can be contrasted with the
strategy of the contestant always switching his guess.

Suppose you're on a game show and you're given the choice of three doors.
Behind one door is a car; behind the others, goats. The car and the goats were
placed randomly behind the doors before the show. The rules of the game show are
as follows:

* After you have chosen a door, the door remains closed for the time being.
* The game show host, Monty Hall, who knows what is behind the doors, now has to
* open one of the two remaining doors, and the door he opens must have a goat
behind it. If both remaining doors have goats behind them, he chooses one randomly.
* After Monty Hall opens a door with a goat, he will ask you to decide whether you
* want to stay with your first choice or to switch to the last remaining door.

Imagine that you chose Door 1 and the host opens Door 3, which has a goat.
He then asks you "Do you want to switch to Door Number 2?" Is it to your advantage
to change your choice?

Note that the player may initially choose any of the three doors (not just Door 1),
that the host opens a different door revealing a goat (not necessarily Door 3),
and that he gives the player a second choice between the two remaining unopened
doors.


Task

Simulate at least a thousand games using three doors for each strategy and show the
results in such a way as to make it easy to compare the effects of each strategy.
"""

import logging
import random
from enum import Enum


class Strategy(Enum):
    """Strategy is an Enum"""
    STAY = 1       # Stay with original choice.
    SWITCH = 2     # Switch to other door.


def play_game(strategy):
    """Play a single game
    :param: strategy a Strategy enum
    :return: True if we won the game, False if we lost
    """
    doors = ['car', 'goat', 'goat']
    # choose a door at random
    choice = random.randint(0, len(doors)-1)
    monty_reveal = [
        door for door in range(0, len(doors))
        if doors[door] == 'goat' and door != choice
    ][0]
    if strategy == Strategy.SWITCH:
        final_decision = [
            door for door in range(0, len(doors))
            if door not in (choice, monty_reveal)
        ][0]
    elif strategy == Strategy.STAY:
        final_decision = choice
    else:
        raise ValueError("Unknown strategy: {0}".format(str(strategy)))
    logging.debug(
        "Doors: %s. Choice %s=%s Monty %s=%s Final %s=%s: %s",
        doors,
        choice, doors[choice],
        monty_reveal, doors[monty_reveal],
        final_decision, doors[final_decision],
        doors[final_decision] == 'car')
    # Decide if we won the car
    return doors[final_decision] == 'car'


def main():
    """main"""

    trials = 5000
    print("Running {0} simulations for each strategy".format(trials))
    switch_results = [play_game(Strategy.SWITCH) for _ in range(0, trials)]
    stay_results = [play_game(Strategy.STAY) for _ in range(0, trials)]
    switch_win_pct = 100.0 * len(
        [res for res in switch_results if res])/len(switch_results)
    stay_win_pct = 100.0 * len(
        [res for res in stay_results if res])/len(stay_results)
    print("Winning percentages:\nStay  : {0:3.1f}\nSwitch: {1:3.1f}".format(
        stay_win_pct, switch_win_pct))


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    main()
