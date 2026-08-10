

# Find the largest element in the list 

l1 = [11,33,55,-22,101,66,-22,22,-55,77,-66,99]

# firnding the largest number 
def findLargestNumber(l1):
    
    max_no = l1[0]
    max_index = 0
    
    
    # apply for loop to treaverse the whole list 
    for i in range(1,len(l1)):
        
        # Comdition 
        if(l1[i] > max_no):
            max_no = l1[i]
            max_index = i
            
    return f"The largest number is {max_no} and its index is {max_index}"
    
print(findLargestNumber(l1))
            

        