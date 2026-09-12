#WAP that takes input from user and prints its count of bits 
num=int(input("Enter a non negative number : "))
if num<0:
    print("Invalid input !!!")
else:
    print("bits count for this number is : ")
    count=0
    while(num):
        num&=(num-1)
        count+=1
    print(count)