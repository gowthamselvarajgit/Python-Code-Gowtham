db_stored_username = "gowtham26"
db_stored_password = "gowtham@bit7"
username = input("Enter the Username: ")
password = input("Enter the Password: ")
if db_stored_username == username:
    if db_stored_password == password:
        print("User Logged in Successfully")
    else:
        print("Username is correct but password is incorrect")
else:
    print("User doesn't exist")