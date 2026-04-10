print("------WELCOME TO THE SIMPLE CALCULATOR------")
number1 = int(input("Enter the First Number: "))
number2 = int(input("Enter the Second Number: "))
operation = input("Enter the Operation to be Done('+','-','*','/', '%'): ")
if operation == '+':
    result = number1 + number2
elif operation == '-':
    result = number1 - number2
elif operation == '*':
    result = number1 * number2
elif operation == '/':
    if number2 != 0:
        result = number1 / number2
    else:
        result = "Number2 should not be zero"
elif operation == '%':
    if number2 != 0:
        result = number1 % number2
    else:
        result = "Number2 should not be zero"
else:
    result = "Operation is Invalid"
print(f"Result : {result}")