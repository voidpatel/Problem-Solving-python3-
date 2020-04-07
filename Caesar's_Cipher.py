# Receive a message and then encrypt it by shifting the
# characters by a requested amount to the right
# A becomes D, B becomes E for example
# Also decrypt the message back again
# using loops

samp_str = input("Enter a string: ")
key = int(input("Enter number of digits to shift: "))

secret_str = ""

# ENCRYPTION
# cycle through each character in sample string
for char in samp_str:
    
    # check if it a letter
    if char.isalpha():
        
        # assign the unicode to new string and add key to shift right
        char_code = ord(char)
        char_code += key
        
        # check if it a uppercase letter
        if char.isupper():
            
            # negate 26 if it exceeds number greater than unicode of letter 'Z'
            if char_code > ord("Z"):  
                char_code -= 26
            
            # add 26 if it exceeds number smaller than unicode of letter 'A'
            if char_code < ord("A"):              
                char_code += 26
                
        # repeat for lowercase letter
        else:   
            
            if char_code > ord("z"):
                char_code -= 26
                
            if char_code < ord("a"):
                char_code += 26
                
        # add charaters in secret string            
        secret_str += chr(char_code)
    
    # keep the character as it is of not a letter
    else:   
        secret_str += char

print("ORIGINAL STRING:  ", samp_str)
print("ENCRYPTED STRING: ", secret_str)

# DECRYPTION
# reverse the key to decrpt the message
key = -key

original_str = ""

# repeat the above code and relace the secret string to original string
for char in secret_str:
    
    if char.isalpha():
    
        char_code = ord(char)
        char_code += key
       
        if char.isupper():

            if char_code > ord("Z"):
            
                char_code -= 26
        
            if char_code < ord("A"):
            
                char_code += 26
        else:
             
            if char_code > ord("z"):
                    
                char_code -= 26
        
            if char_code < ord("a"):
            
                char_code += 26
                        
        original_str += chr(char_code)
    
    else:
        
        original_str += char
        
print("DECRYPTED STRING: ", original_str)

