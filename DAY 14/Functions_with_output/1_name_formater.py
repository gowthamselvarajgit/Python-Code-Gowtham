def format_name(first_name, last_name):
    return first_name.title() + " " + last_name.title()
    
f_name = input("Enter the First Name: \n")
l_name = input("Enter the Last Name: \n")

formated_name = format_name(f_name, l_name)
print(formated_name)