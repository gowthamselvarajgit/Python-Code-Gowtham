def simple_interest_calculator(principal_amount, time_in_years, interest_rate = 10):
    simple_interest = (principal_amount * time_in_years * interest_rate) // 100
    return simple_interest

principal_amount = int(input("Enter the principal amount: "))
time_in_years = float(input("Enter the time period in years: "))
simple_interest = simple_interest_calculator(principal_amount, time_in_years)
print("Simple Interest: ", simple_interest)