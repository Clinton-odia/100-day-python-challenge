from art import logo
def add(n1, n2):
  return n1 + n2

def substract(n1, n2):
  return n1 - n2

def divide(n1,n2):
  return n1 / n2

def multiply(n1,n2):
  return n1 * n2

operation = {
  "+": add,
  "-": substract,
  "*": multiply,
  "/": divide,
}

def calculations(first_num,calc,second_num):
  for sign in operation:
    if sign == calc:
      return operation[sign](first_num,second_num)
def calculator():
  print(logo)
  first_number = int(input("What's your first number? "))
  should_accumulate = True
  while should_accumulate:

    calculation = input("+\n-\n*\n/\nPick an operation: ")
    second_number = int(input("What's your next number? "))
    answer = calculations(first_num=first_number, calc=calculation, second_num=second_number)
    print(f"{first_number}{calculation}{second_number} = {answer}")

    choice = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start new calculation: ").lower()
    if choice == 'y':
      first_number = answer
    else:
      should_accumulate = False
      print("\n" * 20)
      calculator()

calculator()
