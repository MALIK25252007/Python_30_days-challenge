#Write a recursive function recurfactorial(n) in python to calculate and return the factorial of a number n passed to the parameter
def recurfactorial(n):
    if n==1:
        return n
    else:
        return n*recurfactorial(n-1)
num=int(input("Enter a number : "))
if num<0:
    print("Sorry, No factorial for negative numbers")
elif num==0:
    print("Factorial of 0 is 1")
else:
    print("The factorial of ",num," is ",recurfactorial(num))