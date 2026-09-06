#WAP to read a text file and display the count of vowels and consonants in the file
myfile=open("textfile.txt",'r')
ch=' '
vcount=0
ccount=0
while ch:
    ch=myfile.read(1)
    if ch in ['a','e','i','o','u','A','E','I','O','U']:
        vcount+=1
    else:
        ccount+=1
print("Vowels in the file : ",vcount)
print("Consonants in the file : ",ccount)
myfile.close()