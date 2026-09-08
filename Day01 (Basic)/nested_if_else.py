# Wap to check wether the candidate is eligible for interview or not
print("---------------------------------------")
print("Answer the following questions correctly (y/n)")
age=input("Are you 18+ : ")

if age=='y':
    qualification=input("Does you completed your degree : ")
    if qualification=='y':
        print("you are eligible for interview")
    else:
        print("you are not eligible for interview")
else:
    print("you are not eligible for interview")