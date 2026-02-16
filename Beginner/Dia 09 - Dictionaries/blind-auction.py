import os

def clear_console():
    # the command to clear is `cls` on Windows and `clear` on most everything else
    os.system('cls' if os.name == 'nt' else 'clear')

from art import logo

bidding_dict = {}

goAgain = True
while goAgain:

    #Main process
    print(logo)
    print("Welcome to the secret auction program.")
    print()
    name = input("What is your name?: ")
    bid = float(input("What is your bid?: $"))

    bidding_dict[name] = bid

    #Go Again cycle
    print("Are there more bidders? Type 'yes' or 'no'")
    answer = input().lower()

    while answer not in ('yes', 'no'):
        print("Invalid input. Please type 'yes' or 'no'.")
        answer = input().lower()

    if answer == 'yes':
        goAgain = True
    else:
        goAgain = False

    clear_console()

#Showwing the winner
winner_name = name
winner_bid  = bid
for key, value in bidding_dict.items():
    if value > winner_bid:
        winner_name = key
        winner_bid = value


print(logo)
print()
print(f"The winner is {winner_name} with a bid of ${winner_bid}")