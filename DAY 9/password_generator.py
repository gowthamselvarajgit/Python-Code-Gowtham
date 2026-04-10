import random

letters = [
    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
    "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"
]
numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
symbols = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")"]

print("Welcome to the Password Generator")
no_of_letters = int(input("Enter the number of letters you want in your password: "))
no_of_symbols = int(input("Enter the number of symbols you want in your password: "))
no_of_numbers = int(input("Enter the number of numbres you want in your password: "))

password_list = []

for num in range(1, no_of_letters+1):
    password_list.append(random.choice(letters))
    
for num in range(1, no_of_symbols+1):
    password_list.append(random.choice(symbols))
    
for num in range(1, no_of_numbers+1):
    password_list.append(random.choice(numbers))

random.shuffle(password_list)

password = ""
for char in password_list:
    password = password + char

print(password)
