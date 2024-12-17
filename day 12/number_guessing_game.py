import random
from art import logo
number = []
for x in range(1,101):
  number.append(x)

guess = random.choice(number)

print(logo)
print("Welcome to Number Guessing Game\nI'm think about a number between 1- 100")
difficult_choice = input("Choose your difficulty: Type 'easy' or 'hard': ").lower()
# def compare(computer_guess,user_guess):
if difficult_choice == 'easy':
  attempts = 10
elif difficult_choice == 'hard':
  attempts = 5
else:
  attempts = 10
game_over = False
while attempts > 0 and not game_over:
  user_guess = int(input("Make a guess: "))
  if guess == user_guess:
      print(f"you got it! the answer is {guess} ")
      game_over = True
  elif user_guess > guess:
      print("Too high")
      print("guess again")
  else:
      print("Too low")
      print("guess again")

  attempts -= 1
  if attempts > 0 and not game_over:
     print(f"You have {attempts} attempts remaining.")
  elif attempt == 0 and not game_over: 
     print(f"You have {attempts} attempts remaining. Game over")

  

