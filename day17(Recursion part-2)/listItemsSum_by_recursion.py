#Write a recursive code to find the sum of all elements of a list
def sumof(l,n):
    if n==0:
        return l[0]
    else:
        return l[n]+sumof(l,n-1)

list1=[10,20,30,40,50]
size=len(list1)
print("Sum = ",sumof(list1,size-1))