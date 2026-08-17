
# Import the numpy 
import numpy as np

""""
Rules for the Slicing 
example --> a2[row , column]
slice[0:3]  --> first index is include and second one is exclude 
"""

# Creating the array 
a1 = np.arange(1,13)
a2 = np.arange(1,13).reshape(4,3)
a3 = np.arange(27).reshape(3,3,3)
print(a1)
print(a2)
print(a3)

# Slicing in the 1D array 
print(a1[0:4])  # slice index from 0 to 3
print(a1[3:10])   # sclice index from the 3 to 9

# Slicing in the 2D array 
print(a2)
print(a2[0,:])
print(a2[0:2,1:])
print(a2[:,1])
print(a2[0::3,0::2])


# Slicing in the 3D array 
print(a3)
print(a3[-2])
print(a3[0::2])
print(a3[0,1,:])
print(a3[1,:,1])
print(a3[2,1:,1:])
print(a3[0::2,0,0::2])