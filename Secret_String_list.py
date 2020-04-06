# receive a string(Uppercase, lowercas and spaces) and then hide its meaning by turning it into a string of unicodes
# then translate it from unicode back into its original meaning using lists
# unicodes a-z: 65-90, A-Z: 97-122, space( ): 32

samp_string = input('Enter a string: ')

# create list containg unicodes of each character in sample string
sec_msg = [ord(c) for c in samp_string]

print("Secret Message:", sec_msg)

# create list containg character of each unicodes in sample secret message
org_msg = [chr(c) for c in sec_msg]

print("Original Message: ", end="")
# join the list characters in a string
print("".join(org_msg))
