#WAP that takes input of a Decimal number and print its binary equivalent
def decimal_to_binary(number):
    number = number.strip()

    if not number.isdigit():
        return None

    num = int(number)
    
    if num == 0:
        return "0"

    binary_digits = []
    while num > 0:
        remainder = num % 2
        binary_digits.append(str(remainder))
        num = num // 2

    binary_digits.reverse()
    return "".join(binary_digits)


user_input = input("Enter a positive decimal number: ")
result = decimal_to_binary(user_input)

if result is not None:
    print(f"The binary equivalent of {user_input.strip()} is {result}.")
else:
    print("Invalid input. Please enter a positive integer.")