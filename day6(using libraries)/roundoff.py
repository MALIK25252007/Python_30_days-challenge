#WAP that displays the given number rounded off to 3 place after decimal
num=float(input("Enter a real number : "))
tnum=int(num)
rnum=round(num)
print("Number",num,"converted to integer in 2 ways as ", tnum," and ",rnum)
rnum2=round(num,3)
print(num,"rounded off to 3 places after decimal is ",rnum2)