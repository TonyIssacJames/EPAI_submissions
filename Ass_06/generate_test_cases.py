import inspect
import re
import random
from session_06 import Card, Deck, MyPoker
import os


import logging

Test_Card_Set_RF_vs_Combinations = [
                                    tuple(  [[Card('10','spades'), Card('jack','spades'), Card('queen','spades'), Card('king','spades'), Card('ace','spades')],
                                            [Card('10','hearts'), Card('jack','hearts'), Card('queen','hearts'), Card('king','hearts'), Card('ace','hearts')],
                                            'Draw'])#1 Royal Flush vs Royal Flush
                                    ]


logging.basicConfig(level=logging.DEBUG) #uncomment to enable debugging



Royal_Flush_Hands = (['ace','king', 'queen','jack','10'],9000)
Straight_Flush_Hands = (['king', 'queen','jack','10', '9', '8', '7','6','5','4', '3', '2'],8000)

rank_templates = {'Royal_Flush': Royal_Flush_Hands, 'Straight_Flush': Straight_Flush_Hands, 'Four_Of_a_Kind': 2,
                'Full_House': 3, 'Flush': 4, 'Straight': 5,
                'Three_of_a_Kind': 6, 'Two_Pair': 7, 'One_pair': 8,
                'High_Card': 9}


def generate_RF_hand(rank_template:'list, should be of list of template hand',
                     suits:'list, and elements of type Card.get_card_suits',
                     nCards: 'int, specify number of cards in a hand, 3 - 5)'):
    #generate a Royal flush hand
    template , base_rank = rank_template
    cards = list(map(lambda val_suit: Card(*val_suit), zip(template, suits*nCards)))
    logging.debug("cards: ".format(cards))
    return cards, base_rank

def generate_SF_hand(rank_template:'list, should be of list of template hand',
                     high_card:'list, highest card content should be form Card.get_card_vals',
                     suits:'list, and content should be form Card.get_card_suits',
                     nCards: 'int, specify number of cards in a hand, 3 - 5'):
    #generate a Straight flush hand
    template , base_rank = rank_template
                     
    high_card_index = template.index(high_card)
    high_card_index = min(high_card_index, len(template)- nCards)
    high_card = template[high_card_index]
    
    cards = list(map(lambda val_suit: Card(*val_suit), zip(template[high_card_index: ], suits*nCards)))

    base_rank += Card.get_intr_val(high_card)
    logging.debug("cards: ".format(cards))
    return cards, base_rank

def generate_hand(rank_of_hand, suits,  high_card, nCards):
    """generate a hand based on the parameters provided, returns a hand and it is rank value"""
    if rank_of_hand not in rank_templates:
        logging.debug("Invalied rank".format(rank_of_hand))
        return None

    if nCards< 3 or nCards >5:
        logging.debug("Invalied nCards".format(nCards))
        return None

    if high_card and high_card not in Card.get_card_values():
        logging.debug("Invalied high_card".format(high_card))
        return None        

    #basically check if the suits we are having are standard ones
    for suit in set(suits):
        if suit not in Card.get_card_suits():
            logging.debug("Invalied suit".format(suit))
            return None
    
    if rank_of_hand == 'Royal_Flush':
        logging.debug("nCards:{} suit: {}".format(nCards, suits))
        player_hand, rank_value  = generate_RF_hand(rank_templates[rank_of_hand], suits, nCards)
        logging.debug("player_hand:{} rank_value: {}".format(player_hand, rank_value))
        return (player_hand, rank_value)

    elif rank_of_hand == 'Straight_Flush':
        logging.debug("nCards:{} suit: {} high_card: {}".format(nCards, suits, high_card))
        player_hand, rank_value  = generate_SF_hand(rank_templates[rank_of_hand], high_card, suits, nCards)
        logging.debug("player_hand:{} rank_value: {}".format(player_hand, rank_value))
        return (player_hand, rank_value)
    


if __name__ == '__main__':

    suits = Card.get_card_suits()
    print(suits)
    for nCards in range(3,6):
        for suit in suits:
            hand_rank = generate_hand('Royal_Flush', [suit],  None, nCards)
            print(hand_rank)
            
    print(suits)
    for nCards in range(3,6):
        for highcard in Straight_Flush_Hands[0]:
            hand_rank = generate_hand('Straight_Flush', [suits[0]],  highcard, nCards)
            print(hand_rank)
    
    # Sample test code
    deck1 = Deck(None)  # create a deck of cards
    # deck1.show() #show the entire deck of cards
    deck1.shuffle()  # shuffle the careds

    deck1.show(10)  # after shuffling show the first 10 cards

    # game = MyPoker()  # MyPoker intilises a game all the rules are embded in MyPoker

    player1_cards = deck1.deal(5)  # Deal 5 cards for Player 1
    player2_cards = deck1.deal(5)  # Deal 5 cards for Player 2
    # Deal 2 cards for Player 3, just for testing the function
    player3_cards = deck1.deal(2)

    print("Player 1: ", player1_cards)
    print("Player 2: ", player2_cards)
    print("Player 3: ", player3_cards)

    #print("validate_hand(player3_cards):", game.is_valid_hand(player3_cards))
    #print("validate_hand(player1_cards):", game.is_valid_hand(player1_cards))

    print(MyPoker.compare_hands(player3_cards, player2_cards))  # Return None
    print("Player1 ", MyPoker.compare_hands(
        player1_cards, player2_cards))  # Should Compare


