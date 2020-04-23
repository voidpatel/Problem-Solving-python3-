# 1. Create a file named mydata2.txt and put data in it
# 2. how to open a file without with try to open the
# file in a try block
# 3. Catch the FileNotFoundError exception
# 4. In else print the file contents
# 5. In finally close the file
# 6. Try to open the nonexistent file mydata3.txt and
# test to see if you caught the exception

# create a file
with open("mydata2.txt", mode='w', encoding='UTF-8') as myFile:
    
    myFile.write("Neel\nPatel\nNilesh")
   


try:
    #open and read mydata2
    myFile = open("mydata2.txt", 'r')
    #try to read a non-existent file mydata3 
    #remove the comment below to check whether it handles the exception
    #myFile = open("mydata3.txt", 'r')


except FileNotFoundError as ex:

    print("File not Found")
    print(ex.args)

else:
    # print the file contents
    myFile = open("mydata2.txt", 'r')
    print(myFile.read())
    
finally:

    print("Required objectives are finished")
    myFile.close()

    
