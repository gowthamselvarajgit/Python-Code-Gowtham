#global variable
name = "Gowtham"

def student_name(name_of_student):
    print(f"Name inside the function {name_of_student}")
    return name_of_student + " selvaraj"
    
name = student_name(name)
print(f"Name outside the function {name}")