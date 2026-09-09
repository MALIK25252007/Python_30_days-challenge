#WAP to print the lcm of two numbers given by user
a, b, result, lcm=0,0,0,0
a=int(input("Enter first number : "))
b=int(input("Enter second number : "))
num1=a
num2=b
while (b != 0) :
        temp = b
        b = a % b
        a = temp 
result = a
lcm = (num1 * num2) / result
print("LCM of ",num1," and ",num2," is : ",lcm)