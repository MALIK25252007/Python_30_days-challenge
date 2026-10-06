#WAP for linear search in an array (linear list)
def LinearSch(ar,item):
    i=0
    while i<len(ar) and ar[i]!=item:
        i+=1
    if i<len(ar):
        return i
    else:
        return False

n=int(input("Enter how many elements you want to insert (max 50): "))
print("\nEnter elements for linear list: \n")
ar=[0]*n
for i in range(n):
    ar[i]=int(input("Enter "+str(i)+" : "))
item=int(input("\nEnter element to be searched for ..."))
index=LinearSch(ar,item)

if index:
    print("\nElement found at index : ",index," Position : ",(index+1))
else:
    print("\nSorry!! Given element could not be found. ")