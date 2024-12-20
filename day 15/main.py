import math
from art import logo
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk" : 100,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

COIN_VALUES = {
    "quarter": 0.25,
    "dime": 0.1,
    "nickel": 0.05,
    "penny": 0.01,
}
COFFEE_REPORT = {
  "water" : 500,
  "milk" : 300,
  "coffee": 200,
}
profit = 0
def processed_coin():
  print("Please insert coins.")
  quarter = COIN_VALUES["quarter"] * int(input("How many quarter: "))
  dime = COIN_VALUES["dime"] * int(input("how many dime: "))
  nickel = COIN_VALUES["nickel"] * int(input("How many nickel: "))
  penny = COIN_VALUES["penny"] * int(input("How many penny: "))
  return quarter + dime + nickel + penny


def is_resouce_sufficient(order_ingredients):
  for item in order_ingredients:
    if COFFEE_REPORT[item] < order_ingredients[item]:
      print(f"Sorry, there is not enough {item}")
      return False
  return True

def is_transaction_successful(money_received, drink_cost):
  if money_received >= drink_cost:
    change = round(money_received - drink_cost, 2)
    print(f"Here is ${change} in change")
    global profit
    profit +=drink_cost
    return True
  else:
    print("“Sorry that's not enough money. Money refunded.")
    return False
def make_coffee(drink_name, order_ingredients):
  for item in order_ingredients:
    COFFEE_REPORT[item] -= order_ingredients[item]
    
  print(f"Here goes your {drink_name}☕")
coffee_machine = True
print(logo)
while coffee_machine:
  user_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
  if user_choice == "off":
    coffee_machine = False
  elif user_choice == "report":
    print(f"Water: {COFFEE_REPORT['water']}ml\nMilk: {COFFEE_REPORT['milk']}ml\nCoffee: {COFFEE_REPORT['coffee']}gl\nMoney: ${profit}")
  else:
    drink = MENU[user_choice]
    if is_resouce_sufficient(drink["ingredients"]):
      payment = processed_coin()
      if is_transaction_successful(payment, drink['cost']):
        make_coffee(user_choice,drink["ingredients"])
