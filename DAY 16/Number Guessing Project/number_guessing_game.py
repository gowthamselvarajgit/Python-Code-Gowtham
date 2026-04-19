import random
logo = '''
  / _ \_   _  ___  ___ ___  /__   \ |__   ___    /\ \ \_   _ _ __ ___ | |__   ___ _ __ 
 / /_\/ | | |/ _ \/ __/ __|   / /\/ '_ \ / _ \  /  \/ / | | | '_ ' _ \| '_ \ / _ \ '__|
/ /_\\| |_| |  __/\__ \__ \  / /  | | | |  __/ / /\  /| |_| | | | | | | |_) |  __/ |   
\____/ \__,_|\___||___/___/  \/   |_| |_|\___| \_\ \/  \__,_|_| |_| |_|_.__/ \___|_|    
'''

def random_number_generator():
    r_number = random.randint(1,100)
    return r_number

def number_compare(r_number, attempts):
    print(f"You have {attempts} attempts remaining to guess the number.")
    guessed_number = int(input("Make a guess: "))
    
    if guessed_number > r_number:
        return 0
    elif guessed_number < r_number:
        return -1
    else:
        return 1
        
print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

random_number = random_number_generator()
print(random_number)

level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

if level == "easy":
    attempts = 10
elif level == "hard":
    attempts = 5
else:
    print("Invalid choice. Defaulting to hard.")
    attempts = 5

    
win = 0

while attempts != 0 and win != 1:
    result = number_compare(random_number, attempts)
    if result == 0:
        print("Too high.\nGuess again.")
        attempts = attempts -1
    elif result == -1:
        print("Too low.\nGuess again.")
        attempts = attempts -1
    else:
        print(f"You got it! The answer was {random_number}")
        win = 1
        
if attempts == 0:
    print("Out of chance! You Lose")
        
        





