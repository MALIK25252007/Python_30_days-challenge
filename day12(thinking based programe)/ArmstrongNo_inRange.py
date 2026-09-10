#WAP to print all Armstrong number in given range
import math
uprLimit=int(input("Enter the upper limit : "))
lwrLimit=int(input("Enter the lower limit : "))
check=False
amrNo=[ ]
for num in range(lwrLimit,uprLimit+1):
    temp=num
    count=0
    rem=0
    result=0
    while temp!=0:
        temp//=10
        count=count+1
    temp=num
    
    while temp!=0:
        rem=temp%10
        result+=pow(rem,count)
        temp//=10
    if result==num:
        check=True
        amrNo.append(num)
if check==True:
    print("Armstrong number(s) in this range : ",amrNo)
else:
    print("No Armstrong number found in this range.")