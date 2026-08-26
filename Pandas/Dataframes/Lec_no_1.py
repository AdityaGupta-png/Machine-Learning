
# Importing numpy and pandas 
import numpy as np
import pandas as pd

# Creating the dataframes  using dictionary 
labels = [0,1,2,3]
data = {
    "Name": ["Aditya","Chandan","Saurabh","Harsh"],
    "Age" : [21,21,22,21],
    "City" : ["Vasai-virar","Borivali","Naigaon","Bhayender"],
    "Salary" : [30000,40000,50000,60000]
}

# Making the Dataframes of the Data
df = pd.DataFrame(data,labels)
print(df)

# Creating the dataframes using the list 
data_List = [
    ["Anna",22,"New-York",40000],
    ["John",25,"America",50000],
    ["Peter",28,"Austrillia",60000],
    ["Linda",30,"Dubai",70000]
]

# If i want to give the columns name of the List 
column = ["Name","Age","Addresh","Salary"]

df2 = pd.DataFrame(data_List,columns=column)
print(df2)

# Selection of columns 
print(df)
print(df["Name"])  # selection of the single columns 
print(df[["Name","Salary"]])  # selection of multiple columns 

# Creation of the new column
print(df2)
df2["Designation"] = ["Doctor","Engin","Doctor","Engin"]
print(df2) 

# Removing of the columns 
print(df2.drop("Designation",axis =1))
# yeh only copy show karta hai ki remove ho hogaya hai 
# Original me se nhi remove hua hai 
print(df2)

# # You want to remove the permanetly 
df2.drop("Designation",axis=1,inplace= True)
print(df2)

# # Removing of the multiple columns age and salary
df2.drop(["Age","Salary"],axis=1,inplace=True)
print(df2)

"""
# SOME IMPORTANT CONCEPT 
axis = 1 --> COLUMN 
axis = 0 --> ROW 
"""

# Selecting of the rows 
print(df2)
print(df2.loc[0])  # information of the first row 
print(df2.loc[[0,2]])   # information of the multiple row 


# Selecting subset of rows and columns 
print(df2)
print(df2.loc[[0,1]][["Addresh","Salary"]])
print(df2.loc[[0,3]][["Name","Age"]]) 

# Conditional statement 

# I want only person age greater than 25
print(df2[df2["Age"] > 25])

# I wnat person ge greater than 25 and live in the dubai 
print(df2)
print(df2[(df2["Age"] > 25) & (df2["Addresh"] == "Dubai")])
