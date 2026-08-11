
# Methos based on the dictionary 


d = {
    1:100,
    2:200,
    3:300,
    4:400}

# Create the new key in the dictionary 

d[5] = 500
print(d)

# Update the 2 nd key in dictionary 
d[2] = "Aditya"
print(d)

# Delete the last key of the dictionary 
del d[5]
print(d)


# Traversing the dictionary 

d = {
    "name" : "Aditya",
    "age" : 21,
    "Clg" : "Universal College Of Engineering",
    "Tech" : "AIML"
    }

for i in d:
    print(d[i])