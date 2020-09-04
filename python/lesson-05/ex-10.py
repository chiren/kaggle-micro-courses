"""
Define a function which takes a list of numbers, select all the positive numbers
and return a list consisted of the sqaure of the selected numbers.

Function Name: positive_sqares
Function Arguments: numbers
Returns a list of squares of the positive number

"""
# define your function here


# The following codes test your function
numbers = [7, -3, 5, 2, -4, 3]
expected = [49, 25, 4, 9]
result = positive_squares(numbers)

assert result == expected, f"\nFailed: \nYour answer is {result}\nExpected answer is {expected}."

print("Correct!")