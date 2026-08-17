
# Import the numpy 
import numpy as np

# Create the array 
a1 = np.arange(1,13)
a2 = np.arange(1,13).reshape(3,4)
a3 = np.arange(1,9).reshape(2,2,2)
print(a1)
print(a2)
print(a3)

# Access the index from the one 1 D array 
print(a1)
print(a1[-1])  # acces the 12 
print(a1[-5])  # acces the 8
print(a1[4])    # acces the 4

# Acees the elements from the 2d array 
print(a2)
print(a2[-2,-2])  # acces the 7 
print(a2[-1,-3])  # acces the 10
print(a2[-3,-3])  # acces the 2
print(a2[-2,-4])  # acces the 5

# Acces the elements form the 3D array 
print(a3)
print(a3[-2,-1,-2])   # acces the 3
print(a3[-2,-2,-1])  # acces the 2
