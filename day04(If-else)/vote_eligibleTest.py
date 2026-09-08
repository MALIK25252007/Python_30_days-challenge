# WAP to input age from user and verify either he is eligible for voting or not
age=int(input("Enter your age : "))
if age > 18:
    print("As per Indian gov. rule you are eligible for voting")
elif age< 18:
    print("As per Indian gov. rule you are not eligible for voting")
else:
    print("You give a false input!!!")