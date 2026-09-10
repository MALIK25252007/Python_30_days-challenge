#WAP to check whether the year given by user is leap year or not
year=int(input("Enter a year to be check : "))
if year%400==0:
    print("This is a Leap year.")
elif year%100==0:
    print("This is a not Leap year.")
elif year%4==0:
    print("This is a Leap year.")
else: 
    print("This is a not Leap year.")   