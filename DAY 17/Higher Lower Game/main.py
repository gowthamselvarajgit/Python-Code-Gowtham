import random
from game_data import data
from game_art import logo, vs  

def format_data(account):
    name = account["name"]
    description = account["description"]
    country = account["country"]
    return f"{name}, a {description}, from {country}"

random_a = random.choice(data)
def get_random_accounts(game_data):
    global random_a
    random_b = random.choice(game_data)

    while random_a == random_b:
        random_b = random.choice(game_data)

    print(f"Compare A: {format_data(random_a)}.")
    print(vs)
    print(f"Against B: {format_data(random_b)}.")
    return random_a, random_b

def followers_compare(account_a,account_b):  
    global random_a
    input_guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    if account_a['follower_count'] > account_b['follower_count']:
        correct_answer = 'a'
        random_a = account_a
    else:
        correct_answer = 'b'
        random_a = account_b

    if input_guess == correct_answer:
        print(random_a)
        return True
    else:
        return False

game_should_continue = True
score = 0

while game_should_continue:
    print(logo)
    print(f"Current score: {score}.")
    random_accounts = get_random_accounts(data)
    result = followers_compare(random_accounts[0], random_accounts[1])

    if result == True:
        score += 1
        print(f"You're right! Current score: {score}.")
        print("\n" * 10)
    else:
        print(f"Sorry, that's wrong. Final score: {score}.")
        game_should_continue = False
