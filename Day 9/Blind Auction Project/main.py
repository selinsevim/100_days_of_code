# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary

import art
print(art.logo)
bidding_dict = {}

bidding_over = False
answer = "yes"

while answer == "yes":
    bidding_over = False
    name = input("What's your name?\n")
    bid_number = input("What's your bid?\n")
    bidding_dict[name] = bid_number
    answer = input("Are there any other bidders? Type yes or no")
    print("\n" * 20)

    if answer == "no":
        bidding_over = True

print(bidding_dict)
max_bid = 0
max_bidder = {}
for bidder in bidding_dict:
    bid = int(bidding_dict[bidder])
    if bid > max_bid:
        max_bid = bid
        max_bidder[bidder] = max_bid

for key, value in max_bidder.items():
    print(f"The bidder winner is {key}")