from art import logo
print(logo)
auction = {}
game_auction = False
while not game_auction:
  print("Welcome to the silent Auction!")
  name = input("what's your name? ").lower()
  bid = int(input("What's your bid? $ "))
  auction[name] = bid

  more_bid = input("Are there more bidders? Type 'Yes' for more bids or Type 'No' to end bid: ").lower()
  if more_bid == 'no':
    game_auction = True
  else:
    print("\n" * 20)

highest_bid = 0
highest_bidder = ""
for bidder in auction:
  bid_amount = auction[bidder]
  if bid_amount > highest_bid:
    highest_bid = bid_amount
    highest_bidder = bidder
print(f"{highest_bidder} won the silent auction with ${highest_bid}")  

# print(name,bid,auction,bid_amount)
