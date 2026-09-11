#WAP to check whether the given number is strong number or not

def fact(a):
    factorial=1
    for i in range(2,a+1):
        factorial*=i
    return factorial


num=int(input("Enter a number : "))
temp=num
sum=0
rem=0
while(temp!=0):
    rem=temp%10
    sum+=fact(rem)
    temp//=10
if sum==num:
    print("This is a strong number.")
else:
    print("This is not a strong number.")