#WAP to open file stu.dat and search for records with roll numbers as 12 or 14. If found display the records.
import pickle
stu={ }
found=False
fin=open('stu.dat','rb')
searchkeys=[12,14]
try:
    print("Searching in file ...")
    while True:
        stu=pickle.load(fin)
        if stu['Rollno'] in searchkeys:
            print(stu)
            fount=True
except EOFError:
    if found==False:
        print("No such record found in file.")
    else:
        print("Search successful.")
    fin.close()