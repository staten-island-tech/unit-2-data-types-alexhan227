""" x = input("Enter a number: ") """
""" digits = [int(digit) for digit in str(x)] """
""" if len(x) > 0:  # Ensure there's at least one digit
    last_digit = x[-1]  # Use -1 to get the last character of the string """
""" if (digits) == [2,4,6,8,0]:
    print("even")
else: 
    print("odd")

 """
x = input("Enter a number: ")  # Input as a string
if len(x) > 0:  # Ensure there's at least one digit
    last_digit = x[-1]  # Use -1 to get the last character of the string
    print(f"The last digit is: {last_digit}")
else:
    print("The number is empty.")