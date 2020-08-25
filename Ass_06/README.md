# EPAI_Assignment_06 Poker Game

## Objectives

|   | Objectives  |  Status |
|---|---|---|
|1   | Write a single expression that includes lambda, zip and map functions to select create 52 cards in a deck  | done  |
|2   | Write a normal function without using lambda, zip, and map function to create 52 cards in a deck   |  done |
|3   | Write a function that, when given 2 sets of 3 or 4 or 5 cards using game of poker | done   |
|4   | Write a Proper readme file | done  |
|5   | Docstrings must, and it must mention what the function is doing (2, 3)  |  done |
|6   | Write annotations for 3 | done   |
|7   | check correcteness of functions in 1/2 with a manual list of 52 cards | done   |
|7   | Basics tests to ensure your code if correct (20+ combination tests (counted as 1 test) for function in 3 | partially done   |

## Compare two hands of cards using "our" Poker Game rules

1. cards can vary form 3 to 5
    - in five card case standard poker game rule apply (which are given below)
    - when it is 3 or 4 cards we can define the rules
    - we applied the same rules of 5 cards to 3 and 4 cards hands whenever possible
      - but there are some special cases, for example in 3 cards case
          - a **Royal Flush** means A K Q of the same suit
          - there won't be any **Full House**
          - there won't be any **Four Of a Kind**, **Two Pair**
          - etc.
       - in 4 cards case
          - a **Royal Flush** means A K Q J of the same suit
          - there won't be any **Full House**
     - in 3 or 4 card case applying the same rules of 5 cards won't make sense from statistical point of view.       
        - generally higher the rank of a card means that, the probability of getting it is less
        - but this is just an Assignmet
        - My Game, My Rules 
        
2. 2 players only
3. 1 deck of cards only


### 1 - The Standard Poker Game Rules for hands of 5 card are given below

![Five Card Poker Rules](https://i.pinimg.com/474x/6b/1f/f7/6b1ff73716c14139c951241f3c1d7c46.jpg)

The lower number rank wins.
For detailed rules ![click here](https://www.blackrain79.com/2018/05/poker-cheat-sheet.html)

## 2 - Write a single expression that includes lambda, zip and map functions to select create 52 cards in a deck
```python
    def create_deck_single_exp(self):
        """Creates the all the 52 cards in a deck using a single expression having lambda, zip, and map function"""
        self.cards = list(map(lambda val_suit: Card(*val_suit), zip(self.vals*len(self.suits), self.suits*len(self.vals))))
```
## 3 - Write a normal function without using lambda, zip, and map function to create 52 cards in a deck 

```python
    def create_deck_normal(self):
        """Creates the cards without using lambda, zip, and map function to create 52 cards in a deck"""
        for suit in self.suits:
            for val in self.vals:
                self.cards.append(Card(val,suit))
```
## 4 - Test cases
