#WAP that print the product of digits of the given number
num=int(input("Enter a number : "))
rem=0
product=1
while(num):
    rem=num%10
    num=num//10
    product*=rem
print("Product of digits of this number is : ",product)
