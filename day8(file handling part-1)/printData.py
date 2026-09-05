#Wap to read a text file line by line and display each word saperated by a #
myFile=open("textfile.txt",'r')
line=" "
while line:
    line=myFile.readline()
    for word in line.split():
        print(word,end='#')
    print()
myFile.close()