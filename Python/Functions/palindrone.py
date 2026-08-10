
# Check the string is palindrone or not 

def palindrone(str):
    
    i = 0
    j = len(str)-1
    
    while(i <= j):
        
        if str[i] != str[j]:
            return "Not Palindrone"
        i += 1
        j -= 1
        
    return "palindrone"

print(palindrone("nitin"))