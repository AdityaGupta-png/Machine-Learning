

# Generate the factor of the numbers 

n = int(input("Which number do you want factor : "))

numbers = 0

for i in range(1,n+1):
    
    if n % i ==0 :
        numbers = i
        print(numbers)