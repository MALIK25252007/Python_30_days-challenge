# WAP to check and print wether the input number is even, odd or 0
num=int(input("Enter a Positive number : "))
if num==0:
    print("The given input is 0")
elif num%2==0:
    print("This is a even number")
elif num%2==1:
    print("This is a odd number")
else:
    print("Your input is invalid!!")