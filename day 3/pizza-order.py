print("Welcome to Pizza Hut!")
size = input("What size pizza do you want? S, M or L? ").lower()
pepperoni = input('Do you want pepperoni on your pizza? Y or N: ').lower()
extra_cheese = input("Do you want extra cheese? Y or N:")

#Small pizza= $15, Medium pizza= $20 and Large pizza= $25
#conditional statement based on their size choice
bill = None
if size == 's':
  bill = 15
  if pepperoni == 'y':
    bill += 2
elif size == 'm':
  bill = 20
  if pepperoni == 'y':
    bill += 3
elif size == 'l':
  bill = 25 
  if pepperoni == 'y':
    bill += 3
else:
  print('you typed the wrong input')
if extra_cheese == 'y':
  bill += 1
print(f"your total bill is ${bill}")
  