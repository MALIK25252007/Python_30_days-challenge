#Write a recursive function that computes the sum of numbers 1..n ; get the value of last number n from user
def compute(num) :
    if (num==1): 
        return 1
    else:
        return (num + compute(num-1))

last=4
sSum=compute(last)
print("The sum of the series from 1...",last," is ",sSum)