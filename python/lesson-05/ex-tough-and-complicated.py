
"""
Define a function which takes a list of scores, and calculates the Grade Point Average(GPA) 
for the courses taken.  Assuming each course has the same weight.

Function Name: gpa
Function Arguments: scores which is a list of scores
Returns gpa which is a decimal number

** NOTE ** 

To convert score to point, we can use a list with ranges called score_ranges like: 
score_ranges = [range(60), range(60, 70), range(70, 80), range(80, 90), range(90, 100)]
We want to return grade point by:
1. expression: range's index value of score_ranges. 
    This should be easy: score_ranges.index(score_range)

2. context: we want to select the range from score_ranges
    This is a bit complicated. We need 2 'fors' for the context. One to iterate through score_ranges, 
    the other to iterate through scores
    Then we use if to decide which range to select and put into the expression
    The context should be:
    for score_range in score_ranges for score in scores if score in score_range
"""
# define your function here
def gpa(scores):
    score_ranges = [range(60), range(60, 70), range(70, 80), range(80, 90), range(90, 100)]
    return sum([ score_ranges.index(score_range) for score_range in score_ranges for score in scores if score in score_range])/len(scores)

# The following codes test your function
scores = [77, 98, 82, 93, 64]
expected = 2.8
result = gpa(scores)

print("Scores:", scores)
print("GPA:", result)

assert result == expected, f"\nFailed: \nYour answer is {result}\nExpected answer is {expected}."

print("Correct!")