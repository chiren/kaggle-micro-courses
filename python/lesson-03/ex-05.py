"""
Exercise 05:

Define 2 functions. The first one named larger which takes 2 numbers,
and return the larger of the 2 numbers. The second one named smaller which
takes 2 numbers and return the smaller one.

Call your functions with 2 number, and print out the results

ex:

a, b = 4, -5

print("The larger of a and b is", larger(a, b))
print("The smaller of a and b is", smaller(a, b))
"""


# define your functions here
def larger(n1, n2):
    if n1 > n2:
        return n1
    return n2

# Call your functions and print out your results here

a, b = 4, -5

print("The larger of a and b is", larger(a, b))
#print("The smaller of a and b is", smaller(a, b))
