

# Creation of the sets 

s = {1,2,3,4,4,5}
print(s)

# Creation of empty set 
s1 = set()
print(type(s1))

# Charateristic of the sets 

#  1 --> Mutables -> sets are mutables 
s2 = {1,2,3,4,5}
# s2[3] = 10  --> because sets not have the index values 
# sets are support the add or remove 
print(s2)

# 2 --> Duplicate are not allowed 

# 3 --> unordered --> sets does not support the indexing 

#  4 --> heretrogenous --> means ,store only Immutables data types ex --> strings,numbers and tupels 

s3 = {1,2,3,4,"Aditya",(22,44,66,88.999)}

# TypeError: cannot use 'list' as a set element (unhashable type: 'list')
print(s3)

s = {1,2,3,4,8,2.3,"Hello"}

for i in s:
    print(i)