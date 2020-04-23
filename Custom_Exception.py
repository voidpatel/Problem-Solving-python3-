# ---------- CUSTOM EXCEPTIONS ----------

# trigger an exception if the user enters a
# name that contains a number

# create a class that inherits from Exception class
class DogNameError(Exception):
    
    def __init__(self, *args, **kwargs):
        Exception.__init__(self, args, kwargs)
        
try:
    
    dogName = input("Enter dog name: ")
    
    # if any input character is digit, raise exception
    if any (char.isdigit() for char in dogName):
        # raise a custom exception
        raise DogNameError
        
    print("dog name is {}".format(dogName))

# create an exception
except DogNameError:
    
    print("Please enter only characters")
    