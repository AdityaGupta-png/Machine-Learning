# Importing the Numpy 
import numpy as np 

# Creating the numpy array 
a1 = np.arange(1,13).reshape(4,3)
a2 = np.random.random((4,3))
# print(a1)
# print(a2)

# # 4 methods of the numpy
# print(a1.max())  # used to find the maximum element form the a1 matrix
# print(a2.max())
# print(a1.min()) # used to find the minimum element from the a1 matrix 
# print(a1.sum())  # used to find the sum of all element form the a1 matrix 
# print(a2.sum())  # used to find the sum of all element from the a2 matrix 
# print(a1.prod())

# # More 4 methods of the numpy 
# print(a1.mean())  # find teb mean of the all element of the a1 
# print(a2.mean()) 
# print(np.median(a1)) # find the median
# print(np.median(a2))
# print(np.std(a1))  # find the standard deviation 
# print(np.std(a2))
# print(np.var(a1)) # find the variance 

# Trignometry functions 
# print(np.sin(a1))  # find the sin of the matrxi 
# print(np.cosh(a2))  # find the cosh of the matrix 
# print(np.tan(a1))  # find the tan of the matrix 

# Dot product 
a3 = np.arange(1,13).reshape(3,4)
a4 = np.random.random((4,3))
print(a3.dot(a4))
print(a4.dot(a3))

# log and exponential 
print(np.log(a1))
print(np.exp(a2))