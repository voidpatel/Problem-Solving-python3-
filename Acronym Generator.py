#Input string to get its acronym
rand_string = input("Enter a string: ")

#Empty string to save the acronym
acro_string = ""

#Convert all the letters to uppercase
cap_string = rand_string.upper()

#Split whole string to individual charaters and save in new list
first_list = cap_string.split()

#Loop through the list and save the first character in empty string
for i in first_list:
    acro_string += i[0]
   
print("Acronym of given string: ", acro_string)
         

     
