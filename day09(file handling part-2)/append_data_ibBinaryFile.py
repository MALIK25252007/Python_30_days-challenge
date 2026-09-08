#WAP to append student records to file created in previous program, by getting data from user.
import pickle
stu={ }
stufile=open('stu.dat','ab')
ans='y'
while ans=='y' or ans=='Y':
    rno=int(input("Enter roll number : "))
    name=input("Enter name : ")
    marks=float(input("Enter marks : "))
    stu['Rollno']=rno
    stu['Name']=name
    stu['Marks']=marks
    pickle.dump(stu,stufile)
    ans=input("Want to append more records? (y/n)... ")
stufile.close()