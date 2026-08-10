

# Find the second largest element 

l = [12,16,13,19,17]

# Function for the check the largest number and second largest

def secondLargest(l):
    
    largest = l[0]
    sec_largest = l[0]
    
    for i in l :
        
        if i > largest:
            sec_largest = largest
            largest = i
            
        elif i > sec_largest:
            sec_largest = i
            
    print(largest,sec_largest)
    
    
secondLargest(l)
            
