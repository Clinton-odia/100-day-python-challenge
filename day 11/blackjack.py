import sys
import random
card = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


game_start = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
if game_start == 'y':
  my_card = random.sample(card, 2)
  computer_card = random.sample(card, 2)
  my_score = sum(my_card)
  computer_score = sum(my_card)
  print(f"Your Card: {my_card}, Current Score: {my_score}")
  print(f"Computer's first hand: {computer_score}")
  def game_play(my_score, computer_score):
    another_game = input("Type 'y' to get another card, type 'n' to pass: ").lower()
    if another_game == 'y':
      new_card = random.choice(card)
      my_card.append(new_card)
      my_score += new_card
      new_com_card = random.choice(card)
      computer_card.append(new_com_card)
      computer_score = sum(computer_card)

      print(f"Your card: {my_card}, Current Score: {my_score}")
      print(f"Computer's first hand:{computer_card} {computer_score}")

  game_play(my_score, computer_score)
else:
 sys.exit()