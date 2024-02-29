from Art import logo 
import os
print(logo)

bids = {}
bidding_finish = False

def highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of £{highest_bid}")

while not bidding_finish:
    print("Welcome to the secret auction program!")
    name = input("What is your name?: ")
    amount = int(input("What's your bid?: £"))
    bids[name] = amount
    other_bidders = input("Are there any other bidders? Type 'yes' or 'no'. \n")
    print("---------------------------------------------------------------------------------------")
    if other_bidders == "no":
        bidding_finish = True
        highest_bidder(bids)
    elif other_bidders == "yes":
        os.system('cls' if os.name == 'nt' else 'clear')
    