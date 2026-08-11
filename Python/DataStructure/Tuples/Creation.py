
# Creation of the tuples 

m = (1,)
print(type(m))

t = (1,2,3,4,5,6)

# Charateristic of the tuples 
#  1 --> Immutable --> ones created cannot be changed going its value after going to index 

# t[0] = 7
print(t)

# 2 --> Duplicated value are allowed 
t1 = (1,2,3,4,5,6,6,7,10,10,12)
print(t1)

# 3 --> Ordered --> value store one after another 

# 4 --> heterogenous --> single tuples can store different data structure values 
t2 = (1,2,3.4,5.55,print("Aditya"),[1,2,3,55,44.333])
print(t2)

for i in range(len(t2)):
    print(t2[i])
    
    
# Uses the conecpt of the tuple unpacking 

a,b,c,d,e = (1,2,3,4,5)
print(a)
print(b)
print(c)
print(d)
print(e)
