lover1 = input("what is your name? ")
lover2 = input("what is your lover's name? ")
def calculate_love_score(name1,name2):
  combined_word = name1.lower() + name2.lower()
  true_score= 0
  love_score= 0
  for letter in "true":
      true_score +=combined_word.count(letter)
  for letter in "love":
    love_score += combined_word.count(letter)
 
  print(f"Love Score = {true_score}{love_score}")

calculate_love_score(name1=lover1,name2=lover2)