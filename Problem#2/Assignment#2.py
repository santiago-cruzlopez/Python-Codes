#Load file into program (1%)
#We are going to work with the assignment.txt file as an example
file = input("Enter the File Name with .txt at the end: ")
#Process file into list of lines and prompt user for input (2%)

with open(file,'r') as f:
    list_lines = f.readlines()
    nlines = len(list_lines)

while True:
    print(f"The {file} file has {nlines} lines.")
    user = input("Enter a line number or 'exit' to end the program: ")
    
    #Exit case (2%)
    str = 'exit'
    if user == str:
        print("The program has been successfully exited.")
        break
    
    #Error cases (3%)
    if not user.isdigit():
        print("Invalid Input.")
        continue
    integer = int(user)
    if integer < 1 or integer > nlines:
        print(f"Error Case: Enter a number between 1 and {nlines}.")
        continue
    
    #Output corresponding line (2%)
    print(f"Corresponding line {integer}")