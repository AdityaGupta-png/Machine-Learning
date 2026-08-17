# Importing the Numpy 
import numpy as np

# Creating of the numpy array 
a = np.array([1,2,3])
print(a)
print(type(a))

# Creating of 2D array 
a2 = np.array([[1,2,3],[4,5,6]])
print(a2)
print(type(a2))

# Creating of 3 array 
a3 = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
print(a3)
print(type(a3))

# Craeting of type of array 
a4 = np.array([1,2,3,4],dtype=float)
print(a4)

# Use of the arange method 
a5 = np.arange(1,13)
print(a5)

# Use of reshape method
a6 = np.arange(1,13).reshape(3,4)
print(a6)

a7 = np.arange(1,28).reshape(3,3,3)
print(a7)

# For creating the ones array 
a8 = np.ones((3,4))
print(a8)

# for creating the zero array 
a9 = np.zeros((4,5))
print(a9)

# use of the random method 
a10 = np.random.random((3,4))  # use to create the 3x4 matrix of number betwwen(0-1)
print(a10)

# use of linespace 
a11 = np.linspace(-20,20,20)
print(a11)

# creating of the identity matrix
i = np.identity(3)
print(i)
