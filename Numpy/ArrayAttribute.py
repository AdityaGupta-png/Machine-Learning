# Import the numpy 
import numpy as np

# Creating the 1 dimnsional array 
a1 = np.arange(10)
a2 = np.arange(1,13,dtype=int).reshape(3,4)
a3 = np.arange(1,9,dtype=int).reshape(2,2,2)


# Find the dimension of the of the array 
print(a1.ndim)
print(a2.ndim)
print(a3.ndim)

# find the shape of the arrays 
print(a1.shape)
print(a2.shape)
print(a3.shape)

# Find the size of the array 
print(a1.size)
print(a2.size)
print(a3.size)

# find the data types 
print(a1.dtype)
print(a2.dtype)
print(a3.dtype)
