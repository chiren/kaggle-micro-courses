"""
Use for loop to generate a list which contains only score >= 93 of the original scores
Function Name: grade_a_scores
Function Arguments: scores which is a list of score
Return a list of scores where each score is greater or equal to 93

** HINT **
use list method append to add a new item to a list
for example: listVar.append(item)
"""
# define your function here

    

# The following codes test your function
scores = [77, 98, 82, 93, 35, 64, 96, 89, 43, 97, 65]
expected = [98, 93, 96, 97]
a_scores = grade_a_scores(scores)

assert a_scores == expected, f"\nFailed: \nYour answer is {a_scores}\nExpected answer is {expected}."

print("Correct!")