
# Check the number is perfsect number is not 


n = int(input("Check the number is perfect square or not : "))

sum = 0

for i in range(1,n):
    
    if(n % i == 0):
        sum += i
        
if (sum == n):
    print("The number is perfect square of itself")
else:
    print("The number is not perfect square of itself")