
from art import logo
#HINT: You can call clear() to clear the output in the console.

print(logo)

all_bids = {}
will_continue = True

def find_highest_bid(all_bids):
    max = 0
    for key in all_bids:
        if all_bids[key] > max:
            max = all_bids[key]
            winner = key
    print(f"The winner is {winner} with a ${max} bid")


while will_continue:
    name = input("What is the name of a person?: ")
    bid = int(input("What is the Bid Price?: $"))
    all_bids[name] = bid
    will_continue = input("Do you want to add a Bid? [yes], [no]: ")
    if will_continue == 'no':
        will_continue = False

find_highest_bid(all_bids)



