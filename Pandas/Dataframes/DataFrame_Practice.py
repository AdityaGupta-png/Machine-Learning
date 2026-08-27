
# Importing the numpy and pandas 
import numpy as np 
import pandas as pd 

# making the DataFrames thorugh the Dictonary 
my_data = {
    "Name":["Aditya","Chandan","Saurabh","Chandru","Omakr","Harsh","Avachut"],
    "Age":[21,21,22,21,22,21,21],
    "City":["Vasai","Borivali","Naigaon","Kashi-Mira","Kashi-Mira","Bhayendra","Chinchoti"],
    "Branch":["AIML","COMPS","COMPS","CIVIL","AIML","AIML","AIML"]
}

df = pd.DataFrame(my_data)
# print(df)

# Making the dataframe from the list 
my_list = [
    ["Aryan",22,"MALAD","AIML"],
    ["Priyank",22,"EVERSHINE","IT"],
    ["Tanvir",23,"NAIGOAN","SKILLTECH"],
    ["Krishna",20,"Mira road","SKILLTECH"]
]

df2 = pd.DataFrame(my_list)
# print(df2)

# Adding column to the 
columns = ["Names","Age","City","Study"]
df2 = pd.DataFrame(my_list,columns=columns)
# print(df2)

# Selection of the columns 
# print(df2[["Names"]])

# Selection of the multiple coulmns 
# print(df2[["Names","City"]])

# Adding the new columns 
print(df)
df["Smoker"] = ["Yes","YES","Yes","Yes","Yes","Yes","No"]
df["Droper"] = ["NO","YES","YES","NO","NO","YES","2ND DROPPER"]
# print(df)

# Here we have to remove the columns 
print(df)
print(df.drop("Droper",axis=1))  # here it is remove after making the copy not form original
print(df)

# here we remove from the original one 
print(df.drop("Smoker",axis=1,inplace=True))
print(df)

# deleting the multiple columns 
print(df.drop(["Branch","Droper"],axis=1,inplace= True))
print(df)

# 


