logo = '''
  _______ _             _____ _ _            _                        _   _             
 |__   __| |           / ____(_) |          | |       /\             | | (_)            
    | |  | |__   ___  | (___  _| | ___ _ __ | |_     /  \  _   _  ___| |_ _  ___  _ __  
    | |  | '_ \ / _ \  \___ \| | |/ _ \ '_ \| __|   / /\ \| | | |/ __| __| |/ _ \| '_ \ 
    | |  | | | |  __/  ____) | | |  __/ | | | |_   / ____ \ |_| | (__| |_| | (_) | | | |
    |_|  |_| |_|\___| |_____/|_|_|\___|_| |_|\__| /_/    \_\__,_|\___|\__|_|\___/|_| |_|                                                                                        
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

print(logo)

print("*******WELCOME TO THE SECRET AUCTION*******")

restart = True
bidding_dictionary = {}

while restart:
    name = input("What is you name?: ")
    bidding_amount = int(input("Enter your bidding amount: $"))
    next_participant = input("Did there is anyother participant 'Yes' or 'No': ").lower()
    
    if next_participant == "no":
        restart = False
        print("\n" * 100)
    else:
        print("\n" * 100)
        
    bidding_dictionary[name] = bidding_amount


highest_bid = 0
higehest_bid_person = ""
for key in bidding_dictionary:
    if bidding_dictionary[key] > highest_bid:
        highest_bid = bidding_dictionary[key]
        highest_bid_person = key
        
print(f"The winner is {highest_bid_person} with the bid of ${highest_bid}")
    
    
