# WAP to read a number and print its number of digits
num=int(input("Enter a number"))
count=0
while num >0:
    num=num//10
    count=count+1
print("The number of digit in this number is : ",count)


