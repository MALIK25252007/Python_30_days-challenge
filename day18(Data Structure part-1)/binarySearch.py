#WAP for binary search in an array

def BinarySrch(arr,item):
    beg=0
    last=len(arr)-1
    while(beg<=last):
        mid=(beg+last)//2
        if(item==arr[mid]):
            return mid
        elif(item>arr[mid]):
            beg=mid+1
        else:
            last=mid-1
    else:
        return False

n=int(input("Enter desired linear list size (max 50) : "))
print("\nEnter elements for linear list in accending order\n")
arr=[0]*n
for i in range(n):
    arr[i]=int(input("Element "+str(i)+" : "))
item=int(input("\nEnter element to be searched for ..."))
index=BinarySrch(arr,item)

if index:
    print("\nElement found at index : ",index,", Position : ",(index+1))
else:
    print("\nSorry!! Given element not found.")