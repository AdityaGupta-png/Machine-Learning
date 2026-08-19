
# Learing about the broadcasting 
import numpy as np

# # Same size of array
# a1 = np.arange(0,6).reshape(2,3)
# a2 = np.arange(6,12).reshape(2,3)
# print(a1)
# print(a2)
# print(a1 + a2)

# # Different size of array 
# a3 = np.arange(0,6).reshape(2,3)
# a4 = np.arange(3).reshape(1,3)
# print(a3)
# print(a4)
# print(a3 + a4)

# RULES FOR THE BROADCASTING 
"""
1 . both array ko same dimension me convert maro 
2 . sb dimension dono array ka same karo --> (1) mila to h strechted maro 
3 . (1) --> nh mila toh broadcasting perform nhi hoga 
"""

# Examle no 1 
a1 = np.arange(12).reshape(4,3)
a2 = np.arange(3)
print(a1)
print(a2)
print(a1 + a2)

# Example no 2 
# a = np.arange(12).reshape(3,4)
# b = np.arange(3)
# print(a + b)
# does not perform broadcasting 

# Exaple no 3 
a = np.arange(3).reshape(1,3)
b = np.arange(3).reshape(3,1)
print(a)
print(b)
print(a + b)

