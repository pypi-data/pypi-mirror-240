#!/usr/bin/python
# -*- coding: utf-8 -*-

from dicencards.dice import D4, D6, D20, BunchOfDice, BEST_OF_DICE, SUM_OF_DICE, SCORES, BUST, HIT

MAX_REROLL = 10
MIN_REROLL = 0


def run():
    bunch = BunchOfDice(10, 4)

    result = bunch.roll(MAX_REROLL, MIN_REROLL)
    print(result[SCORES])

    print('Best of dice -> {}'.format(result[BEST_OF_DICE]))
    print('Sum of dice -> {}'.format(result[SUM_OF_DICE]))
    print('Busts -> {}'.format(result[BUST]))
    print('Hits -> {}'.format(result[HIT]))


if __name__ == '__main__':  # pragma: no coverage
    run()
