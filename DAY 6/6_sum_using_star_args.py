def sum_calculator(*numbers):
    total = 0
    for num in numbers:
        total = total + num
    return total

# user_input = input("Enter the numbers using commas: ")
# numbers = tuple(map(int, user_input.split(',')))
# sum = sum_calculator(numbers)
sum = sum_calculator(1,2,3,4,5)
print(sum)