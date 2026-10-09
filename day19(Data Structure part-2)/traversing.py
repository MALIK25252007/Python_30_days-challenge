# WAP for traversing a linear list
def traverse(arr):
    size=len(arr)
    for i in range(size):
        print(arr[i],end=' ')

size=int(input("Enter the size of linear list to be input : "))
arr=[None]*size
print("Enter elements for linear list")
for i in range(size):
    arr[i]=int(input("Element "+str(i)+" : "))
print("Traversing the list : ")
traverse(arr)