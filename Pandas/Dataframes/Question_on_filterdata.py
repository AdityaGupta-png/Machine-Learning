

# Importing the numpy and pandas 
import numpy as np 
import pandas as pd 

# Making dataframe of the dictionary 
emp_data = {
    "Empid" : [101,102,103,104,105,106,107,108,109,110],
    "Name" : ["Amit","Ravi","Sita","Neha","Rahul","Priya","Ankit","Pooja","Vikas","Kiran"],
    "City" : ["Patna","Delhi","Mumbai","Kolkata","Chennai","Bangalore","Hyderabad","Pune","Jaipur","Lucknow"],
    "Dept" : ["HR","IT","Finance","IT","Sales","HR","IT","Finance","Sales","HR"],
    "Post" : ["Manager","Developer","Analyst","Developer","Excutive","Manager","Tester","Analyst","Executive","Manager"],
    "Sal" : [50000,60000,55000,62000,45000,52000,48000,53000,47000,51000]

}

# Making the dataframe of the dictionary 
df = pd.DataFrame(emp_data)
print(df)

# Answer of 1 st question 
print(df[df["Sal"] > 50000])

#Answer of 2 nd question 
print(df[df["Dept"] == "IT"])

# Answer of 3rd question 
print(df[df["City"] == "Patna"])

# 4 answer 
print(df[df["Sal"] < 48000])

# 5 answer 
print(df[df["Name"] == "Ravi"])

# 6 Answer 
print(df[(df["Sal"] > 45000) & (df["Sal"] < 55000)])

# 7 answer 
print(df[(df["Dept"] == "HR") & (df["Sal"] > 50000)])

# 8 answer 
print(df[(df["Dept"] == "IT") & (df["Dept"] == "Finance")])

# 9 answer 
print(df[(df["City"] == "Delhi") & (df["City"] == 'Mumbai')])

#10 answer 
print(df[df["Sal"].isin([45000,47000,60000])])
