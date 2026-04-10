def second_largest_finder(list_numbers):
    unique_list = list(set(list_numbers))
    unique_list.sort()
    return unique_list[-2]

list_numbers = list(map(int, input("Enter the numbers seperated by space: ").split()))
second_largest = second_largest_finder(list_numbers)
print(second_largest)