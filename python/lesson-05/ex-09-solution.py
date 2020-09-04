"""
Define a function which takes a list of grades, and calculates the Grade Point Average(GPA) 
for the courses taken.  Assuming each course has the same weight.

Function Name: gpa
Function Arguments: grades which is a list of grades
Returns gpa which is a decimal number

** NOTE ** 
This time there is no grade_to_point function.
Remember in lesson 4, we learn a list method index(item) which
return the index value of item found in the list.

To convert grade to point, we can use a list with items like: ['F', 'D', 'C', 'B', 'A'] 
and use its index method to get index value as the grade's point.
For example: to find out B's point, B's index value in the ['F', 'D', 'C', 'B', 'A']
is 3 which happens to be grade B's point
"""
# define your function here
def gpa(grades):
    return sum([ ['F', 'D', 'C', 'B', 'A'].index(grade) for grade in grades])/len(grades)

# The following codes test your function
grades = ['C', 'A', 'B', 'A', 'D']
expected = 2.8
result = gpa(grades)

assert result == expected, f"\nFailed: \nYour answer is {result}\nExpected answer is {expected}."

print("Correct!")