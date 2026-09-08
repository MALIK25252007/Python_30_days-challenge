# WAP that reads a line and prints its statistics like: 
# *no. of uppercase/lowercasw letters , *no. of alphabates, *no. of digits

line=input("Enter a line : ")
lowerCount=upperCount=0
digitCount=alphaCount=0
for a in line:
    if a.islower():
        lowerCount+=1
    elif a.isupper():
        upperCount+=1
    elif a.isdigit():
        digitCount+=1
    if a.isalpha():
        alphaCount+=1
print("------------------------------------")
print("Number of uppercase letters : ",upperCount)
print("------------------------------------")
print("Number of lowercase letters : ",lowerCount)
print("------------------------------------")
print("Number of alphabets : ",alphaCount)
print("------------------------------------")
print("Number of digits : ",digitCount)

