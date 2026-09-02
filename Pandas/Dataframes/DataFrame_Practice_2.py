
# Importing of numpy and pandas 
import numpy as np
import pandas as pd 

# There are 3 ways that we are create the Dataframe 
"""
1 --> Via Dictinoary
2 --> Via List 
3 --> Via Numpy nd aaray 
"""

# 1 -->  Creation of the dataframe via dictionary 
my_dict = {
    "Names" : ["Anand","Aditya","Aayush","Chandan"],
    "Education" : ["BSC","B.TECH","B.TECH","B.TECH"],
    "Tech" : ["Full Stack","ML Enginner","ML Enginner","DSA JAVA"],
    "Add" : ["VASAI","VASAI","BHOPAL","BORIVALI"]
}

# Making the data frame of the above dictionary 
df = pd.DataFrame(my_dict)
# print(df)

# 2 --> Creation of the dataframe via  Nested List 
my_list = [
    [101,"Aditya","ML Enginner","B.TECH"],
    [102,"Aayush","ML Enginner","B.TECH"],
    [103,"Chandan","DSA JAVA","B.TECH"],
    [104,"Anand","FULL Stack","BSC"],
    [105,"Harsh","Berojgar","B.TECH"]
]

# Making the dataframe of the 
df1 = pd.DataFrame(my_list)
# print(df1)

# Adding the column name to the nested list dataframe 
column = ["StudentId","Name","Tech","Education"]

df2 = pd.DataFrame(my_list,columns=column)
# print(df2)

# 3 --> Creation of dataframe by using the nd array 
my_data = np.array(
    [
    [101,"Aditya","ML Enginner","B.TECH"],
    [102,"Aayush","ML Enginner","B.TECH"],
    [103,"Chandan","DSA JAVA","B.TECH"],
    [104,"Anand","FULL Stack","BSC"],
    [105,"Harsh","Berojgar","B.TECH"]  
    ]
)

df3 = pd.DataFrame(my_data)
# print(df3)

# making the columns 
column = ["StudentId","Name","Tech","Education"]
df4 = pd.DataFrame(my_data,columns=column)
print(df4)

# Acces only the Name columns 
print(df4["Name"])
# Acces the multiples columns 

print(df4[["StudentId","Tech","Education"]])

# Acces the 0 2 and 4 rows 
print(df4.iloc[0:5:2])

# iloc --> se index pe operation hota hai toh (0,5) --> 0 include and 5 exclude 
#  loc --> se values pe operation hota hai toh (0,5)  ---> 0 include and 5 include 

print(df4.loc[0:4:2])