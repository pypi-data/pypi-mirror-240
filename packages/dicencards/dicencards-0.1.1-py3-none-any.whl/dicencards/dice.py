# -*- coding: utf-8 -*-
"""
.. module:: dice
    :synopsis: an easy way to make dice rolls

.. moduleauthor:: Xavier ROY <xavier@regbuddy.eu>
"""

import random

BEST_OF_DICE = 'BEST_OF'

SUM_OF_DICE = 'SUM'

SCORES = 'SCORES'

BUST = 'BUST'

HIT = 'HIT'

UNLIMITED_REROLL: int = -1

NO_REROLL: int = 0


class Die:
    """
    A class to represent a die.
    """

    def __init__(self, side_count: int):
        """
        Constructs a die instance
        :param side_count: the number of sides on the die
        :type side_count: int
       """
        self.side_count = side_count

    def __str__(self):
        """
        Constructs the character string representing the die
        :return: the representation string
        :rtype: int
        """
        return f'D{self.side_count}'

    def roll(self, on_max_reroll: int = NO_REROLL, on_min_reroll: int = NO_REROLL) -> int:
        """
        Make a die roll

        If the roll is open on the minimum or maximum values of the 1st result, a retry is performed as many times as allowed by the on_max_reroll and on_min_reroll parameters.
        If the 1st result has reached the maximum value of the die, the following re-rolls are added to the initial result.
        If the 1st result matches the minimum value of the die (normally 1), the following throws are added together and then subtracted from the initial result.

        :param on_max_reroll: the maximum number of times the die can be re-rolled when the result hits to the die's maximum value.
        :type on_max_reroll: int
        :param on_min_reroll: the maximum number of times the die can be re-rolled when the 1st result matches the minimum value of the die.
        :type on_min_reroll: int
        :return: the result of the roll
        :rtype: int
        """
        score = random.randint(1, self.side_count)
        if score == self.side_count and on_max_reroll != 0:
            score = score + self.roll(on_max_reroll - 1, 0)
        elif score == 1 and on_min_reroll != 0:
            score = score - self.roll(on_min_reroll - 1, 0)
        return score


D2 = Die(2)
D4 = Die(4)
D6 = Die(6)
D8 = Die(8)
D10 = Die(10)
D12 = Die(12)
D20 = Die(20)
D100 = Die(100)


class BunchOfDice:
    """
    A class to represent a bunch of dice of the same type.
    """

    def __init__(self, number_of_dice: int, die_type: int = 6):
        """
        Constructs the character string representing an instance of the class
        :param number_of_dice: the number of dice in the bunch
        :type number_of_dice:int
        :param die_type: the number of faces of each die in the bunch
        :type die_type: int
       ²"""
        self.dice = []
        self._die_type = die_type
        for i in range(0, number_of_dice):
            self.dice.append(Die(die_type))

    def __str__(self):
        """
        Constructs the character string representing the bunch of dice
        :return: the representation string
        :rtype: str
        """
        return f'{len(self.dice)}D{self._die_type}'

    def count_dice(self) -> int:
        """
        Counts dice in the bunch
        :return: the number of dice in the bunch
        :rtype: int
        """
        return len(self.dice)

    def roll(self, on_max_reroll=NO_REROLL, on_min_reroll=NO_REROLL) -> dict:
        """
        Make roll for all dice in the bunch

        See :func:`dicecacrds.dice.Die.roll` for re-roll behavior description.

        :param on_max_reroll: the maximum number of times the die can be re-rolled when the result hits to the die's maximum value.
        :type on_max_reroll: int
        :param on_min_reroll: the maximum number of times the die can be re-rolled when the 1st result matches the minimum value of the die.
        :type on_min_reroll: int
        :return: the result of the roll
        :rtype dict
        """
        scores = []
        hit_count = 0
        bust_count = 0
        for die in self.dice:
            score = die.roll(on_max_reroll, on_min_reroll)
            if score <= 1:
                bust_count += 1
            elif score >= die.side_count:
                hit_count += 1
            scores.append(score)
        scores = sorted(scores)
        return {SCORES: scores, SUM_OF_DICE: sum(scores), BEST_OF_DICE: max(scores), HIT: hit_count, BUST: bust_count}
