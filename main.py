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

  while not is_game_over:
      
    user_score = calculate(user_cards)
    computer_score = calculate(computer_cards)

    print(f"your cards: {user_cards}, current score: {user_score}")
    print(f"computer first card: {computer_cards[0]}")

    if user_score == 0 or computer_score == 0 or user_score > 21:
      is_game_over = True
    else:
      go_on = input("Gett more cards? 'y' for yes and 'n' for no: ")
      if go_on == 'y':
        user_cards.append(deal_card())
        user_score = calculate(user_cards)
        print(f"your cards: {user_cards}, current score: {user_score}")
      else:
        is_game_over = True

  while computer_score !=0 and computer_score < 17:
    computer_cards.append(deal_card())
    computer_score = calculate(computer_cards)

  print(compare_scores(user_score,computer_score))

while input("Do you want to play a game of Blackjack? type 'y' to play and 'n' for no: ") == 'y':
  os.system("clear")
  black_jack()