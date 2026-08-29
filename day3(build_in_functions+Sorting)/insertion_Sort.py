# program to sort a sequence using insertion sort
aList=[24,46,1,288,39,47]
print("Original list : ", aList)
for i in range(1,len(aList)):
    key=aList[i]
    j=i-1
    while j>=0 and key< aList[j]:
        aList[j+1]=aList[j]
        j=j-1
    else:
        aList[j+1]=key
print("List after sorting : ",aList)