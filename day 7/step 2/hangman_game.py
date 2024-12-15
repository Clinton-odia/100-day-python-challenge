import random
word_list = ['clinton', 'camel', 'baboon']

chosen_word = random.choice(word_list)

print(chosen_word)
placeholder = ""
for letters in chosen_word:
  placeholder += "_"
print(placeholder)
guess = input("guess a letter: ").lower()
display = ""
for letter in chosen_word:
  if guess == letter:
    display += guess
  else:
    display += "_"
print(display)