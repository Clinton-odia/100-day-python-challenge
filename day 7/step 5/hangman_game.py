import random
from hangman_art import logo
from hangman_art import stage
from hangman_words import word_list
lives = 6
chosen_word = random.choice(word_list)
print(logo)
print("Welcome to Hangman Game!\n GUESS THE WORD")
print(chosen_word)
placeholder = ""
for letter in chosen_word:
  placeholder += "_"
print(placeholder)
correct_word = []
game_over = False
while not game_over:
  guess = input("Guess a letter: ").lower()
  if guess not in chosen_word:
    print(f"you guessed wrong!. you picked {guess}")
  display = ""
  for letter in chosen_word:
    if letter == guess:
      display += letter
      correct_word.append(guess)
    elif letter in correct_word:
      display += letter
    else:
      display += "_"
    
  if guess not in chosen_word:
    lives -= 1
    if lives == 0:
      game_over = True
      print("You lose.")
  print(display)
  if "_" not in display:
      game_over = True
      print("You win")
  
  print(f"{stage[lives]}")
  print(f"You have {lives} left")