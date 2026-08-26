
# Importing the numpy and pandas 
import numpy as np
import pandas as pd

# Creating arrays 
labels = ['a','b','c']
my_list = [10,20,30]
arr = np.array([10,20,30])
d = {1:10,2:20,3:30}

# here creating the pandas series 
print(pd.Series(my_list))

# Assign the custom labels 
print(pd.Series(my_list,index=labels))

# We cannot send the 2D arary in the series because series 
# is The 1D array 

# Making the series of the np array
print(pd.Series(arr))

# Making the series of the DICTIONARY 
# Dictonary --> have key and value pair we 
# do not have to assign the custom index 
# And also Series 1D array not assign its index 
print(pd.Series(d))
