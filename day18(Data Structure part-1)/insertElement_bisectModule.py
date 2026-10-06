# WAP for inserting element in sorted array using bisect module
import bisect
myList=[10,20,30,40,50,60,70,80]
print("The list in sorted order is : ")
print(myList)
item=int(input("Enter new element to be inserted : "))
ind=bisect.bisect(myList,item)
bisect.insort(myList,item)

print(item," Inserted at index ",ind)
print("The list after inserting new element is : ")
print(myList)
