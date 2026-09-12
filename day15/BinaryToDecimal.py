#WAP that takes input of a binary number and print its Decimal equivalent
def binary_to_decimal(binary_str):
    binary_str = binary_str.strip()
    
    if len(binary_str) == 0:
        return None

    for char in binary_str:
        if char != "0" and char != "1":
            return None

    decimal_value = 0
    for digit in binary_str:
        decimal_value = decimal_value * 2 + int(digit)

    return decimal_value


user_input = input("Enter a binary number: ")
result = binary_to_decimal(user_input)

if result is not None:
    print(f"The decimal equivalent of {user_input.strip()} is {result}.")
else:
    print("Invalid binary number. Please enter only 0s and 1s.")