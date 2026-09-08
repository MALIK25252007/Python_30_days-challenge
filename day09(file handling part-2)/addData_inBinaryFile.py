#WAP to get student data (rollno, name, and marks) from user and write onto a binary file.
#The program should be able to get data from the user and write onto the file as long as the user wants.
import pickle
stu={ }
stufile=open('stu.dat','wb')
ans='y'
while ans=='y':
    rno=int(input("Enter roll number : "))
    name=input("Enter name : ")
    marks=float(input("Enter marks : "))
    stu['Rollno']=rno
    stu['Name']=name
    stu['Marks']=marks
    pickle.dump(stu,stufile)
    ans=input("want to enter more records? (y/n)... ")
stufile.close()