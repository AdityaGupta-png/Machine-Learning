
# Importing the numpy and pandas 
import numpy as np
import pandas as pd 

# Making the list 
my_list = [100,200,300,400,500,600,700]
df = pd.Series(my_list)
print(df)

# Making the labels 
labels = ['1','2','3','4','5','6','7']
df1 = pd.Series(my_list,index = labels)
print(df1)

print(df.sum())   # find the sum of the all element of the series 
print(df1.mean())   # find the average of the all elemnt 
print(df1.median())
print(df1.mode())
print(df1.max())
print(df1.min())
print(df1.prod())
print(df1.count())



# Some others examples 

# Making the data 
s = [10,20,30,20,30,40,20,10]

# Making the labels 
l = ['a','b','c','d','e','f','g','h']
df2 = pd.Series(s,index = l)
print(df2)


# Some important methods 
print(df2.describe())     # its find the all mathematical related calculations 

print(df2.value_counts())     # used to find the how many times the values is countable

print(df2.unique())   # find the unique values and repersent it on the new list 

# Find the agg 
print(df2.agg(["mean","median","sum"]))



# Here i used the boolean indexing 

s2 = [10,20,30,40,50,60]
label_2 = ['a','b','c','d','e','f']

df3 = pd.Series(s2,index = label_2)
print(df3)

# 1 ka solution 
print(df3[df3 > 30] + df3*10//100)

# 2 ka solution
print(df3[df3 <40] -5)

# 3 ka solutions 
print(df3[df3 >= 50] *2)

# 4 ka solutons 
print(df3[df3<20] + 100)

# 5 ka solutions 
print(df3[df3 > 40] ** 2)

# 6 solution 
print(df3[df3 < 30] /2)

# 7 solutions 
print(df3[(df3>30) &  (df3 < 50)+ df3*10//100])

