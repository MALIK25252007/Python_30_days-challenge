# WAP that receives two numbers in a function and returns the result of all arithmetic operations (+,-,*,/,%)
def arCalc(x,y):
    return x+y, x-y, x*y, x/y, x%y

num1=int(input("Enter number1 : "))
num2=int(input("Enter number2 : "))
add, sub, mult, div, mod=arCalc(num1, num2)
print("Sum of given numbers : ",add)
print("Subtraction of given numbers : ",sub)
print("Product of given numbers : ",mult)
print("Division of given numbers : ",div)
print("Modulo of given numbers : ",mod)