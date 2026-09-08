#Write a program to create a csv file by suppressing the EOL translation.
import csv
fh=open("Employee.csv",'w',newline='')
ewriter=csv.writer(fh)
empdata=[
    ['Empno','Name','Designation','Salary'],
    [1001,'shiv','Manager',55000],
    [1002,'raghav','Analyst',45000],
    [1003,'veeru','Clerk',57000],
    [1004,'krish','PR Officer',54000]
    ]
ewriter.writerows(empdata)
print("File successfully created")
fh.close()