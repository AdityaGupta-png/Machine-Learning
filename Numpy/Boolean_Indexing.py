
# Practising the boolean indexing 

import numpy as np

#Example number 1 
a1 = np.random.randint(0,100,24).reshape(6,4)
print(a1)
# Boolean Indexing --> find the numbers which are greature than 50 
print(a1[a1>50])

# Example number 2 
a2 = np.arange(1,31).reshape(6,5)
print(a2)
# Find the numbers whic are divisible by 2 
print(a2[a2 % 2 == 0])

# Example number 3 
a3 = np.random.randint(0,100,25).reshape(5,5)
print(a3)
# find the numbers which are greature than 50 and divisible by 2
print(a3[(a3 > 50) & (a3 % 2 == 0)])

# Example number 4 
a4 = np.random.randint(0,150,60).reshape(6,10)
print(a4)
# Numbers are not divisible by 7 
print(a4[(a4 % 7 != 0)])
