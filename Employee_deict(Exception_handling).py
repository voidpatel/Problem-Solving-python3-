# Creating employee dictionary with first and last name
# with exception handling

employees = []

while True:
    
    try:
        
        ans = input("Add customers (Yes/No): ")
        ans = ans.lower()
       
        if len(ans) != 1 and len(ans) != 3:
            print("Please enter y, yes, n or no")
            break
        
        elif ans == 'y' or ans == 'yes':
            fname, lname = input("Enter Employee Name : ").split()
            len(fname) > 0
            len(lname) > 0
            employees.append({'fname': fname, 'lname': lname})

        elif ans == 'n' or ans == 'no':
            break
    
    except ValueError: 
        print("Enter both first and last name")
        
# append values in employee list
for i in employees:
    print(i['fname'], i['lname'])
