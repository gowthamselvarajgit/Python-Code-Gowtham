def digit_counter(number):
    digit_count = 0
    while number != 0:
        digit_count += 1
        number = number // 10
    return digit_count
    

def check_armstrong_number(number):
    digit_count = digit_counter(number)
    duplicate_number = number
    result = 0   # initialize result before using it
    while number != 0:
        digit = number % 10
        result += digit ** digit_count
        number = number // 10

    if result == duplicate_number:
        return True
    else:
        return False
    

number = int(input("Enter the number: "))
result = check_armstrong_number(number)
if result:
    print("It is an Armstrong number")
else:
    print("It is not an Armstrong number")
