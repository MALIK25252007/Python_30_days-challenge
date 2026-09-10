#WAP to check weather the number given by user is a Armstrong or not
import math
num=int(input("Entre a number : "))
temp=num
count=0
rem=0
result=0
while temp!=0:
    temp=temp//10
    count=count+1
temp=num

while temp!=0:
    rem=temp%10
    result+=pow(rem,count)
    temp//=10
if result==num:
    print("This is a Armstrong number.")
else:
    print("This is not a Armstrong number.")