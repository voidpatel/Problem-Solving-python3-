#fill the cells in a multidimensional
# list with a multiplication table using values 1 - 9

# create a multidimensional 10X10 list
listTable = [[0] * 10 for i in range(10)]

# increment for each row
for i in range(1, 10):
    
    # increment for each item in row
    for j in range(1, 10):
        # assign values to cell
        listTable[i][j] = i * j

# repeat the same for the output 
for i in range(1, 10):

    for j in range(1, 10):
        print(listTable[i][j], end=", ")
    print()