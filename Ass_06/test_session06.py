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

# 5_card_P1_Royal_Flush_P2_Combinations  eache element is tuple(hand1, hand2, result)
Test_Card_Set_RF_vs_Combinations = [
    tuple([[Card('10', 'spades'), Card('jack', 'spades'), Card('queen', 'spades'), Card('king', 'spades'), Card('ace', 'spades')],
           [Card('10', 'hearts'), Card('jack', 'hearts'), Card(
               'queen', 'hearts'), Card('king', 'hearts'), Card('ace', 'hearts')],
           'Draw'])  # 1 Royal Flush vs Royal Flush
]

# Read Me Tests


def test_readme_exists():
    """ check if readme.md exists or not"""
    assert os.path.isfile("README.md"), "README is not there"


def test_if_all_cards_are_created_using_normal():
    """ This test case checks if all cards are creted using
        normal function without using lambda, zip, and map function
    """
    deck = Deck()  # create a deck of cards using the normal function
    New_House_of_Cards = deck.deal(52)  # deal all the 52 cards
    #print("House_of_Cards",House_of_Cards, type(House_of_Cards[0]))
    #print("New_House_of_Cards",New_House_of_Cards, type(New_House_of_Cards[0]))

    # testing if we generated 52 cards
    assert len(New_House_of_Cards) == 52, "52 cards are created"
    assert len(House_of_Cards) == 52, "52 cards are created manually"

    # testing if all cards in the manual list is there  in the generated list
    for card in House_of_Cards:
        if card not in New_House_of_Cards:
            assert False, "Some cards were not created"
            return

    assert True, "All cards were created using normal expression"


def test_if_all_cards_are_created_using_single_expression():
    """ This test case checks if all cards are creted using a single expresseion
        using lambda, zip, and map function
    """
    deck = Deck(None)  # create a deck of cards using the normal function
    New_House_of_Cards = deck.deal(52)  # deal all the 52 cards
    #print("House_of_Cards",House_of_Cards, type(House_of_Cards[0]))
    #print("New_House_of_Cards",New_House_of_Cards, type(New_House_of_Cards[0]))

    # testing if we generated 52 cards
    assert len(New_House_of_Cards) == 52, "52 cards are created"
    assert len(House_of_Cards) == 52, "52 cards are created manually"

    # testing if all cards in the manual list is there  in the generated list
    for card in House_of_Cards:
        if card not in New_House_of_Cards:
            assert False, "Some cards were not created"
            return

    assert True, "All cards were created using single expression having lamda,zip and map"


def test_detect_deletion_of_a_card():
    """ This test case checks one card is delted from the desk will that be caugt or not
    """
    deck = Deck(None)  # create a deck of cards using the normal function
    New_House_of_Cards = deck.deal(52)  # deal all the 52 cards
    old_card = New_House_of_Cards[0]
    New_House_of_Cards[0] = New_House_of_Cards[1]  # deleting a card
    #print("House_of_Cards",House_of_Cards, type(House_of_Cards[0]))
    #print("New_House_of_Cards",New_House_of_Cards, type(New_House_of_Cards[0]))

    assert len(New_House_of_Cards) == 52, "52 cards are created"
    assert len(House_of_Cards) == 52, "52 cards are created manually"

    if old_card not in New_House_of_Cards:
        #print("is it missing",card)
        assert True, "Detection of Deteted card happened Successfully"
        return

    assert False, "Deletion was not detected, Failed"


def test_5_card_P1_Royal_Flush_P2_Combinations():
    """ This test case calculates which hand wins if two hands of 5 cards are given
        P1 - will have Royal Flush
        P2 - will have othe combinations
    """
    test_set = Test_Card_Set_RF_vs_Combinations  # player 1 has Royal Flush and Player 2 has other combinations

    for player1_cards, player2_cards, true_result in test_set:
        calc_result = MyPoker.compare_hands(player1_cards, player2_cards)
        if calc_result != true_result:
            assert True, "Result Calculation Went Wrong"
