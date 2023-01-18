import random
import os
from art import logo

def deal_card():
    """Picks a single number from the card list and returns it"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card
