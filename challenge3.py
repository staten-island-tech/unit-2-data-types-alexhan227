number = int(input("enter a number: "))
def find_factors(number):
    factors= []
    #lists the factors
    for i in range(1, number + 1):
        if number % i == 0:  # If 'i' is a factor of 'number'
            factors.append(i)  # Add 'i' to the factors list
    return factors  # Return the list of factors after the loop completes

# Call the function and print the result
factors = find_factors(number)

print(f"Factors of {number}: {factors}")