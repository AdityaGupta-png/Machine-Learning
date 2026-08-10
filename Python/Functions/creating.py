

# Creating of the function 
# def --> use of this keyword and then name of the function 

def hello():
    print("Hello, i am learning the function in python")
    
hello()


# at time of creation of function --> we add the parameter inside the braces 
# at time of call the function --> we pass the argument 

# There are 3 types of the argument 

#  1 --> Default argument 

def sum(a = 20,b =40):
    print(f"Sum of two numbers are : {a + b}")
    
sum()
    
#  2 --> keyword argument 

def info(name,age):
    print(f"My name is {name} and age is {age}")
    
info(age=21,name ="Aditya")

#  3 --> Positional  arguemnt 

def product(a,b):
    print(f"The product of two numbers are : {a*b}")
    
product(10,10)