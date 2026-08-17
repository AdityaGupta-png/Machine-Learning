
# Importing the numpy
import numpy as np

# Doing the common operation of the numpy
a1 = np.arange(1,17).reshape(4,4)
a2 = np.linspace(-10,15,16).reshape(4,4)
print(a1)
print(a2)


# Performing the Scaler operations on the array 
print(a1+2)  # adding 2 to all element of the a1 
print(a2-1)   # substract 2 from the all element of the a2 
print(a1*3)  # multiply 2 in the a1 of all element 
print(a1/5)  # divide 5 from the all element of a1
print(a2 // 5)  # floor division
print(a1**99)


# Performing the vector operation 
print(a1 + a2)  # add matirx a1 and a2 and print those sum in the form of matrix 
print(a1 - a2)
print(a1 * a2)
print(a1 ** a2)

