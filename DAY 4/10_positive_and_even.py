number = int(input("Enter the Number: "))
if number > 0:
    if(number % 2 == 0):
        print("The Number is Positive and Even")
    else:
        print("The Number is Positive and Odd")
elif number < 0:
    if(number % 2 == 0):
        print("The Number is Negative and Even")
    else:
        print("The Number is Negative and Odd")
else:
    print("The Number is zero")