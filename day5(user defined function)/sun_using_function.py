#Program to add two numbers through a function
def calcSum(x,y):
    s=x+y
    return s

num1=float(input("Enter first number : "))
num2=float(input("Enter second number : "))
sum=calcSum(num1,num2)
print("sum of these two numbers is : ",sum)