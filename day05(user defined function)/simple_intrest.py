# Programe to calculate simple intrest using a function intrest() thatcan receive principal amount, time, and rate and returns calculated simple intrest. Do specify default values for rate and time as 10% and 2 years respectively
def intrest(principal,time=2,rate=0.10):
    return principal*rate*time

prin=float(input("Enter principal amount : "))
print("Simple intrest with default ROI and time values is : ")
si1=intrest(prin)
print("Rs. ",si1)
roi=float(input("Enter rate of intrest (ROI) : "))
time=int(input("Enter time in years : "))
print("Simple intrest with your provided ROI and time values is : ")
si2=intrest(prin, time, roi/100 )
print("Rs. ", si2)