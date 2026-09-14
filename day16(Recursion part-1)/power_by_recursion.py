# program to show the use of recursion in calculation of power e.g. a^b
def power(a,b):
    if b==0:
        return 1
    else:
        return a*power(a,b-1)

print("Enter only the positive numbers below")
num=int(input("Enter base number : "))
p=int(input("raised to the power of : "))
result=power(num,p)
print(num," raised to the power of ",p," is ",result)