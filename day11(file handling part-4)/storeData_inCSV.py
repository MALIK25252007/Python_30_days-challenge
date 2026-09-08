#WAP to create a CSV file to store student data (Rollno, Names, Marks). Obtain data from user and write 5 records into the file.
import csv
fh=open("Student.csv",'w')
stuwriter=csv.writer(fh)
stuwriter.writerow(['Rollno','Name','Marks'])

for i in range(5):
    print("Student rcord",(i+1))
    rollno=int(input("Enter rollno : "))
    name=input("Enter name : ")
    marks=float(input("Enter marks : "))
    sturec=[rollno,name,marks]
    stuwriter.writerow(sturec)

fh.close()