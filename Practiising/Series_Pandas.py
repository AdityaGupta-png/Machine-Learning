# Practising all the things that i learn in the Series pandas 

# Import numpy and pandas 
import numpy as np 
import pandas as pd 

#  SERIES --> Means the 1 dimensional labeled array 

# Creating via list 
data = [10,20,30,40,50]
s1 = pd.Series(data)
# print(s1)

# Aceesing the element from the series framework 

# # Acesss the element from via Index 
# print(s1.iloc[0])     # Acess the 0 index element from the list 
# print(s1.iloc[3])     # Acess the 3 index element frm the list 

# Adding the Labels in the Series data types 
# print(s1)
# label = ['a','b','c','d','e']
# s2 = pd.Series(data,index = label)
# print(s2)

# # Acesss the element via labels 
# print(s2.loc['a'])            # Acesss the a  label element 
# print(s2.loc['c'])            # Acesss the c label element 

# # Acces the multiple element via index 
# print(s1.iloc[0:3])           # via slsicing 
# print(s1.iloc[[0,3]])               # via indexing panadas allow this type of indexing 

# Acesss the multiple elemnts via labels 
# print(s2.loc[['a','d']])


# Practising the some information methods 
# List store value inform of key and values 
my_list = {
    # List of all spartans members 
    "1" : "Aditya",
    "2" : "Chandan", 
    "3" : "Chandru",
    "4" : "Omkar",
    "5" : "Saurabh",
    "6" : "BABA",
    "7" : "Aryan",
    "8" : "Priyank",
    "9" : "Ankur",
    "10" : "Prakash"
}

# Convert into Series 
s3 = pd.Series(my_list)
# print(s3)

# # Practing the methods 
# print(s3.head(3))    # Staring ke 3 key and values lake de dega 
# print(s3.tail(4))      # ending ke 4 key and values lake de dega 
# print(s3.ndim)        # find the dimension of the series framewor
# print(s3.shape)       # series la shape batata  hai 
# print(s3.size)        # use to find the size of the series framework
# print(s3.index)       # print all the indexs
# print(s3.values)      # print all the values 


# Pratising the some mathematical functions 
my_data = [10,30,10,50,40,70,40,90,70,50]
labels = ['a','b','c','d','e','f','g','h','i','j']

s4 = pd.Series(my_data,index = labels)
# print(s4)

# Some mathematical operations 
# print(s4.min())  # find the minimum values from the list 
# print(s4.max())    # find the maximum value from the list
# print(s4.prod())    # find the product of all values 
# print(s4.count())   # how many element inside the list that find 
# print(s4.sum())      # find the sum of the all element of the list
# print(s4.mean())       # find the mean of the element
# print(s4.median())     # find the median of the element
# print(s4.mode())       # find the mode of the elemnt

# One methods used to find the overall 
# print(s4.describe())       # find overall mathematical operation

# # find the values count 
# print(s4.value_counts())      # which values repeat how many times 

# # find the unique values 
# print(s4.unique())           # which one is wnique that value print

# # agg methods 
# print(s4.agg(['sum','mean','max']))    # kisi bhi 3 ka values find find  ak ste hai 

# Practising the boolean indexing 

# Ques = [10,25,30,45,60,75,90,-5,100]
# s5 = pd.Series(Ques)
# print(s5)

# # Question 1 
# print(s5[s5>50])

# # Question 2 
# print(s5[(s5 > 20) & (s5 < 80)])

# # Question 3 
# print(s5[s5%2 != 0])

# # Question 4 
# print(s5[s5 < 0])

# # Question 5 
# print(s5[~(s5 > 0)])

# # Question 6 
# print(s5[s5 != 100])

# # Question 7 
# print(s5[s5.isin([10,30,100])])

# # Question 8 
# print(s5[(s5 < 20) | (s5 > 80)])

# # Question 9
# print(s5[s5 % 5 == 0])

# Practising the Conditional maths operation 

ques = [10,20,30,40,50,60]
s6 = pd.Series(ques)
print(s6)

# Qustion 1 
print(s6[s6 > 30]*(1.1))

# Question 2 
print(s6[s6<40]- 5)

# Question 3
print(s6[s6>=50]*2)

# Question 4 
print(s6[s6<= 20] + 100)

# Question 5 
print(s6[s6 > 40]**2)

# Question 6 
print(s6[s6<30]/2)

# Question 7 
print(s6[(s6>30) & (s6<50)*(1.1)])





