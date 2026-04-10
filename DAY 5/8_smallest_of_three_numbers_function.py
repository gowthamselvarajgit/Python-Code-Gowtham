def find_smallest(number1, number2, number3):
    return min(number1, number2, number3)

number1 = int(input("Enter the First Number: "))
number2 = int(input("Enter the Second Number: "))
number3 = int(input("Enter the Third Number: "))
smallest_number = find_smallest(number1, number2, number3)
print(smallest_number)