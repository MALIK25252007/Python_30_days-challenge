#WAP to print the GCD of two numbers given by user
a, b, gcd=0,0,0
a=int(input("Enter first number : "))
b=int(input("Enter second number : "))
num1=a
num2=b
while (b != 0) :
        temp = b
        b = a % b
        a = temp 
gcd = a
print("GCD of ",num1," and ",num2," is : ",gcd)