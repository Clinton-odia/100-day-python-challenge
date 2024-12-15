import random
word_list = ['clinton', 'camel', 'baboon']

#Todo 1 - Randomly choose a word from the word_list and assign it a variable called chosen_word then print it
chosen_word = random.choice(word_list)
print(chosen_word)

# todo 2 - Ask the user to guess a letter and assign their answer to a variable called guess. make guess lowercase
guess = input("guess a letter: ").lower()
#todo 3 - Check if the letter the guessed(guess) is one of the letters in the chosen_word. print "Right" if it is
#is "wrong" if it's not.
for letter in chosen_word:
  if guess == letter:
    print("right")
  else:
    print("Wrong")