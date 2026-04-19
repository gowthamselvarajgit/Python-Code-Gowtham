def is_prime(num):
    if num == 0 or num == 1:
        return False
    
    for i in range(2, num):
        if num % i == 0:
            return False
            
    return True
   
number = int(input("Enter the number: "))
result = is_prime(number)

if result == True:
    print("It is a prime number")
else:
    print("It is not a prime number")
    
    
    