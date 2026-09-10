#WAP that checks the password given by user is valid or not as per instructions
#Password must be in following format : first 4 letters of user name(capitalised) + first 4 digit of phone no.
name=input("Please enter your name in capital letters : ")
phone=input("Please enter your 10 digit phone number : ")
password=input("Enter your password : ")
temp=name[:4]+phone[:4]

if password==temp:
    print("Password is correct.")
else:
    print("You enter a invalid password.")