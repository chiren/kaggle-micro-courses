"""
Use while loop to print out a multiplication table with n 

Function Name: print_multiplication
Function Arguments: n 

For example, if we call print_multiplication(7), 
the print out will be:
7 x 1 =  7
7 x 2 = 14
7 x 3 = 21
7 x 4 = 28
7 x 5 = 35
7 x 6 = 42
7 x 7 = 49
7 x 8 = 56
7 x 9 = 63
"""
def print_multiplication(n):
    i = 1  # need to initialize i, because i is used in the condition of while statement   
    while i < 10:
        print(f"{n} x {i} = {n*i:2}")
        i += 1  # Increment i by 1, without this statement, programe will never stop

n = 7

print_multiplication(7)