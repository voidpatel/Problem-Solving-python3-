# write and read from a file
# read 1 line at a time

# wrtie on a file
with open("mydata.txt", mode="w", encoding="utf-8") as myfile:
    
    myfile.write("Neel\nPatel\nNileshbhai")
 
# read individual lines from a file
with open("mydata.txt", encoding="utf-8") as myfile:
    
    line_num = 1
    
    # loop unitl line ends
    while True:
        
        data = myfile.readline()
        
        # if line doesn't return data, breal the loop
        if not data:
            break
        
        print("Line Number ", line_num, ":", data, end="")
        
        line_num += 1
        
