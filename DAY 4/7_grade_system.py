name = input("Enter the Student Name: ")
mark = int(input("Enter the Student Mark: "))
if mark >= 90:
    print(f"{name} got A Grade")
elif mark >= 75:
    print(f"{name} got B Grade")
elif mark >= 50:
    print(f"{name} got C Grade")
else:
    print(f"{name} got Fail")