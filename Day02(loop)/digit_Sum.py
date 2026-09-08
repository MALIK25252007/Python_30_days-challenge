# WAP to input a number a prints the sum of its digits 
num=int(input("Enter a number"))
sum=0
while num>0:
    rem=0
    rem=num%10
    sum=sum+rem
    num=num//10
print("Sum of digits of this number is : ",sum)