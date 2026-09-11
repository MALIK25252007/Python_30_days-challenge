#WAP to check whether the given number is perfect number or not
num=int(input("Enter a number : "))
digit=2
sum=1
while(digit!=num):
    if num%digit==0:
        sum+=digit
    digit+=1

if sum==num:
    print("This is a perfect number.")
else:
    print("This is not a perfect number.")