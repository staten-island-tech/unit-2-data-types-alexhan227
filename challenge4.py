num1 = int(input("enter a number: "))
num2 = int(input("enter another number: "))

factorsA = []
factorsB = []
def find_factorsB(num1):
    for i in range(1, num1 + 1):
        if num1 % i == 0:  
            factorsB.append(i)

def find_factorsA(num2):
    for i in range(1, num2 + 1):
        if num2 % i == 0:  
            factorsA.append(i)


def GCF(factorsA, factorsB):
    common_factors = []  # List to store common factors
    
    # Find common factors between the two lists
    for i in factorsA:
        if i in factorsB:
            common_factors.append(i)  # Append the common factor to the list
    
    # Manually find the largest common factor
    gcf = 1  # Start with a default value of 1
    for factor in common_factors:
        if factor > gcf:
            gcf = factor  # Update the GCF to the largest common factor found

    return gcf

gcf = GCF(factorsA, factorsB)
print(f"The GCF is: {gcf}")
