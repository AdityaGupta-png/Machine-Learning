
# # Prcatising the methods of the Numpy that i learned in the lecture 1 
# # Import the Numpy

import numpy as np

# # Creating the array 
#  1D array 
a1 = np.array([1,2,3,4,5])
print(a1)
print(type(a1))

# 2D array 
a2 = np.array([[1,2,3,4],[5,6,7,8]])
print(a2)
print(type(a2))

# 3d array 
a3 = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
print(a3)
print(type(a3))

# Using of the arange method
# 1D array 
a4 = np.arange(1,13)
print(a4)

# 2D array 
a5 = np.arange(1,13).reshape(3,4)
print(a5)

# 3d array 
a6 = np.arange(1,9).reshape(2,2,2)
print(a6)

# Creating the array of 1 
a7 = np.ones((3,4))
print(a7)

# Creating the array of 0
a8 = np.zeros((3,4))
print(a8)

# Creating array of random numbers beetween 1 and 0
a9 = np.random.random((3,4))
print(a9)

# Making the equals distance of array 
a10 = np.linspace(-1,1,20).reshape(4,5)
print(a10)

# Making the identity array 
a11 = np.identity(4)
print(a11)

# Arrays attribute 
a12 = np.arange(1,13)
a13 = np.arange(1,13).reshape(3,4)
a14 = np.arange(1,9).reshape(2,2,2)

# Find the dimension of the array 
print(np.ndim(a12))
print(np.ndim(a14))

# Find the shape of the array 
print(np.shape(a12))
print(np.shape(a14))

# find the size of the array 
print(np.size(a12))
print(np.size(a14))

# Doing the scaler multiplication
print(a12*2)
print(a12 + 20)
print(a14/22)

# Vector multiplication 

a15 = np.arange(1,13).reshape(3,4)
a16 = np.arange(12,24).reshape(4,3)
# Operations on the matrixs 
print(a15 + a16)
print(a15 * a16)
print(a15**a16)

print(a15.max())
print(a15.min())
print(a16.prod())
print(a16.sum())


# # # mean/ median/std/var 
print(a15.mean())
print(np.median(a16))
print(np.std(a15))
print(np.var(a16))

# # Dot product 
print(a15.dot(a16))

# # Trigonometry methods 
print(np.cos(a15))
print(np.tan(a16))

# # # Log and exponentil 
print(np.log(a15))
print(np.exp(a16))

# # Indexing and Slicing 
a1 = np.arange(1,13)
a2 = np.arange(1,13).reshape(3,4)
a3 = np.arange(1,28).reshape(3,3,3)
print(a1)
print(a2)
print(a3)

# # ------------------ INDEXING ------------------------
# Indexing on the 1D array 
print(a1)
print(a1[2])    # acces of the 3 
print(a1[-1])    # acees of the 12
print(a1[-3])    # acces of the 10

# # Indexing on the 2D array 
print(a2)
print(a2[-2,-3])   # acces of the 6
print(a2[-1,-3])   # acces of the 10
print(a2[-2,-4])    # acces of the 5

# # # Indexing on the 3D array 
print(a3)
print(a3[-2,-2,-2])  # acces of the 14
print(a3[-2,-3,-2])  # acces of the 11
print(a3[-3,-2,-2])   # acces of the 5

# #  --------------------- SLICING ------------------------
# # slicing in the 1D array 
print(a1)
print(a1[0:5])   # acces elemnt from 1 to 5
print(a1[-1:-4:-1])

# # Slicing in the 2D array 
print(a2)
print(a2[0:2,1:3])
print(a2[0::2,0:3:2])
print(a2[1:,1:3])

# # Slicing in the 3D array 
print(a3)
print(a3[-2])
print(a3[-2,0:2,0:2])
print(a3[0:2,1,0:2])


for i in np.nditer(a3):
    print(i)
    
    
# # Here i transpose use 
print(np.transpose(a2))

# # # revel --> used to make the array as 1d 
print(np.ravel(a3))  # --> convert the 3D to 1d 

# # Stacking 
a20 = np.arange(1,5).reshape(2,2)
a21 = np.arange(5,9).reshape(2,2)
print(a20)
print(a21)

print(np.hstack((a20,a21)))   # horizontal stacking 
print(np.vstack((a20,a21)))   # vertical stacking 

# # spliting is reverse of stacking 






