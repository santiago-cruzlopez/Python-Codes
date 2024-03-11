def program_description():
    '''
    Standard science experiment to drop a ball and see how high it bounces.
    '''
    return None
#Allow the user to enter the numbers
print ("Enter the height and the number of bounces")
h = float(input("Enter the height: "))
b = int(input("Enter the number of bounces: "))
#Index
ix = 0.6
#Formula for the distance using the While and For Statement
while b == 1:
    #This part of the code calculate the distance for just one bounce
    d1 = h + (h*ix)
    print("The distance is: {} ft".format(d1))
    break
else:
    #Math formula for n bounces
    i = 0
    for i in range(b):
        dn = h + b*(h*ix) + (b-1)*(h*ix**b)
    print("The distance is: {} ft".format(dn))