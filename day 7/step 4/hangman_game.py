import random
word_list = ['clinton', 'camel', 'baboon']
lives = 6
chosen_word = random.choice(word_list)

print(chosen_word)
placeholder = ""
for letters in chosen_word:
  placeholder += "_"
print(placeholder)
correct_letters = []
game_over = False
while not game_over:
  guess = input("guess a letter: ").lower()

  display = ""
  for letter in chosen_word:
    if guess == letter:
      display += guess
      correct_letters.append(guess)
    elif letter in correct_letters:
      display += letter
    else:
      display += "_"
  print(display)
  if guess not in chosen_word:
    lives -= 1
    if lives == 0:
      game_over = True
      print('You lose.')
  if "_" not in display:
    game_over = True
    print("You win")