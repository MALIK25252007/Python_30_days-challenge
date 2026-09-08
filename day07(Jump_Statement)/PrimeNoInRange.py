#WAP to find all the prime numbers in the given range
lower=int(input("Enter lower limit : "))
upper=int(input("Enter upper limit : "))
primeNums=[]
for  a in range(lower,upper+1):
    isPrime=True
    if a<=2:
        continue
    else:
        for i in range(2,(a//2)+1):
            if a%i==0:
                isPrime=False
                
        if isPrime==False:
            continue
        else:
            primeNums.append(a)   


if len(primeNums)==0:
    print("No prime number found in this range.")
else:
    print("Prime numbers in this range : ",primeNums)