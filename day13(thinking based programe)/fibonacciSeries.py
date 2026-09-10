#WAP to print fibonacci series upto the used defined term
nterms=int(input("How many terms? : "))
n1, n2=0, 1
count=0
if nterms <= 0:
    print("Please enter a valid positive integer.")
elif nterms==1:
    print("Fibonacci series upto ",nterms,": ")
    print(n1)
elif nterms==2:
    print("Fibonacci series upto ",nterms,": ")
    print(n1)
    print(n2)
else:
    print("Fibonacci series :")
    print(n1)
    print(n2)
    for i in range(3,nterms+1):
        nth=n1+n2
        print(nth)
        n1=n2
        n2=nth