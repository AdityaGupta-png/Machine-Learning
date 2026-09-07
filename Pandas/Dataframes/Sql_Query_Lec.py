
# Importing numpy and pandas 
import numpy as np
import pandas as pd 

# Making the dictionary 
data = {
    "Name" : ["Ravi","Amit","Sita","Rahul","Ankit","Riya","Sumit",
              "Neha","Karan","Pooja"],
    "Age" : [25,30,28,35,27,24,32,29,31,26],
    "City" : ["Patna","Delhi","Patna","Mumbai","Delhi","Patna",
              "Kolkata","Mumbai","Delhi","Patna"],
    "Department" : ["IT","HR","Finance","IT","HR","IT","Finance","HR",
                    "IT","Finance"],
    "Salary" : [50000,60000,45000,70000,40000,55000,48000,52000,
                65000,43000],
    "Email" : ["ravi@gmail.com","amit@yahoo.com","sita@gmail.com",
               "rahul@outlook.com","ankit@gmail.com","riya@gmail.com",
               "sumit@gmail.com","neha@gmail.com","karan@yahoo.com",
               "pooja@gmail.com"]
}

# Making the dataframe 
df = pd.DataFrame(data)
# print(df)

# print(df[df["Salary"] > 50000])
# Writing in form of the quey function 
# print(df.query("Salary > 50000"))
# print(df.query("Salary > 50000 and City == 'Patna'"))

# SOLVING THE QUESTIONS 

print(df)

# Question 1 
print(df.query("Salary > 50000"))

# Question 2 
print(df.query("City == 'Patna'"))

# Question 3 
print(df.query("Age < 30"))

# Question 4 
print(df.query("Department == 'IT'"))

# Question 5 
print(df.query("Salary <= 45000"))

# Question 6
print(df.query("Salary > 50000 and City == 'Patna'"))

# Question 7 
print(df.query("City == 'Delhi' or City == 'Mumbai'"))

#  Question 8 
print(df.query("Age > 25 and Age < 35"))

# Question 9 
print((df.query("Department != 'HR'")))

# Question 10 
print(df.query("Salary in [40000,50000,60000]"))

# Question 11 
print(df.query("City =='Patna' and Department == 'IT'"))

# Question 12 
print(df.query("Salary > 60000 and Age < 30"))

