def square(number):
    return number * number

def display_result(number):
    result = square(number)
    print(result)

number = int(input("Enter the number: "))
display_result(number)
    