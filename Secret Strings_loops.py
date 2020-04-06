# receive a string(Uppercase, lowercas and spaces) and then hide its meaning by turning it into a string of unicodes
# then translate it from unicode back into its original meaning
# unicodes a-z: 65-90, A-Z: 97-122, space( ): 32

# input string from user
samp_string = input('Enter a string: ')
# empty string to store secret message(Unicode)
sec_msg = ""
# empty string to store original message
ORG_MSG = ""

# loop through each character in sample string
# subtract 23 from each unicode in order to convert three digit unicode to two digit 
# to iterate through loop two steps at a time
for char in samp_string:
   
   # check for spaces and substitute in string 
   if ord(char) == 32:
       sec_msg += chr(32)
   # substract 32 to detect zero in further code
       sec_msg += str(ord(char) - 32)

   # substract 23 and concatenate in string
   else:
       sec_msg += str(ord(char) - 23)
     
print("Secret Message:", sec_msg)

# loop secret string from index 0 till end of string and increment each time with 2
# add 23 in each unicode to convert them back in original unicodes
for i in range(0, len(sec_msg)-1, 2):
    
    # print space, if 0 detected in string
    if sec_msg[i] == 0:   
         print(chr(32))
         # use the i+1 and i+2 index if space detected
         for i in range(0, len(sec_msg)-1, 2):
             ORG_MSG += chr(int(sec_msg[i+1] + sec_msg[i+2]) + 23)
    
   # add the first and second index values with 23, convert that unicode to character and save it to empty string
    else:
        ORG_MSG += chr(int(sec_msg[i] + sec_msg[i+1]) + 23)
        
print("")
print("Original Message:", ORG_MSG)




    
            
           
      


    
