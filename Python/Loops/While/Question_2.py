

# Making the gausss number game 

import random

num = random.randint(1,10)

tries = 0


while True :
    
    guess = int(input("Guess the number : " ))
    
    if guess == num:
        tries += 1
        print(f"you are right you gussed the number is {tries} tries")
        break
    
    elif guess > num :
        print("Too much high")
        tries += 1
        
    elif guess < num :
        print("Too much low")
        tries += 1
        
    else :
        print("Number not found")
        tries += 1




