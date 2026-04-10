# cook your dish here
def fibonacci_generator(nterms):
    number1 = 0
    number2 = 1
    count = 0
    
    if nterms <= 0:
        print("Please enter a positive number")
    elif nterms == 1:
        print("Fibonnaci series upto",nterms,":")
        print(n1)
    else:
        while count < nterms:
            print(number1)
            number3 = number1+ number2
            number1 = number2
            number2 = number3
            count += 1

nterms = int(input("Enter the number for a range: "))
fibonacci_generator(nterms)