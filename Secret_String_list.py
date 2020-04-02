samp_string = input('Enter a string: ')

sec_msg = [ord(c) for c in samp_string]

print(sec_msg)

org_msg = [chr(c) for c in sec_msg]

print(org_msg)

org_string = ""

for c in org_msg:
    
    org_string += c
    
print(org_string)
print("".join(org_msg))
