"""
Use list comprehension to define a function which takes a list of scores 
and converts them into a list of grades 
Use the provided function score_to_grade() in your function to convert
each score to a grade


Function Name: grades_report
Function Arguments: scores which is a list of score
Return a list of grades
"""

def score_to_grade(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'

# define your function here


# The following codes test your function
scores = [77, 98, 82, 93, 35, 64]
expected = ['C', 'A', 'B', 'A', 'F', 'D']
result = grades_report(scores)

assert result == expected, f"\nFailed: \nYour answer is {result}\nExpected answer is {expected}."

print("Correct!")