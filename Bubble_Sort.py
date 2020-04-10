import random

new_list = []

# get random numer upto 10 in new_list to sort
for i in range(5):
    new_list.append(random.randrange(1, 9))

# loop until i greater than 1
while i > 1:
    
    j = 0
    
    # loop until j less than i
    while j < i:
        
        # compare current and the following index
        if new_list[j] < new_list[j+1]:
            
            # swapping
            # move the current value in temporary variable
            temp = new_list[j]
            # move the following value in current index
            new_list[j] = new_list[j+1]
            # move the temporary calue in following index
            new_list[j+1] = temp
            
        j += 1
    
    i -= 1
    
print(" ".join(str(j) for j in new_list))
        
