#!/usr/bin/python
# -*- coding: utf-8 -*-

from dicencards.cards import Color, Suite, Rank, Card, BasicValueModel, ValueModel, Deck


def run():
    cards: list[Card] = []
    excluded_ranks = (Rank.ONE, Rank.KNIGHT, Rank.JOKER)
    # TODO: Use generator expression / generator function
    for suite in list(Suite):
        for rank in list(Rank):
            if rank not in excluded_ranks:
                card = Card(rank, suite)
                cards.append(card)
    cards.append(Card(Rank.JOKER, color=Color.BLACK))
    cards.append(Card(Rank.JOKER, color=Color.RED))

    deck = Deck(cards)
    deck.shuffle()
    hand = deck.draw(12)

    print(' |'.join(str(c) for c in hand))
    value_model = BasicValueModel()
    hand = value_model.sort(hand, ValueModel.DESC)
    print(' |'.join(str(c) for c in hand))


if __name__ == '__main__':  # pragma: no coverage
    run()
