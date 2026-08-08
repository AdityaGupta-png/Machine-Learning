

# Printing of the odd and even numbers 


n = int(input("Enter the number : "))

sumEven = 0  # for calculate the even numbers sum
sumOdd = 0   # for calculate the odd numbers sum 

for i in range(n+1) :
    
    if(i %2 == 0):
        sumEven += i

    else:
        sumOdd += i
         
print(sumEven)
print(sumOdd)

        
    

        