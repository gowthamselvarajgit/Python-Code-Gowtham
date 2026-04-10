def find_max(*numbers):
    largest = numbers[0]
    for i in numbers:
        if i > largest:
            largest = i
    return largest

print(find_max(1,3,2,4,3))