def life_in_weeks(current_age):
    live_until_years = 90
    weeks_per_year = 52
    
    total_weeks = live_until_years * weeks_per_year
    weeks_completed = current_age * weeks_per_year
    
    remaining_weeks_in_life = total_weeks - weeks_completed
    
    print(f"You have {remaining_weeks_in_life} weeks left.")
    
life_in_weeks(12)