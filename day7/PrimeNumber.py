#WAP that reads a number and verify that whether it is prime or not
num=int(input("Enter a number : "))
isPrime=True
if num<=1:
    print("Invalid ,input number should not equal to or less than 1 Hence:")
    isPrime=False
else:
    for i in range(2,num//2):
        if num%i==0:
            isPrime=False
            break
if(isPrime):
    print("This is a prime number.")
else:
    print("This is not a prime number.")
