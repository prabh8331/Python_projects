from art import logo
import os

print(logo)

iterate = True

biddings={}

while iterate == True:
    bidder=input("What is your name?: ")
    bid=float(input("What is your bid amount?: $"))
    biddings[bidder]=bid
    more_bids=input("Are there more bidders? yes/no:\n").lower()
    if more_bids == "no":
        iterate=False
    os.system('cls')


highest_bid=0

for key in biddings:
    if biddings[key] > highest_bid:
        highest_bid=biddings[key]
        winner=key


print(f"The winner is {winner} with a bid of ${highest_bid}")

# print(biddings)