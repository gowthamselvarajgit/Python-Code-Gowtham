def check_even_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

def display_result(number):
    result = check_even_odd(number)
    print(result)

number = int(input("Enter the number: "))
display_result(number)
    