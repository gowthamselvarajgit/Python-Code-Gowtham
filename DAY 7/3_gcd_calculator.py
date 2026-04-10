def gcd(number1, number2):
    while number2 != 0:
        number1, number2 = number2, number1 % number2
    return number1

number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
result = gcd(number1, number2)
print(result)