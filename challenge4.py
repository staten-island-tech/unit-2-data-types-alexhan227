def gcd(a, b):
    while b:
        a, b = b, a % b  # Replace 'a' with 'b' and 'b' with 'a % b'
    return a  # The last non-zero remainder is the GCF

# Example usage:
num1 = int(input("enter a number: "))
num2 = int(input("enter another number: "))
result = gcd(num1, num2)
print(f"The GCF of {num1} and {num2} is {result}")