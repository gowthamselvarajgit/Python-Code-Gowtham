logo = """
 _____________________
|  _________________  |
| | GowthamCal      | |  .----------------.  .----------------.  .----------------.  .----------------.
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------'
|_____________________|
"""

def add(f_number, n_number):
    return f_number + n_number
    
def sub(f_number, n_number):
    return f_number - n_number

def multiply(f_number, n_number):
    return f_number * n_number
    
def divide(f_number, n_number):
    return f_number // n_number

operations = {
    "+" : add,
    "-" : sub,
    "*" : multiply,
    "/" : divide
}

def calculator():
    print(logo)
    
    should_continue = True
    first_number = float(input("What's the first number?: "))
    
    while should_continue:
        for symbol in operations:
            print(symbol)
        operation = input("Pick an operation: ")
        next_number = float(input("What's the next number?: "))
        
        result = operations[operation](first_number, next_number)
        print(f"{first_number} {operation} {next_number} = {result}")
        
        y_or_n = input(f"Type 'y' to continue with {result}, 'n' for new calculation, or 'q' to quit: ").lower()
        
        if y_or_n == "y":
            first_number = result
        else:
            should_continue = False
            print("\n" * 20)
            calculator()
        
        if y_or_n == "q":
            should_continue = False
            
calculator()
