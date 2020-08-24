""" Assignment for Session 06, First class functions Part -1
    Implementing the our own Poker Game"""

import random

class Card:
    #a static dictionary to indicate what charecters to show for each card
    card_show_val = {'2':'2', '3':'3', '4':'4', '5':'5', '6':'6',\
                     '7':'7', '8':'8', '9':'9', '10':'10',\
                     'jack':'J', 'queen':'Q', 'king':'K', 'ace':'A',\
                     'spades':'S', 'clubs':'C', 'hearts':'H', 'diamonds':'D'}
    
    #a static dictionary to calcualte intrinisc value of each card
    card_intr_val = {'2':2, '3':3, '4':4, '5':5, '6':6,\
                     '7':7, '8':8, '9':9, '10':10,\
                     'jack':10, 'queen':11, 'king':12, 'ace':13,\
                     'spades':4, 'clubs':1, 'hearts':3, 'diamonds':2 #sutis have no significance here
                     }
    def __init__(self, val, suit):
        self.val = val
        self.suit = suit

    def __repr__(self):
        return '{0}-{1}'.format(self.card_show_val[self.suit], self.card_show_val[self.val])

    def __str__(self):
        return '{0}-{1}'.format(self.card_show_val[self.suit], self.card_show_val[self.val])

    def __int__(self):
        "returns the value of the card as an integer"
        #return((self.card_intr_val[self.val] * 4) + self.card_intr_val[self.suit])
        return(self.card_intr_val[self.val])

    def __le__(self, other):
        return self.__int__() <= other.__int__()
        
    def __lt__(self, other):
        return self.__int__() < other.__int__()
    
    def __eq__(self, other):
        return self.__int__() == other.__int__()


class Deck:
    def __init__(self):
        self.vals = tuple(['2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king', 'ace'])
        self.suits= tuple(['spades', 'clubs', 'hearts', 'diamonds'])
        self.cards=[] 
        self.order=[]
        self.top=0 #points to top of the deck

        #create the deck of cards normally
        self.create_deck_normal()

        #when the deck is created cards are in normal order
        self.order = list(range(52))

    def create_deck_normal(self):
        """Creates the cards without using lambda, zip, and map function to create 52 cards in a deck"""
        for suit in self.suits:
            for val in self.vals:
                self.cards.append(Card(val,suit))

    def show(self, count = 52):
        """show count number of cards from the deck"""
        count = min(count, 52) #limit between to 52

        if count > 0:
            for card in self.cards[:count]:
                print(card)

    def shuffle(self):
        """shuffle the cards in the deck"""
        random.shuffle(self.cards)

    def deal(self, count = 3):
        """deal count number of cards"""
        start = self.top
        end   = min(self.top + count , 52)

        if start + count == end:
            self.top = end
            return self.cards[start:end]

class MyPoker:
    """MyPoker is class is created to put together all game functionalites
       and rules

       for rules refer:
       1 - https://www.blackrain79.com/2018/05/poker-cheat-sheet.html
       2 - https://i.pinimg.com/474x/6b/1f/f7/6b1ff73716c14139c951241f3c1d7c46.jpg"""

    rank_of_hand = {'Royal_Flush': 1, 'Straight_Flush': 2, 'Four_Of_a_Kind': 3, \
                    'Full_House': 4, 'Flush': 5, 'Straight': 6, \
                    'Three_of_a_Kind': 7, 'Two_Pair': 8, 'One_pair': 9, \
                    'High_Card': 10}

    def __init__(self):
        pass

    def is_valid_hand(self, p_hands, min_cards = 3, max_cards = 5):
        """validate the current set cards
           this function has to be called first so furhter operation are guranteed to be of success"""
        if p_hands and ((len(p_hands) >= min_cards) and (len(p_hands) <= max_cards)):
            return True


    def pair_exists(self, p_hands):
        """ check if any pair or more exists in the hand"""
        
        if len(p_hands) != len(set(p_hands)):
            return True
        else:
            return False

    def calc_rank(self, p_hand):
        """ anlayze the hand and rank it
            this function retuns a tuple
            the rank of the hand
            rank - what rank for the card """
        if pair_exists(p1_hand):
            #Four of Kind, Full house, Three of a kind, Two pair, One pair
        else:
            #Royal Flush, Straight Flush, Flush, Straigt, High Card"
        
    def compare_hands(self, p1_cards, p2_cards):
        """ Given two decks of cards decide the winning  hand
            if p1 wins retuns Wins
            if p1 loses returs Lose
            if it is a draw returns Draw
            if cannot be determined retun None"""
        #check if both hands are valid
        if not self.is_valid_hand(p1_cards) or not self.is_valid_hand(p2_cards):
            return

        #check if lenghs are matching
        if len(p1_cards)!= len(p2_cards):
            return

        #sort the hands and get the intrinisc value of the cards
        p1_cards = map(sorted(p1_cards,key=int, reverse=True), int)
        p2_cards = map(sorted(p2_cards,key=int, reverse=True), int)

        p1_rank = calc_rank(p1_cards)
        p2_rank = calc_rank(p2_cards)
        
        if p1_rank < p2_rank:
            return "Wins" # P1 wins
        elif: p1_rank > p2_rank:
            return "Lose" # P2 wins
        else: #rank is same not let' check the card vlaues
            for card1, card2 in zip(p1_cards, p2_cards):
                if card1 > card2:
                    return "Wins" # P1 wins
                elif card1 < card2:
                    return "Lose" # P2 wins

            return "Draw" # the game is draw
    
#=========================
#start execuring the code
deck1 = Deck()
deck1.show()
deck1.shuffle()
print("==============================")
deck1.show(10)

game = MyPoker()

player1_cards = deck1.deal(5)
player2_cards = deck1.deal(5)
player3_cards = deck1.deal(2)

print("Player 1: ", player1_cards)
print("Player 2: ", player2_cards)
print("Player 1: ", sorted(player1_cards,key=int, reverse=True))
print("Player 2: ", sorted(player2_cards,key=int, reverse=True))


print(player1_cards)

print(player1_cards[0] >= player2_cards[0])
print(player1_cards[0] > player2_cards[0])
print(player1_cards[0] !=  player2_cards[0])

print("validate_hand(player3_cards):", game.is_valid_hand(player3_cards))
print("validate_hand(player1_cards):", game.is_valid_hand(player1_cards))
print(game.compare_hands(player3_cards, player2_cards))
