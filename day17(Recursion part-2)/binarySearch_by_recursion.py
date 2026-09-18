# WAP for binary searching in an array (a sorted list)
def binarySearch(arr,key):
    low=0
    high=len(arr)-1
    while low<=high:
        mid=int((low+high)/2)
        if key == arr[mid]:
            return mid
        elif key<arr[mid]:
            high=mid-1
        else:
            low=mid+1
    else:
        return -999
arr=[12,15,21,25,28,32,33,36,43,45]
item=int(input("Enter search item : "))
res=binarySearch(arr,item)
if res>=0:
    print(item,"Found at index ",res)
else:
    print("Sorry! ",item," Not found in array")