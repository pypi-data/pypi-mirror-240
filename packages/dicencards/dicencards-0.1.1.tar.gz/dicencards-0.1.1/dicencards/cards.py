# -*- coding: utf-8 -*-
"""
.. module:: cards
    :synopsis: an easy way to make card drawing

.. moduleauthor:: Xavier ROY <xavier@regbuddy.eu>
"""

import random
from enum import Enum
from collections import namedtuple
from dataclasses import dataclass, field


class TupleSymbol(namedtuple('TupleSymbol', ['name', 'glyph'])):

    def __str__(self):
        return f'{self.name}: {self.glyph}'


class TupleColor(namedtuple('TupleColor', ['name', 'repr', 'rgb', 'ansi'])):

    def __str__(self):
        return f'{self.name}: #{self.rgb}'


class TupleSuite(namedtuple('TupleSuite', ['symbol', 'color'])):

    def __str__(self):
        return f'{self.symbol.name}: {self.color.ansi}{self.symbol.glyph}\033[39m'


class TupleRank(namedtuple('TupleRank', ['name', 'order', 'repr'])):

    def __str__(self):
        return f'{self.name}: {self.order}'


class Symbol(Enum):
    CLUBS = TupleSymbol('club', '\u2663')
    DIAMONDS = TupleSymbol('diamonds', '\u2666')
    HEARTS = TupleSymbol('hearts', '\u2665')
    SPADES = TupleSymbol('spades', '\u2660')

    def glyph(self):
        return self.value.glyph

    def __str__(self):
        return str(self.value)


class Color(Enum):
    BLACK = TupleColor('black', 'B', '000000', '\033[30m')
    RED = TupleColor('red', 'R', 'FF0000', '\033[31m')

    def ansi(self):
        return self.value.ansi

    def rgb(self):
        return self.value.rgb

    def __str__(self):
        # return f'{self.value.ansi}{self.name}\0033[m'
        return self.value.repr


class Suite(Enum):
    CLUBS = TupleSuite(Symbol.CLUBS, Color.BLACK)
    DIAMONDS = TupleSuite(Symbol.DIAMONDS, Color.RED)
    HEARTS = TupleSuite(Symbol.HEARTS, Color.RED)
    SPADES = TupleSuite(Symbol.SPADES, Color.BLACK)

    def symbol(self) -> Symbol:
        return self.value.symbol

    def color(self) -> Color:
        return self.value.color

    def glyph(self):
        return self.value.symbol.glyph()

    def colored_glyph(self):
        return f'{self.color().ansi()}{self.glyph()}\033[39m'

    def __str__(self):
        return self.colored_glyph()


class Rank(Enum):
    ONE = TupleRank('one', 1, '1')
    TWO = TupleRank('two', 2, '2')
    THREE = TupleRank('three', 3, '3')
    FOUR = TupleRank('four', 4, '4')
    FIVE = TupleRank('five', 5, '5')
    SIX = TupleRank('six', 6, '6')
    SEVEN = TupleRank('seven', 7, '7')
    EIGHT = TupleRank('eight', 8, '8')
    NINE = TupleRank('nine', 9, '9')
    TEN = TupleRank('ten', 10, '10')
    JACK = TupleRank('jack', 11, 'J')
    KNIGHT = TupleRank('knight', 12, 'C')
    QUEEN = TupleRank('queen', 13, 'Q')
    KING = TupleRank('king', 14, 'K')
    ACE = TupleRank('ace', 15, 'A')
    JOKER = TupleRank('joker', 20, 'Jo')

    def __str__(self):
        return str(self.value.repr)


@dataclass
class Card:
    rank: Rank
    suite: Suite = field(default=None)
    color: Color = field(default=None)

    def __post_init__(self):
        # TODO: Tester la cohérence
        if self.suite is not None:
            self.color = self.suite.color()

    def __eq__(self, other):
        return self.rank == other.rank and self.suite == other.suite

    def __str__(self):
        if self.suite is None:
            s = f'{self.rank}{self.color}'.rjust(3)
        else:
            s = f'{self.rank}{self.suite}'.rjust(3)
        return s


class CardValueModel:
    ASC = 1
    DESC = -1

    def __init__(self):
        pass

    def evaluate(self, card: Card):
        raise NotImplementedError()

    def compare(self, c1: Card, c2: Card):
        c1_val = self.evaluate(c1)
        c2_val = self.evaluate(c2)
        if c1_val > c2_val:
            return 1
        elif c1_val < c2_val:
            return -1
        else:
            return 0

    def sort(self, cards: list[Card], order=ASC) -> list[Card]:
        evaluated_cards = []
        for card in cards:
            evaluated_cards.append((card, self.evaluate(card)))
        evaluated_cards = sorted(evaluated_cards, key=lambda c: c[1])
        # print(' | '.join('{}={}'.format(str(c[0]), c[1]) for c in evaluated_cards))
        sorted_card = []
        for evaluated_card in evaluated_cards:
            sorted_card.append(evaluated_card[0])
        if order == CardValueModel.DESC:
            sorted_card.reverse()
        return sorted_card

    def get_rank_value(self, rank: Rank):
        raise NotImplementedError()

    def get_suite_value(self, suite: Suite):
        raise NotImplementedError()


class Deck:

    def __init__(self, cards: list[Card]):
        self.cards: list[Card] = cards

    def __str__(self):
        return ' |'.join(str(c) for c in self.cards)

    def shuffle(self):
        random.shuffle(self.cards)

    def draw(self, n: int) -> list[Card]:
        subset: list[Card] = []
        i = 0
        while i < n:
            subset.append(self.cards.pop(0))
            i += 1
        return subset

    def count(self):
        """Count cards in the deck"""
        return len(self.cards)

    def sort(self, value_model: CardValueModel, order: int = CardValueModel.ASC):
        """Sorts the cards in the deck regarding the specified value model"""
        self.cards = value_model.sort(self.cards, order)


class HandStatus(Enum):
    OK = "Ok"
    OVERLOAD = "Overload"
    LACK = "Lack"

    def __str__(self):
        return self.value


class Hand:

    def __init__(self, cards: list[Card], max_size: int = None, min_size: int = 0):
        if cards is None:
            self.cards: list[Card] = []
        else:
            self.cards: list[Card] = cards[:]
        self.max_size: int = max_size
        self.min_size = min_size
        self.state = self._compute_state()

    def __str__(self):
        s = '\t'.join(str(c) for c in self.cards)
        return f'{s} ({self.state})'

    def append(self, card: Card):
        if len(self.cards) <= self.max_size:
            self.cards.append(card)
            self.state = self._compute_state()
        else:
            raise ValueError("Hand has reached its max size")

    def remove(self, card: Card):
        self.cards.remove(card)
        self.state = self._compute_state()

    def pop(self, i: int) -> Card:
        outgoing_card: Card = self.cards.pop(i)
        self.state = self._compute_state()
        return outgoing_card

    def change(self, i: int, incoming_card: Card) -> Card:
        outgoing_card: Card = self.cards[i]
        self.cards[i] = incoming_card
        return outgoing_card

    def sort(self, value_model: CardValueModel, order: int = CardValueModel.ASC):
        """Sorts the cards in the deck regarding the specified value model"""
        self.cards = value_model.sort(self.cards, order)

    def _compute_state(self) -> HandStatus:
        status = HandStatus.OK
        hand_size = len(self.cards)
        if hand_size < self.min_size:
            status = HandStatus.LACK
        elif self.max_size is not None and hand_size > self.max_size:
            status = HandStatus.OVERLOAD
        return status


class DeckModel:

    def __init__(self, excluded_ranks: set[Rank], number_of_card_packs: int = 1):
        self.excluded_ranks: set[Rank] = excluded_ranks
        self.number_of_card_packs: int = number_of_card_packs

    def build_deck(self) -> Deck:
        cards: list[Card] = self._build_card_pack() * self.number_of_card_packs
        deck = Deck(cards)
        return deck

    def _build_card_pack(self) -> list[Card]:
        cards: list[Card] = []
        for suite in list(Suite):
            for rank in list(Rank):
                if rank not in self.excluded_ranks:
                    card = Card(rank, suite)
                    cards.append(card)
        return cards


FIFTY_TWO_CARD_DECK_MODEL = DeckModel({Rank.ONE, Rank.KNIGHT, Rank.JOKER})

THIRTY_TWO_CARD_DECK_MODEL = DeckModel(
    {Rank.ONE, Rank.TWO, Rank.THREE, Rank.FOUR, Rank.FIVE, Rank.SIX, Rank.SEVEN, Rank.KNIGHT, Rank.JOKER})


class BasicCardValueModel(CardValueModel):

    def __init__(self, excluded_ranks: set[Rank] = None):
        super().__init__()
        excluded_ranks = {} if excluded_ranks is None else excluded_ranks
        self.model = {}
        value = 1
        for rank in list(Rank):
            if rank not in excluded_ranks:
                self.model[rank] = value
                value += 1

    def evaluate(self, card: Card):
        return self.get_rank_value(card.rank) * self.get_suite_value(card.suite)

    def get_rank_value(self, rank: Rank):
        return self.model.get(rank, 0)

    def get_suite_value(self, suite: Suite):
        return 1


class HandRankValueModel:

    def __init__(self):
        pass

    def evaluate(self, hand: Hand):
        raise NotImplementedError()

    def compare(self, h1: Hand, h2: Hand):
        c1_val = self.evaluate(h1)
        c2_val = self.evaluate(h2)
        if c1_val > c2_val:
            return 1
        elif c1_val < c2_val:
            return -1
        else:
            return 0
