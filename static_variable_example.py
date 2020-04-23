# ---------- STATIC VARIABLES ----------
# Fields declared in a class, but outside of any method
# are static variables. There value is shared by every
# object of that class

class Dog:
    
    # initializing staic variable
    num_of_dogs = 0
    
    def __init__(self, name="unknown"):
        
        self.name = name
        
        Dog.num_of_dogs += 1
    
    @staticmethod
    def getDog():
        print("There are {} dogs".format(Dog.num_of_dogs))
    
def main():
    
    spot = Dog("Spot")
    
    Tony = Dog("Tony")
    
    spot.getDog()
    
    Tony.getDog()
    
main()
