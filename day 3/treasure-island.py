print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[clinton]
*******************************************************************************
''')
print("Welcome to Treasure Land. \nYour mission is to find the treasure\nYou're at a cross road. Where do you want to go?")
crossroad = input('   Type "left" or "right"🕖 ').lower()
if crossroad == 'left':
  print("You ended up in a riverbank. Do you want to wait for the boat or swim?🎃")
  swim = input('     Type "swim" or "wait" 🏊‍♂️: ').lower()
  if swim == 'wait':
    print("the boat come and carried you to a cattle in the island.\n wandering around the cattle. you've discovered three doors")
    door= input('   Type "red", "yellow" or "blue": ').lower()
    if door == "red":
      print("Burned by fire.Game Over🔥👻")
    elif door == "yellow":
      print("You Win!🏆")
    elif door == 'blue':
      print("Eaten by beast.Game Over👿👻")
    else:
      print("wrong input")
      
  elif swim == 'swim':
    print("You got attacked by crocodiles.Game Over🐊👻")
  else:
    print("wrong input")
elif crossroad == 'right':
  print("You fall into a hole. Game Over👻")
else:
  print("wrong input")