

# Calculate the mean of the 

l = [10,11,12,13,14,15,16,17,18,19,20]
count = 0
sum = 0

for i in range(len(l)):
    count += 1
    sum += l[i]
    
mean = sum // count
print(mean)
