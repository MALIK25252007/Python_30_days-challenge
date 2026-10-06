# WAP for inserting element in a sorted array using traditional algorithm
def FindPos(arr,item):
    size=len(arr)
    if item<arr[0]:
        return 0
    else:
        pos=-1
    for i in range(size-1):
        if (arr[i]<=item and item<arr[i+1]):
            pos=i+1
            break
        if (pos==-1 and i<=size-1):
            pos=size
        return pos

def Shift(arr,pos):
    arr.append(None)
    size=len(arr)
    i=size-1
    while i>=pos:
        arr[i]=arr[i-1]
        i=i-1

myList=[10,20,30,40,50,60,70,80]
print("The list in sorted array is : ")
print(myList)
item=int(input("Enter new element to be inserted : "))
position=FindPos(myList,item)
Shift(myList,position)
myList[position]=item
print("The list after inserting ",item," is ")
print(myList)