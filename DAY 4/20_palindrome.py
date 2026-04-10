orginal_number = int(input("Enter a Number: "))
duplicate_number = orginal_number
reversed_number = 0
while(duplicate_number != 0):
    digit = duplicate_number % 10
    reversed_number = reversed_number * 10 + digit
    duplicate_number = duplicate_number // 10
if reversed_number == orginal_number:
    print("It is a Palindrome")
else:
    print("It is not a Palindrome")
    