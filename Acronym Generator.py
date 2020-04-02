rand_string = input("Enter a string: ")

acro_string = ""

cap_string = rand_string.upper()


first_list = cap_string.split()

for i in first_list:
    acro_string += i[0]
    
print("Afcronym of given string: ", acro_string)
         

     