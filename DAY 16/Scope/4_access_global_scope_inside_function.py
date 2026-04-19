#global variable
name = "Gowtham"

def student_name():
    #Can change the real global scope otherwise new local name variable will be created
    global name
    name = "Gowtham Selvaraj"
    print(f"Name inside the function {name}")
    
student_name()
print(f"Name outside the function {name}")