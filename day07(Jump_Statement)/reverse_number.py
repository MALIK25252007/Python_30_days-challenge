#WAP to print the reverse of the givem number
num=int(input("Enter a number : "))
temp=0
while(num):
    temp*=10
    temp+=num%10
    num=num//10
print("Number after reversing : ",temp)   