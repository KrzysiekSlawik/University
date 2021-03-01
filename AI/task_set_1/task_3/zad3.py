import random
import re
from enum import Enum

# diamonds = 'D'
# hearths = 'H'
# spades = 'S'
# clubs = 'C'
# two = '1'
# three = '2'
# four = '3'
# five = '4'
# six = '5'
# seven = '6'
# eight = '7'
# nine = '8'
# ten = '9'
# jack = 'J'
# queen = 'Q'
# king = 'K' 
# ace = 'A'

class Card():
    def __init__(self, figure:str, color:str):
        self.figure:str = figure
        self.color:str = color
    
class Hand():
    def __init__(self, cards:list[Card]):
        self.cards = cards

    def figures(self) -> str:
        lst = [card.figure for card in self.cards]
        lst.sort()
        return ''.join(lst)

    def color(self) -> str:
        lst = [card.color for card in self.cards]
        lst.sort()
        return ''.join(lst)


def is_pair(hand:Hand) -> bool:
    figures = hand.figures()
    return re.search('(.)\1',figures) != None

def is_two_pairs(hand:Hand) -> bool:
    figures = hand.figures()
    return re.search('(.)\1(.)\1',figures) != None

def is_three(hand:Hand) -> bool:
    figures = hand.figures()
    return re.search('(.)\1\1',figures) != None

def is_full(hand:Hand) -> bool:
    figures = hand.figures()
    return re.search('(.)\1\1(.)\2|(.)\3(.)\4\4',figures) != None

def is_four(hand:Hand) -> bool:
    figures = hand.figures()
    return re.search('(.)\1\1\1',figures) != None

def is_color(hand:Hand) -> bool:
    colors = hand.color()
    return re.search('(.)\1\1\1\1',colors) != None

def is_straight(hand:Hand) -> bool:
    figures = list(map(int,hand.figures()))
    for i in range(1,4):
        if figures[i] != figures[0] + i:
            return False
    return True
def is_poker(hand:Hand) -> bool:
    return is_color(hand) and is_straight(hand)

def eval_blotkarz(hand:Hand) -> int:
    if is_poker(hand):
        return 8
    if is_four(hand):
        return 7
    if is_full(hand):
        return 6
    if is_color(hand):
        return 5
    if is_straight(hand):
        return 4
    if is_three(hand):
        return 3
    if is_two_pairs(hand):
        return 2
    if is_pair(hand):
        return 1
    return 0

def eval_figurant(hand:Hand) -> int:
    if is_four(hand):
        return 7
    if is_full(hand):
        return 6
    if is_color(hand):
        return 5
    if is_three(hand):
        return 3
    if is_two_pairs(hand):
        return 2
    if is_pair(hand):
        return 1
    return 0

def is_blotkarz_winner(blotkarz:Hand, figurant:Hand) -> bool:
    return eval_blotkarz(blotkarz) > eval_figurant(figurant)

def simulate_game(blotkarz_deck:list[Card], figurant_deck:list[Card], games:int) -> int:
    blotkarz_won:int = 0
    for i in range(0,games):
        if(is_blotkarz_winner(
            Hand(random.sample(blotkarz_deck, 5)),
            Hand(random.sample(figuarant_deck, 5)))):
            blotkarz_won += 1
    return blotkarz_won



figuarant_deck = [
    Card('J','D'),
    Card('J','H'),
    Card('J','S'),
    Card('J','C'),
    Card('Q','D'),
    Card('Q','H'),
    Card('Q','S'),
    Card('Q','C'),
    Card('K','D'),
    Card('K','H'),
    Card('K','S'),
    Card('K','C'),
    Card('A','D'),
    Card('A','H'),
    Card('A','S'),
    Card('A','C')
]

blotkarz_deck = [
    Card('1','D'),
    Card('1','H'),
    Card('1','S'),
    Card('1','C'),
    Card('2','D'),
    Card('2','H'),
    Card('2','S'),
    Card('2','C'),
    Card('3','D'),
    Card('3','H'),
    Card('3','S'),
    Card('3','C'),
    Card('4','D'),
    Card('4','H'),
    Card('4','S'),
    Card('4','C'),
    Card('5','D'),
    Card('5','H'),
    Card('5','S'),
    Card('5','C'),
    Card('6','D'),
    Card('6','H'),
    Card('6','S'),
    Card('6','C'),
    Card('7','D'),
    Card('7','H'),
    Card('7','S'),
    Card('7','C'),
    Card('8','D'),
    Card('8','H'),
    Card('8','S'),
    Card('8','C'),
    Card('9','D'),
    Card('9','H'),
    Card('9','S'),
    Card('9','C')
]

blotkarz_eq_figurant_deck = [
    Card('6','D'),
    Card('6','H'),
    Card('6','S'),
    Card('6','C'),
    Card('7','D'),
    Card('7','H'),
    Card('7','S'),
    Card('7','C'),
    Card('8','D'),
    Card('8','H'),
    Card('8','S'),
    Card('8','C'),
    Card('9','D'),
    Card('9','H'),
    Card('9','S'),
    Card('9','C')
]

good_blotkarz_deck = [
    Card('1','C'),
    Card('2','C'),
    Card('3','C'),
    Card('4','C'),
    Card('5','C'),
    Card('6','C'),
    Card('7','C'),
    Card('8','C'),
    Card('9','C')
]
#hand or deck?
super_blotkarz_deck = [
    Card('5','C'),
    Card('6','C'),
    Card('7','C'),
    Card('8','C'),
    Card('9','C')
]

print(simulate_game(blotkarz_deck, figuarant_deck, 100))
print(simulate_game(good_blotkarz_deck, figuarant_deck, 100))
print(simulate_game(blotkarz_eq_figurant_deck, figuarant_deck, 100))
print(simulate_game(super_blotkarz_deck, figuarant_deck, 100))
