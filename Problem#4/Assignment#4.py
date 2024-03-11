#Expo Function
def expo(number, exponential):
    result = 1
    for i in range(exponential):
        result *= number
    return result

#Big-O Analysis Example
result = expo(10, 3) # Compute 10 raised to the power of 3
print(result) # Output: 1000