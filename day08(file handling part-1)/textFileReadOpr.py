# Wap to display the size of a file in bytes
myFile=open("textfile.txt",'r')
str=myFile.read()
size=len(str)
print("Size of the given file textfile.txt is : ")
print(size,"bytes")

#Wap to display the number of lines in the file 
myFile1=open("textfile.txt",'r')
s=myFile1.readlines()
lineCount=len(s)
print("Number of lines in textfile.txt is : ",lineCount)
myFile1.close()