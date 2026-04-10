def second_largest_finder(list_numbers):
    largest = float('-inf')
    second_largest = float('-inf')
    
    for num in list_numbers:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num != largest:
            second_largest = num
            
    return second_largest

list_numbers = list(map(int, input("Enter the numbers seperated by space: ").split()))
second_largest = second_largest_finder(list_numbers)
print(second_largest)