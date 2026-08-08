

# Printing the factoraial of the numbers 

n = int(input("Enter the number : "))

product = 1;

for i in range(n,0,-1):
    product *= i

print(product)