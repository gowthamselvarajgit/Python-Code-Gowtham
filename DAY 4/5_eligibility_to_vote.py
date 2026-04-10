name = input("Enter Voter Name: ")
age = int(input("Enter the Voter Age: "))
if(age >= 18):
    print(f"{name} is Eligible to Vote")
else:
    print(f"{name} is Not Eligible to Vote")
    