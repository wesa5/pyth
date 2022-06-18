

bids = {}

def highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_ammount = bidding_record[bidder]
        if bid_ammount > highest_bid:
            highest_bid = bid_ammount
            winner = bidder
    print(f"The winner is {winner} with bid amount of ${highest_bid}")

bidding_finished = False
while not bidding_finished:
    name = input("what is your name? ")
    bid = int(input("How much are you bidding?: $ "))

    bids[name] = bid
    should_continue = input("Are there any other bidders? Type 'yes' or 'no'\n")
    if should_continue == "no":
        bidding_finished = True
        highest_bidder(bids)
