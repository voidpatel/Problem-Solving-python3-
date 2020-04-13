# Fibonacci series
# 1, 1, 2, 3, 5, 8, 13

num = int(input("ENTER NUMBER: "))

def fib(num):
    
    # returning the same values for 0 and 1
    if num == 0:
        return 0
    
    elif num == 1:   
        return 1  
    
    else:
        # calling function recursively 
        result = fib(num-2) + fib(num-1)
        return result
    
i = 1

# loop unitl user provided number
while i < num:
    
    # save each result in new string
    num_fib = fib(i)
    
    print(num_fib)
    
    i += 1
    
print("All done")



    
        
    
    
    