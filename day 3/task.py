#control flow with if/else and conditional operators
#modulo operator
#a program to check if a number is even or odd
# number = int(input("what's your number? "))
# if number % 2 == 0:
#   print("even")
# else:
#   print("odd")

#rollercoster ticketmaster
print("Welwcomw to the rollercoster!")
height = int(input("what is your height in cm? "))
if height > 120:
  print("you can ride the rollercoster")
  age = int(input("what is your age? "))
  if age <= 12:
    bill = 5
    print("Child tickets are $5")
  elif age <= 18:
    bill = 7
    print("Youth tickets are $7")
  else:
    bill = 12
    print("Adult tickets are $12")
  wants_photo = input('Do you want to have a photo take? Type Y for Yes and N for No: ').lower()
  if wants_photo == 'y':
    #add $3 to total bill
    bill += 3
  print(f"your total bill is ${bill}")
else:
  print("Sorry, you have to grow taller before you can ride")