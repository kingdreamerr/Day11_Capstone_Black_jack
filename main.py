import random
import os
from art import logo

def deal_card():
    """Picks a single number from the card list and returns it"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate(cards):
  """Inputs a list and returns a sum of the list"""
  if sum(cards) == 21 and len(cards) == 2:
    return 0

  if 11 in cards and sum(cards) > 21:
    cards.remove(11)
    cards.append(1)
  
  return sum(cards)

def compare_scores(user,computer):
  if user == computer:
    return "Draw"
  elif computer == 0:
    return "Lose, opponent has a Blackjack"
  elif user == 0:
    return "Win with Blackjack"
  elif user > 21:
    return "You went over. You lose"
  elif computer > 21:
    return "Opponent went over. You win"
  elif user > computer:
    return "You win!"
  else:
    return "You lose!"

def black_jack():
  print(logo)
  computer_cards = []
  user_cards = []
  is_game_over = False

  for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())