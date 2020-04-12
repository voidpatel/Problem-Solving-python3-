# Fibonacci number
# EXAMPLE FIBONACCI OF 4 = 3

num = int(input("ENTER NUMBER: "))

def fib(num):
    # returning the same values for 0 and 1
    if num == 0:
        return 0
    
    elif num == 1:
        return 1    
    
    # calling function recursively 
    else:
        result = fib(num-1) + fib(num-2) 
        return result
    
print(fib(num))
    
        
    
    
    
