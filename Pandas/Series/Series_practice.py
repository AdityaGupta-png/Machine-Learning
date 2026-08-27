
# Importing numpy and pandas 
import numpy as np
import pandas as pd 

# Making the 

labels = ['a','b','c']
fruits = ["apple","mango","pineapple"]
my_list = [10,20,30,40]
data = [100,200,300,400]

# Making the series 
sd = pd.Series(labels)
print(sd)

# Making the 
sd2 = pd.Series(fruits,index=labels)
print(sd2)

# Making the series of the another data 
sd3 = pd.Series(data,index=my_list)
print(sd3)