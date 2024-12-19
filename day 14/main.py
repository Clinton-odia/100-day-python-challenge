import random
from art import logo
from art import vs
import game_data

def pick(choice):
  """return the value of user's choice"""
  if choice == 'a':
    return first_compare_followers
  if choice == 'b':
    return second_compare_followers
first_compare = random.choice(game_data.data)
current_score = 0
game_over = False
while not game_over:
  print(logo)
  print(f"Compare A: {first_compare['name']}, a {first_compare['description']}, from {first_compare['country']} ")
  print(vs)
  second_compare = random.choice(game_data.data)
  print(f"Against B: {second_compare['name']}, a {second_compare['description']}, from {second_compare['country']} ")
  first_compare_followers = first_compare['follower_count']
  second_compare_followers = second_compare['follower_count']

  choice = input("Who has more followers? Type 'A' or 'B': ").lower()
  user_choice = pick(choice)
  if user_choice > first_compare_followers or user_choice > second_compare_followers:
    current_score += 1
    first_compare = second_compare
    print(f"You're right! Current score:{current_score}")
  else:
    print(f"sorry, that's wrong. the final score:{current_score}")
    game_over = True