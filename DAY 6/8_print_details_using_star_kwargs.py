def student_details(**data):
    for key, value in data.items():
        print(key, " : ", value)

student_details(name = "Gowtham", age = 22, dept = "EIE")