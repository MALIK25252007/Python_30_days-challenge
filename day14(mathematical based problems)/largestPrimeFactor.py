#Write a program to print largest prime factor of given number
num=int(input("Enter a number : "))
largestPrimeFactor =-1
temp=num
while (temp % 2 == 0):
    largestPrimeFactor = 2
    temp //= 2

for i in range (3, num//2):
    while (temp % i == 0):
        largestPrimeFactor = i
        temp //= i
        i=i+2
        
    
if (num > 2):
    print("largest Prime Factor of this number is : ",largestPrimeFactor)
    
elif (largestPrimeFactor == -1):
    print("No prime factor found.")
else:
    print("Some error happend.")