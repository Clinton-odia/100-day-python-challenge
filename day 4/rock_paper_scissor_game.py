import random

#building the rock paper scissor game
# Rock
rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

# Paper
paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

# Scissors
scissor = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
user_choice = int(input("welcome to my rock,paper and scissors game!\nPick 1 for rock, 2 for paper and 3 for scissor: "))
computer_choice = random.randint(1,3)
# print(user_choice,computer_choice)
if user_choice == 1:
  if computer_choice == 2:
    print(rock)
    print(paper)
    print('Computer wins')
  elif computer_choice == 3:
    print(rock)
    print(scissor)
    print("You win")
  else:
    print(rock)
    print(rock)
    print("Draw")
elif user_choice == 2:
  if computer_choice == 3:
    print(paper)
    print(scissor)
    print('Computer wins')
  elif computer_choice == 1:
    print(paper)
    print(rock)
    print("You win")
  else:
    print(paper)
    print(paper)
    print("Draw")
elif user_choice == 3:
  if computer_choice == 2:
    print(scissor)
    print(paper)
    print('You win')
  elif computer_choice == 1:
    print(scissor)
    print(rock)
    print("Computer wins")
  else:
    print(scissor)
    print(scissor)
    print("Draw")
else:
  print("Sorry. Wrong input")