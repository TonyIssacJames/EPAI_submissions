""" Assignment for Session 06, First class functions Part -1
    Implementing the our own Poker Game"""

import random
import logging

# logging.basicConfig(level=logging.DEBUG) #uncomment to enable debugging

values = tuple(['2', '3', '4', '5', '6', '7', '8', '9',
                '10', 'jack', 'queen', 'king', 'ace'])
suits = tuple(['spades', 'clubs', 'hearts', 'diamonds'])


class Card:
    # a static dictionary to indicate what charecters to show for each card
    card_show_val = {'2': '2', '3': '3', '4': '4', '5': '5', '6': '6',
                     '7': '7', '8': '8', '9': '9', '10': '10',
                     'jack': 'J', 'queen': 'Q', 'king': 'K', 'ace': 'A',
                     'spades': 'S', 'clubs': 'C', 'hearts': 'H', 'diamonds': 'D'}

    # a static dictionary to calcualte intrinisc value of each card
    card_intr_val = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6,
                     '7': 7, '8': 8, '9': 9, '10': 10,
                     'jack': 11, 'queen': 12, 'king': 13, 'ace': 14,
                     # sutis have no significance here
                     'spades': 4, 'clubs': 1, 'hearts': 3, 'diamonds': 2
                     }

    # define the suit values and card values
    card_vals = tuple(['2', '3', '4', '5', '6', '7', '8',
                       '9', '10', 'jack', 'queen', 'king', 'ace'])
    card_suits = tuple(['spades', 'clubs', 'hearts', 'diamonds'])

    # a static method to check if a Person is adult or not.
    @staticmethod
    def get_card_values():
        return Card.card_vals

    @staticmethod
    def get_card_suits():
        return Card.card_suits

    def __init__(self, val, suit):
        self.val = val
        self.suit_val = suit

    def __repr__(self):
        return '{0}-{1}'.format(self.card_show_val[self.suit_val], self.card_show_val[self.val])

    def __str__(self):
        return '{0}-{1}'.format(self.card_show_val[self.suit_val], self.card_show_val[self.val])

    def __int__(self):
        "returns the value of the card as an integer"
        # return((self.card_intr_val[self.val] * 4) + self.card_intr_val[self.suit])
        return(self.card_intr_val[self.val])

    def __le__(self, other):
        return self.__int__() <= other.__int__()

    def __lt__(self, other):
        return self.__int__() < other.__int__()

    def __eq__(self, other):
        return self.__int__() == other.__int__() \
            and self.card_intr_val[self.suit_val] == self.card_intr_val[other.suit_val]

    def suit(self):
        return self.card_show_val[self.suit_val]


class Deck:
    def __init__(self, sel_function='normal'):
        self.vals = Card.get_card_values()
        self.suits = Card.get_card_suits()
        self.cards = []
        self.order = []
        self.top = 0  # points to top of the deck

        logging.debug("sel_function: {}".format(sel_function))
        # create the deck of cards normally
        if sel_function == 'normal':
            self.create_deck_normal()  # creates a deck card normally
        else:
            # creates a deck of card using single expression using zip, lambda and map
            self.create_deck_single_exp()

        # when the deck is created cards are in normal order
        self.order = list(range(52))

    def create_deck_normal(self):
        """Creates all the 52 cards in a deck without using lambda, zip, and map function to create 52 cards in a deck"""
        for suit in self.suits:
            for val in self.vals:
                self.cards.append(Card(val, suit))

    def create_deck_single_exp(self):
        """Creates the all the 52 cards in a deck using a single expression having lambda, zip, and map function"""
        self.cards = list(map(lambda val_suit: Card(
            *val_suit), zip(self.vals*len(self.suits), self.suits*len(self.vals))))

    def show(self, count=52):
        """show count number of cards from the deck"""
        count = min(count, 52)  # limit count to 52

        if count > 0:
            for card in self.cards[:count]:
                print(card)

    def shuffle(self):
        """shuffle the cards in the deck"""
        random.shuffle(self.cards)

    def deal(self, count=3):
        """deal count number of cards"""
        start = self.top
        end = min(self.top + count, 52)

        if start + count == end:
            self.top = end
            return self.cards[start:end]


class MyPoker:
    """MyPoker is class is created to put together all game functionalites
       and rules

       MyPoker.compare_hands() can be used to decidide the result of two  hands as per poker rule

       for rules refer:
       1 - https://www.blackrain79.com/2018/05/poker-cheat-sheet.html
       2 - https://i.pinimg.com/474x/6b/1f/f7/6b1ff73716c14139c951241f3c1d7c46.jpg"""

    rank_names = ('Royal_Flush', 'Straight_Flush', 'Four_Of_a_Kind',
                  'Full_House', 'Flush', 'Straight',
                  'Three_of_a_Kind', 'Two_Pair',  'One_pair',
                  'High_Card',)

    rank_of_hand = {'Royal_Flush': 0, 'Straight_Flush': 1, 'Four_Of_a_Kind': 2,
                    'Full_House': 3, 'Flush': 4, 'Straight': 5,
                    'Three_of_a_Kind': 6, 'Two_Pair': 7, 'One_pair': 8,
                    'High_Card': 9}

    def __init__(self):
        pass

    @staticmethod
    def is_valid_hand(p_hands, min_cards=3, max_cards=5):
        """validate the current set cards
           this function has to be called first so furhter operation are guranteed to be of success"""
        if p_hands and ((len(p_hands) >= min_cards) and (len(p_hands) <= max_cards)):
            return True

    @staticmethod
    def pair_exists(p_values: 'list of card values as integers'):
        """ check if any pair or more exists in the hand"""
        if len(p_values) != len(set(p_values)):
            return True
        else:
            return False

    @staticmethod
    def is_flush(p_suits: 'list of suit values as strings'):
        """ calcualte if the cards are all of same suit(flush) or not"""
        if len(set(p_suits)) == 1:
            return True
        else:
            return False

    @staticmethod
    def is_running_seq(p_values: 'list of card values as integers') -> 'True or False':
        """ calcualte if the cards are in a continous sequence or not"""
        diff = p_values[0] - p_values[-1]
        if diff == len(p_values) - 1:
            return True
        else:
            return False

    @staticmethod
    def calculate_hist(p_values: 'list of card values as integers'):
        """ calcualte the histogram of input cards, the result will be used to find pairs"""
        hist = {}
        for val in p_values:
            if val in hist:
                hist[val] += 1
            else:
                hist[val] = 1

        return hist

    @staticmethod
    def calc_rank_on_values(p_values: 'list of card values as integers'):
        """calculate the rank of hand based on just the values"""

        hist = MyPoker.calculate_hist(p_values)
        no_cards = len(p_values)

        # max_rep , to detect 4 of kind or 3 of a kind
        max_reps = max(hist.values())
        no_of_reps = len(
            list(filter(lambda x: x > 1, hist.values())))  # no_of_reps

        logging.debug("hist= {}, no_cards= {}, max_reps={}, no_of_reps={}".format(
            hist, no_cards, max_reps, no_of_reps))

        if no_cards >= 3:
            # make rules for the case when cards are 3, 4, 5
            # we don't change the rules, these ranks may not be based on the right probability
            if max_reps == 4:
                return 'Four_Of_a_Kind'
            elif max_reps == 3:
                if no_of_reps == 2:
                    return 'Full_House'
                else:
                    return 'Three_of_a_Kind'
            elif max_reps == 2:
                if no_of_reps == 2:
                    return 'Two_Pair'
                else:
                    return 'One_pair'
        else:
            return None

    @staticmethod
    def calc_rank(p_cards: 'list of objects of type Card'):
        """ anlayze the hand and rank it
            this function retuns a tuple
            the rank of the hand
            rank - what rank for the card """

        p_values = list(map(int, sorted(p_cards, key=int, reverse=True)))
        p_suits = list(map(lambda card: card.suit(),
                           sorted(p_cards, key=int, reverse=True)))

        logging.debug("p_values: {}".format(p_values))
        logging.debug("p_suits: {}".format(p_suits))

        if MyPoker.pair_exists(p_values):
            # Four of Kind, Full house, Three of a kind, Two pair, One pair
            # Suits has no role any more we only need to check the values
            return MyPoker.calc_rank_on_values(p_values)
        else:
            # Royal Flush, Straight Flush, Flush, Straigt, High Card"
            if MyPoker.is_flush(p_suits):
                # Royal Flush, Straight Flush, Flush
                if MyPoker.is_running_seq(p_values):
                    if p_values[0] == 13:
                        return 'Royal_Flush'  # 'Royal Flush'
                    else:
                        return 'Straight_Flush'  # 'Straight Flush'
                else:
                    return 'Flush'  # 'Flush'
                pass
            else:
                # Straigt, High Card
                if MyPoker.is_running_seq(p_values):
                    return 'Straight'  # 'Straight'
                else:
                    return 'High_Card'  # 'High_Card'

    @staticmethod
    def compare_hands(p1_cards: 'list of Objects of type Card',
                      p2_cards: 'list of Objects of type Card'
                      ) -> 'result can be \'Wins\',\'Lose\', \'Draw\' or None':
        """ Given two decks of cards decide the winning  hand
            if p1 wins retuns Wins
            if p1 loses returs Lose
            if it is a draw returns Draw
            if there is an issue and the result cannot be calcualted then it retun None"""
        # check if both hands are valid
        if not MyPoker.is_valid_hand(p1_cards) or not MyPoker.is_valid_hand(p2_cards):
            return

        # check if lenghs are matching
        if len(p1_cards) != len(p2_cards):
            return

        # sort the hands and get the intrinisc value of the cards
        p1_values = list(map(int, sorted(p1_cards, key=int, reverse=True)))
        p2_values = list(map(int, sorted(p2_cards, key=int, reverse=True)))

        # we need to sort by repetion first, and value next for comparison
        p1_hist = MyPoker.calculate_hist(p1_values)
        p2_hist = MyPoker.calculate_hist(p2_values)

        logging.debug(
            "Before Sort with histogram, p1_values: {}".format(p1_values))
        logging.debug(
            "Before Sort with histogram, p2_values: {}".format(p2_values))

        p1_values = sorted(
            p1_values, key=lambda val: p1_hist[val], reverse=True)
        p2_values = sorted(
            p2_values, key=lambda val: p2_hist[val], reverse=True)

        logging.debug(
            "After Sort with histogram, p1_values: {}".format(p1_values))
        logging.debug(
            "After Sort with histogram, p2_values: {}".format(p2_values))

        p1_rank_name = MyPoker.calc_rank(p1_cards)
        p2_rank_name = MyPoker.calc_rank(p2_cards)

        p1_rank = MyPoker.rank_of_hand[p1_rank_name]
        p2_rank = MyPoker.rank_of_hand[p2_rank_name]

        logging.debug("p1_rank: {}".format(p1_rank_name))
        logging.debug("p2_rank: {}".format(p2_rank_name))

        if p1_rank < p2_rank:
            return "Wins"  # P1 wins
        elif p1_rank > p2_rank:
            return "Lose"  # P2 wins
        else:
            # rank is same now let's check the card vlaues
            for p1_value, p2_value in zip(p1_values, p2_values):
                if p1_value > p2_value:
                    return "Wins"  # P1 wins
                elif p1_value < p2_value:
                    return "Lose"  # P2 wins

            return "Draw"  # the game is draw


if __name__ == '__main__':
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
