
# Practice all the methods 
# Import the numpy and matplotlib

import numpy as np
import matplotlib.pyplot as ply 

# Practice the Fancy indexing 
a = np.arange(1,13)
b = np.linspace(-5,5,36).reshape(6,6)
c = np.linspace(-10,10,27).reshape(3,3,3)

# # # FANCY INDEXing in the 1D array 
# # print(a)
# # print(a[[0,2,6]])
# # print(a[[6,4,2]])

# # Fancy indexing in the 2D array 
# print(b)
# print(b[[0,2]]) # acces the 0 and 2 rows 
# print(b[:,[0,2,3,4]])  # acces the 0 ,2,3 and 4 column

# # Fancy indexing in the 3D array 
# print(c)
# print(c[0:,[0,2]])
# print(c[0:3:2,0:3:2,[0,2]])

# Boolean Indexing 
# print(a)
# print(b)
# print(c)

# Doing operation in the 1D array 
# print(a)
# print(a[a % 2 == 0])
# print(a[(a> 5) & (a%2 == 0)])

# Doing operations in 2D array 
a2 = np.linspace(-100,100,500).reshape(50,10)
print(a2)
print(a2[a2 > 50])
print(a2[(a2 > 50) & (a2 % 2 == 0)])




