# Wap to calculate factorial of a given number
num=int(input("Enter a number : "))
fact=1
for a in range(num):
    fact=fact*(a+1)
print("Factorial of this given number is : ",fact)