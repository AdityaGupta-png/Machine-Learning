

# Learning about the methods of the sets 

# Creation of an set
s = {1,2,3,4,5}

# 1 --> 1st method --> remove
s.remove(3)
print(s)

# 2 --> 2nd method --> clear 

s1 = {22,44,5.4,"Chandan",(99,11,66)}
print(s1.clear)

#  3 --> 3rd method --> add 

s2 = {55,77,88,22.111111,44,("Apple","Mango","Banana")}
s2.add("Aditya")
print(s2)


# Learing the Union,Intersection,Difference,symmetric difference 

s1 = {1,2,3,4,5,6,7}
s2 = {5,6,7,8,9,10,12}

# Union operation --> jo common hai usko ek bar likhenege 
s_union = s1.union(s2)
print(s_union)

# Intersection --> jo common hai only usko likhenge 
s_intersection = s1.intersection(s2)
print(s_intersection)

# Difference --> jo part s1 me hai s2 ka usko hata de s1 print mar denge 
s_difference = s1.difference(s2)
print(s_difference)

# Symmetric_differnce --> s1 and s2 me common part hai usko hata ke dono ko 
# merge karke set print kar denge 
s_symmetric_differnce = s1.symmetric_difference(s2)
print(s_symmetric_differnce)