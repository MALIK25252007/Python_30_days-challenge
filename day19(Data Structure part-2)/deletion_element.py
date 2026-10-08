# WAP for deletion of an element from a sorted linear list
def Bsearch(arr,item):
    beg=0
    last=len(arr)-1
    while(beg<=last):
        mid=(beg+last)//2
        if(item == arr[mid]):
            return mid
        elif (item>arr[mid]):
            beg=mid+1
        else:
            last=mid-1
    else:
        return False

myList=[10,20,30,40,50,60,70,80]
print("The list in sorted order is ")
print(myList)
item=int(input("Enter element to be deleted : "))
position=Bsearch(myList,item)
if position:
    del myList[position]
    print("The list after deleting ",item," is ")
    print(myList)
else:
    print("Sorry! No such element in the list")
