# WAP that inputs a main string ad then creates an incrypted string by embedding a short symbol based string after each caracter. The program sould alsobe able to produce the decrypted string from encrypted string
def encrypt(sttr,enkey):
    return enkey.join(sttr)
def decrypt(sttr,enkey):
    return sttr.split(enkey)

mainString=input("Enter main string : ")
encryptStr=input("Enter encryption key : ")
enStr=encrypt(mainString,encryptStr)
deLst=decrypt(enStr,encryptStr)

deStr="".join(deLst)
print("The encrypted string is ",enStr)
print("String after decryption is : ",deStr)
