# Program to sort a list using bubble sort
aList=[15,3,66,7,35,67]
print("Original list : ", aList)
n=len(aList)

for a in range(n):
    for j in range(0,n-1-1):
        if aList[j] > aList[j+1]:
            aList[j],aList[j+1]= aList[j+1],aList[j]
print("List after sorting : ",aList)