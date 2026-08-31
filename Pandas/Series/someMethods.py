# Importing numpy and pandas 
import numpy as np
import pandas as pd 

# Making the series 
s = [10,20,30,40,50,60]

# Making the labels 
labels = ['a','b','c','d','e','f']

# Printing with the 0 based indexing 
df = pd.Series(s)
print(df)

# Printing with the labels 
df1 = pd.Series(s,index = labels)
print(df1)
print(df.dtype)

# printing only the values 
print(df.iloc[[0,3,5]])

# Accesing the values using the Labels indexing 
print(df1.loc[['a','c','e']])

# Methods of the series 

print(df1.head(3))    # acces the 3 numbers from the top 
print(df1.tail(2))    # acces the 2 numbers from the bottom
print(df1.ndim)     # dimension bata hai 1 D hai 
print(df1.shape)       # give the shape of the datastrure 
print(df1.size)         # size batata hai array kla 
print(df1.index)   # print the index values 
print(df1.values)         # print the values 
