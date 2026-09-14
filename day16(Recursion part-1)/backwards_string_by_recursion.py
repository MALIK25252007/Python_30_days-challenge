# Write a recursive function to print a string backwards
def bp(sg,n):
    if n>0:
        print(sg[n],end='')
        bp(sg,n-1)
    elif n==0:
        print(sg[0])

s=input("Enter a string : ")
bp(s,len(s)-1)