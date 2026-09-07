#Read file stu.dat created in earlier programs and display records having marks > 81
import pickle
stu={ }
found=False
print("Searching in the file ...")
with open('stu.dat','rb') as fin:
    stu=pickle.load(fin)
    if stu['Marks']>81:
        print(stu)
        found=True
if found==False:
    print("No such record found !!")
else:
    print("Search successful.")