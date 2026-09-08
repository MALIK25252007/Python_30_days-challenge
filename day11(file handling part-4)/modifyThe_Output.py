#The CSV file (Student.csv) used in the previous program was created on window OS where the EOL character is '\r\n'. Write the code so that the blank lines for every EOL are not displayed.
import csv
with open("Student.csv",'r',newline='\r\n') as fh:
    creader=csv.reader(fh)
    for rec in creader:
        print(rec)