
# Solve the question 

name = str(input("Enter your name : "))
age = int(input("Enter your age : "))

if age >= 18 :
    print(f"hello {name} your age is {age} and you valid for vote")
    
else : 
    ryear = 18-age
    print(f"hello {name} your age is {age} and you  not valid for vote")
    print(f"and you vote after the {ryear} years ")