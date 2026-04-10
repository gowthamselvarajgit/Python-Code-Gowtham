number1 = int(input("Enter the First Number: "))
number2 = int(input("Enter the Second Number: "))
number3 = int(input("Enter the Third Number: "))
if (number1 >= number2) and (number1 >= number3):
    print("First Number is Greater than Second and Third Number")
elif (number2 >= number1) and (number2 >= number3):
    print("Second Number is Greater than First and Third Number")
else:
    print("Third Number is Greater")
    