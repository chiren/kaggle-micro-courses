"""
Function Name: average
Function Arguments: list
Return the average of a list of numbers


"""
# define your function here



# The following codes test your function
scores = [77, 82, 35, 67, 89, 43, 97]
expected = 70.0
avg = average(scores)

assert avg == expected, f"\nFailed: average({scores})\nYour answer is {avg} and expected answer is {expected}."

print("Correct!")