print("---------------------------------------")
print(" ------ Calculator using if else ------")
print("---------------------------------------")

name=input("Enter your name: ")
roll=int(input("Enter your roll no.: "))

print("---------------------------------------")

num1=int(input("Enter first number : "))
char=input("Enter the operation(+,-,/,//,^) : ")
num2=int(input("Enter second number : "))

if(char=="+"):
    print("---------------------------------------")
    print(num1, "+", num2, "=", num1+num2)
elif(char=="-"):
    print("---------------------------------------")
    print(num1, "-", num2, "=", num1-num2)
elif(char=="*"):
    print("---------------------------------------")
    print(num1, "*", num2, "=", num1*num2)
elif(char=="/"):
    print("---------------------------------------")
    print(num1, "/", num2, "=", num1/num2)
elif(char=="//"):
    print("---------------------------------------")
    print(num1, "//", num2, "=", num1//num2)
elif(char=="^"):
    print("---------------------------------------")
    print(num1, "^", num2, "=", num1**num2)
else:
    print("---------------------------------------")
    print("invalid operator used !!!!")
