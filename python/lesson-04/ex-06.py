"""
Function Name: clone
Function Arguments: list
Return a new list cloned from the argument 


"""
# define your function here


# The following codes test your function
scores = [77, 82, 35, 64, 89, 43, 97]
expected = [77, 82, 35, 64, 89, 43, 97]
cloned = clone(scores)

assert cloned == expected, f"\nFailed: clone({scores})\nYour answer is {cloned} and expected answer is {expected}."

cloned[0] = 0

assert cloned != scores, f"\nFailed: cloned list has been modified.\nCloned: ${cloned}\nScores: ${scores}"

print("Correct!")