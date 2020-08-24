# EPAI_Assignment_06 Poker Game

## Objective
#### Compare two hands of cards using Standard Poker Game rules

1. cards can vary form 3 to 5
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


## 1 - The Standard Poker Game Rules for hands of 5 card are given below

![Five Card Poker Rules](https://i.pinimg.com/474x/6b/1f/f7/6b1ff73716c14139c951241f3c1d7c46.jpg)

## 2
## 3 - Write a normal function without using lambda, zip, and map function to create 52 cards in a deck 

```python
    def create_deck_normal(self):
        """Creates the cards without using lambda, zip, and map function to create 52 cards in a deck"""
        for suit in self.suits:
            for val in self.vals:
                self.cards.append(Card(val,suit))
```
