# Creating employee dictionary with first and last name
# with exception handling

employees = []

while True:
    
    try:
        
        ans = input("Add customers (Yes/No): ")
        # convert the input to lowercase
        ans = ans.lower()
       
        # only accept input with length 1 or 3
        if len(ans) != 1 and len(ans) != 3:
            print("Please enter y, yes, n or no")
            break
        
        # if yes, take input and check for value errors of both first and last name
        elif ans == 'y' or ans == 'yes':
            fname, lname = input("Enter Employee Name : ").split()
            len(fname) > 0
            len(lname) > 0
            # append data if inputs are correct
            employees.append({'fname': fname, 'lname': lname})
        
        # exit the function if input is no
        elif ans == 'n' or ans == 'no':
            break
            
    # print error message incase of value error
    except ValueError: 
        print("Enter both first and last name")
        
# append values in employee list
for i in employees:
    print(i['fname'], i['lname'])
