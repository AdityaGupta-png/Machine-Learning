
# Importing numpy and pandas 
import numpy as np 
import pandas as pd

# Making the data set of dictinoary 
data = {
    "Name" : ["Ravi","Amit","Sita","Rahul","Ankit","Riya",
              "Sumit"],
    "City" : ["Patna","Delhi","Patna","Mumbai","Delhi","Patna",
              "Kolkata"],
    "Email" : ["ravi@gmail.com","amit@yahoo.com","sita@gmail.com",
               "rahul@yahoo.com","ankit@gmail.com","riya@yahoo.com",
               "sumit@gmail.com"]
}

# Making dataframe 
df = pd.DataFrame(data)
# print(df)

# # Jiska name R start se start ho raha hai uska record  print maro 
# print(df[df["Name"].str.startswith("R")])

# # name end with l 
# print(df[df["Name"].str.endswith("l")])

# # Contains with 
# print(df[df["Name"].str.contains("a")])

# # End with gmail.com 
# print(df[df["Email"].str.endswith("gmail.com")])

# # city patna
# print(df[df["City"] == 'Patna'])

# Doing QUESTIONS 

# 1 --> Questions 
print(pd)
print(df[df["Name"] == "Ravi"])

# 2 --> Question 
print(df[df["City"] == "Patna"])

# 3 --> Question 
print(df[df["Name"].str.contains("a")])

#4 --> Question 
print(df[df["Name"].str.startswith("R")])

# 5 --> Question 
print(df[df["Name"].str.endswith("t")])

# 6 --> Question 
print(df[df["Email"].str.endswith("gmail.com")])

# 7 --> Question 
print(df[(df["Name"].str.contains("i")) & (df["City"] == "Patna")])

# 8 --> Question 
print(df[(df["Name"].str.contains("a")) | (df["City"]) == "Delhi"])

# 9 Question 
print(df[df["Email"].str.endswith("yahoo.com")])

#10 --> Question 
print(df[df["Name"].str.lower().str.contains("ra")])

# 11 --> Question 
print(df[~(df['Name'].str.contains("a"))])

# 12 --> Question 
print(df[df["Name"].str.len() == 5])

# 13 --> Question 
print(df[df["City"].str.startswith("A")])