
# Learning the fancy indexing 
import numpy as np

# Fancy indexing in 2D arrays 
# Making the 2D array 
# Examle no. 1 
a1 = np.arange(1,13).reshape(4,3)
print(a1)
# Fancy indexing 
print(a1[[0,2,3]])

# Example number 2 
a2 = np.arange(1,25).reshape(6,4)
print(a2)
# Fancy indexing --> acces the 0,2,4,5 index 
print(a2[[0,2,4,5]])


# Example number 3 
a3 = np.arange(36).reshape(6,6)
print(a3)
# Acces the 1,3 ,5 columns
print(a3[0:,[1,3,5]])

# Fancy indexing in the 3D arrays 
# Creation of the 3D array

a4 = np.arange(1,28).reshape(3,3,3)
print(a4)
# Fancy indexing  --> in 3D arrays  
print(a4[0:2,[0,1]])
print(a4[0:3:2,0:,[0,2]])