def play_game():
    bidders = {}
    name = input("What is your name: ").upper()
    bid = input("What is your bid: ")
    bidders[name] = bid
    ans = input("Is there another person for the bidding(yes/no): ").lower()

    while ans == "yes":
        name = input("What is your name: ").upper()
        bid = input("What is your bid: ")
        bidders[name] = bid
        ans = input("Is there another person for the bidding(yes/no): ").lower()
    
    highest_bid = 0
    highest_bidder = ""
    for thing in bidders:
        if int(bidders[thing]) > highest_bid:
            highest_bid = int(bidders[thing])
            highest_bidder = thing.upper()
    
    print(f"The highest bid was of {highest_bid} by {highest_bidder}")