def number_reverser(number):
    sign = -1 if number < 0 else 1
    number = abs(number)
    reversed_number = 0
    while (number > 0):
        digit = number % 10
        reversed_number = reversed_number * 10  + digit
        number = number // 10
    return reversed_number * sign
        
print("-----WELCOME TO NUMBER REVERSING SYSTEM-----")
number = int(input("Enter the Number that need to be reversed: "))
reversed_number = number_reverser(number)
print("Reversed Number: ", reversed_number)