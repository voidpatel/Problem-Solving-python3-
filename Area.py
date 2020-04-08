# calculate area of different shapes (rectangle and circle)

import math

# func to show layout of code
def get_shape(new_shape):
    
    # convert the string to lowercase
    new_shape = new_shape.lower()
    
    # if rectangle call 'area_rectangle' function
    if new_shape == 'rectangle':
        area_rectangle()
        
    # or call 'area_cirlcle' func
    elif new_shape == 'circle':
        area_circle()
        
    # or handle by acknowledging user
    else:
        print("Enter rectangle or cicrcle")

# func to calculate area of recrtangle
def area_rectangle():
    
    length = float(input("Enter length: "))
    width = float(input("Enter width: "))
    
    print("Area for rectangle is {:.2f} ".format(length*width))

# func to calculate area of circle
def area_circle():
    
    radius = float(input("Enter radius: "))
   
    area = math.pi * math.pow(radius, 2)

    print('Area of circle is {:.2f}'.format(area))


def main():
    
    shape = input("Enter shape rectangle or circle: ")
    
    get_shape(shape)

main()
    
