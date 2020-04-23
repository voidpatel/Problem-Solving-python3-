# Static methods allow access without the need to initialize
# a class. They should be used as utility methods, or when
# a method is needed, but it doesn't make sense for the real
# world object to be able to perform a task

class Sum:
    
    # initializing static method
    @staticmethod
    def add(*args):
        
        total = 0
        
        for i in args:
            total += i
            
        return total
    
def main():
    
    # call static method
    print("sum:", Sum.add(4, 2, 3, 1))
    
main()
