#WAP to read the records of the CSV file created before
import csv
with open("Student.csv",'r') as fh:
    creader=csv.reader(fh)
    for rec in creader:
        print(rec)
        