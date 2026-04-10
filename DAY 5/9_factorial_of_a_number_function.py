def factorial_calculator(number):
    factorial = 1
    for i in range(1, number+1):
        factorial = factorial * i
    return factorial

number = int(input("Enter the Number: "))
factorial_value = factorial_calculator(number)
print(f"The factorial of a number {number} is {factorial_value}")
