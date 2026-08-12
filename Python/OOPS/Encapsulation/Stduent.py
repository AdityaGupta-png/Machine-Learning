
# Encapsulation --> means taking about the Data security 

# Making the student class 
class Student:
    
    # Constructor 
    # Making the private instance attribute 
    def __init__(self,name,age,rollNo,phoneNo):
        self.__name = name
        self.__age = age
        self.__rollNo = rollNo
        self.__phoneNo = phoneNo
        
    # Methods also making protected 
    
    def _showInfo(self):
        print(f"Name of the student is {self.__name}")
        
    # Making the getter and setter of the attributes 
    
    # For the name 
    def get_name(self):
        return self.__name
    
    def set_name(self,new_name):
        if(len(new_name) > 0):
            self.__name = new_name
        else:
            print('Name could not empty')
            
    # for the age 
    def get_age(self):
        return self.__age
    
    def set_age(self,new_age):
        
        if(new_age > 0):
            self.__age = new_age
        else:
            print("Age never is negative ")
    
    # for the roll no
    def get_rollNo(self):
        return self.__rollNo
    
    def set_rollNo(self,new_rollNo):
        if(new_rollNo > 0):
            self.__rollNo = new_rollNo
        else:
            print("Never be negative")
            
    # for the phoneNo 
    def get_phoneNo(self):
        return self.__phoneNo
    
    def set_phoneNo(self,new_phoneNo):
        if(new_phoneNo == 10):
            self.__phoneNo = new_phoneNo
        else:
            print("Please enter valid mobile number")
            
    


# making the object of the class 
S1 = Student("Aditya",21,34,"xxxxxxxxxx")
S1._showInfo()
print(S1.get_name())
S1.set_name("Aditi")
print(S1.get_name())
S1._showInfo()
