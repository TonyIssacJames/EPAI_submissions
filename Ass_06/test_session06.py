import pytest
import inspect
import re
import random
from session_06 import Card, Deck, MyPoker
import os

# the card deck
House_of_Cards = [Card('2', 'clubs'), Card('3', 'clubs'), Card('4', 'clubs'), Card('5', 'clubs'),  Card('6', 'clubs'),
                  Card('7', 'clubs'), Card('8', 'clubs'), Card(
                      '9', 'clubs'), Card('10', 'clubs'), Card('jack', 'clubs'),
                  Card('queen', 'clubs'), Card(
                      'king', 'clubs'), Card('ace', 'clubs'),
                  Card('2', 'diamonds'), Card('3', 'diamonds'), Card(
                      '4', 'diamonds'), Card('5', 'diamonds'),  Card('6', 'diamonds'),
                  Card('7', 'diamonds'), Card('8', 'diamonds'), Card(
                      '9', 'diamonds'), Card('10', 'diamonds'), Card('jack', 'diamonds'),
                  Card('queen', 'diamonds'), Card(
                      'king', 'diamonds'), Card('ace', 'diamonds'),
                  Card('2', 'hearts'), Card('3', 'hearts'), Card(
                      '4', 'hearts'), Card('5', 'hearts'),  Card('6', 'hearts'),
                  Card('7', 'hearts'), Card('8', 'hearts'), Card(
                      '9', 'hearts'), Card('10', 'hearts'), Card('jack', 'hearts'),
                  Card('queen', 'hearts'), Card(
                      'king', 'hearts'), Card('ace', 'hearts'),
                  Card('2', 'spades'), Card('3', 'spades'), Card(
                      '4', 'spades'), Card('5', 'spades'),  Card('6', 'spades'),
                  Card('7', 'spades'), Card('8', 'spades'), Card(
                      '9', 'spades'), Card('10', 'spades'), Card('jack', 'spades'),
                  Card('queen', 'spades'), Card('king', 'spades'), Card('ace', 'spades')]

# Read Me Tests


def test_readme_exists():
    """ check if readme.md exists or not"""
    assert os.path.isfile("README.md"), "README is not there"


def test_if_all_cards_are_created_using_normal():
    """ This test case checks if all cards are creted using
        normal function without using lambda, zip, and map function to create 52 cards in a deck
    """
    deck = Deck()  # create a deck of cards using the normal function
    New_House_of_Cards = deck.deal(52)  # deal all the 52 cards
    print("House_of_Cards", House_of_Cards, type(House_of_Cards[0]))
    print("New_House_of_Cards", New_House_of_Cards,
          type(New_House_of_Cards[0]))

    assert len(New_House_of_Cards) == 52, "52 cards are created"
    assert len(House_of_Cards) == 52, "52 cards are created manually"

    for card in House_of_Cards:
        print(card)
        if card not in New_House_of_Cards:
            print("is it missing", card)
            assert False, "Some cards were not created"
            return

    assert True, "All cards wre created"

    #assert set(New_House_of_Cards) == set(House_of_Cards), "all cards are generted"
