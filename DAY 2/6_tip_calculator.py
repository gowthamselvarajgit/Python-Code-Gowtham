print("Welcome to the tip calculator!")
total_bill = float(input("What was the total bill? $"))
tip_percentage = int(input("How much tip would you like to give? 10,20, or 15? "))
number_of_people = int(input("How much people to split the bill? "))
tip = total_bill * (tip_percentage / 100)
total_bill = total_bill + tip
print("Each person should pay: " + "$" + str(round(total_bill / number_of_people, 2)) )