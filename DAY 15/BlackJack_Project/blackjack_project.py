import random

logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10]
    return random.choice(cards)
    
def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
        
    score = sum(cards)
    return score
    
def compare(my_score, computer_score):
    if computer_score == my_score:
        return "Draw"
    elif computer_score == 0:
        return "Lose, opponent has Blackjack"
    elif my_score == 0:
        return "Win with a Blackjack"
    elif my_score > 21:
        return "You went over. You lose"
    elif computer_score > 21:
        return "Oppenent went over. You win"
    elif my_score > computer_score:
        return "You win"
    else:
        return "You lose"

def play_game():
    print(logo)
    my_cards = []
    computer_cards = []
    computer_score = -1
    my_score = -1
    
    for _ in range(2):
        my_cards.append(deal_card())
        computer_cards.append(deal_card())
        
    is_game_over = False  
      
    while not is_game_over:
        my_score = calculate_score(my_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards: {my_cards}, current score: {my_score}")
        print(f"Computers's first cards: {computer_cards[0]}")
        
        if my_score == 0 or computer_score == 0 or my_score > 21:
            is_game_over = True
        else:
            should_continue = input("Type 'y' to get another card, type 'n' to pass: ").lower()
            if should_continue == "y":
                my_cards.append(deal_card())
            else:
                is_game_over = True
                
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)
        
    print(f"Your final hand: {my_cards}, final score : {my_score}")
    print(f"Computer final hand: {computer_cards}, final score : {computer_score}")
    print(compare(my_score,computer_score))
    
while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower():
    print("\n" * 20)
    play_game()





