import random
import game_data

def pick(choice):
  if choice == 'a':
    return first_compare_followers
  if choice == 'b':
    return second_compare_followers
current_score = 0
game_over = False
while not game_over:
  first_compare = random.choice(game_data.data)
  print(first_compare)

  second_compare = random.choice(game_data.data)
  print(second_compare)
  first_compare_followers = first_compare['follower_count']
  second_compare_followers = second_compare['follower_count']
  print(first_compare_followers)
  print(second_compare_followers)

  choice = input("Who has more followers? Type 'A' or 'B': ").lower()
  print(choice)
  user_choice = pick(choice)
  if user_choice > first_compare_followers or user_choice > second_compare_followers:
    current_score += 1
    print("You are correct",current_score)
  else:
    print("you are wrong",current_score)
    game_over = True