#WAP to print nyh fibonacci term given by user
#WAP to print fibonacci series upto the used defined term
nterm=int(input("Enter the fibonacci term you want to print : "))
n1, n2=0, 1
term=2
if nterm <= 0:
    print("Please enter a valid positive integer.")
else:
    print(nterm," th term of fibonacci series is :")
    while term!=nterm:
        nth=n1+n2
        n1=n2
        n2=nth
        term+=1
    print(nth)