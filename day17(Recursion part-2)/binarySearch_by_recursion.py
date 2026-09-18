# Write a recursive function to implement binary search algorithm
def binarySearch(arr,key,low,high):
    if low>high:
        return -999
    mid=int((low+high)/2)
    if key==arr[mid]:
        return mid
    elif key<arr[mid]:
        high=mid-1
        return binarySearch(arr,key,low,high)
    else:
        low=mid+1
        return binarySearch(arr,key,low,high)

ary=[12,15,21,25,28,32,33,36,43,45]
item=int(input("Enter search item : "))
res=binarySearch(ary,item,0,len(ary)-1)
if res>=0:
    print(item," Found at index ",res)
else:
    print("Sorry! ",item," Not found in array")