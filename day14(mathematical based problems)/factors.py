#WAP to ask user to input a number and program prints its all factors

num=int(input("Enter a number : "))
print("Factors of ",num, " are : ")
digit=2
while(digit!=num):
    if num%digit==0:
        print(digit," ")
    digit+=1

