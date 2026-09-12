#WAP to calculate the power of a base to the exponent without using exponential operator(**)
def power(base, exp):
    ans = 1
    for i in range(exp):
        ans *= base
    return ans


user_input = input("Enter base and exponent: ").split()

if len(user_input) == 2 and user_input[0].isdigit() and user_input[1].isdigit():
    base = int(user_input[0])
    exp = int(user_input[1])
    print(f"{base} raised to the power {exp} is : {power(base, exp)}")
else:
    print("Please enter two positive integers.")