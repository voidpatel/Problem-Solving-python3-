samp_string = input('Enter a string: ')
sec_msg = ""
ORG_MSG = ""

for char in samp_string:
   
   if ord(char) == 32:
       sec_msg += chr(32)
       sec_msg += str(ord(char) - 32)

   else:
       sec_msg += str(ord(char) - 23)
     
print(sec_msg)
          
for i in range(0, len(sec_msg)-1, 2):
    
    if sec_msg[i] == 0:   
         print(chr(32))
         i += 1
         for i in range(0, len(sec_msg)-1, 2):
             ORG_MSG += chr(int(sec_msg[i] + sec_msg[i+1]) + 23)
    
    else:
        ORG_MSG += chr(int(sec_msg[i] + sec_msg[i+1]) + 23)
        
print("")
print(ORG_MSG)




    
            
           
      


    