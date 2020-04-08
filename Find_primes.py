# Return a list of primes

# function to check a number is prime or not
def is_prime(num):
    
    # cycle from 2 till its limit
    for i in range(2, num):
        if (num % i) == 0:
            return False
    
    return True

# function to create a list that fetches prime numbers
def lists(max_num):
    
    prime_list = []
    
    
    for num1 in range(2, max_num):
        
        # call function 'isprime' and save in a list if number is prime
        if is_prime(num1) == True:
            prime_list.append(num1)
    
    return prime_list

max_num_check = int(input("Prime number upto: "))

# call function 'lists'
prime_list = lists(max_num_check)

# cycle and print each prime number in 'prime_list'
for prime in prime_list: 
    print(prime)
    
    
            