"""
Define a function which takes a list of grades, and calculates the Grade Point Average(GPA) 
for the courses taken.  Assuming each course has the same weight.
Use the provided function grade_to_point() in your function to convert
each grade to a point

Function Name: gpa
Function Arguments: grades which is a list of grades
Returns gpa which is a decimal number
"""
def grade_to_point(grade):
    if grade == 'A':
        return 4
    elif grade == 'B':
        return 3
    elif grade == 'C':
        return 2
    elif grade == 'D':
        return 1
    else:
        return 0

# define your function here
def gpa(grades):
    return sum([grade_to_point(grade) for grade in grades])/len(grades)

# The following codes test your function
grades = ['C', 'A', 'B', 'A', 'D']
expected = 2.8
result = gpa(grades)

assert result == expected, f"\nFailed: \nYour answer is {result}\nExpected answer is {expected}."

print("Correct!")