#Consider the binary file stu.dat storing student details, which youcreated in earlier programs. Write a program to update the records of the file Stu.dat so that those who have scored more than 81.0 , get additional bonus marks of 2
import pickle
stu={ }
found=False
fin=open('stu.dat','rb+')
try:
    while True: 
        rpos=fin.tell()
        stu=pickle.load(fin)
        if stu['Marks']>81:
            stu['Marks']+=2
            fin.seek(rpos)
            pickle.dump(stu,fin)
            found=True
except EOFError:
    if found==False:
        print("Sorry,no matching record found.")
    else:
        print("Record(s) successfully updated.")
    fin.close()