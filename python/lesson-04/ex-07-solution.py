"""
Function Name: select_third
Function Arguments: list
Return the third item of the list, if the list has no third item return None
"""
# define your function here
def select_third(list):
    if len(list) >= 3:
        return list[2]




# The following codes test your function
# First test, for length of list >= 3
list = [1, 2, 3, 4, 5, 6, 7]
expected = 3
selected = select_third(list)

assert selected == expected, f"\nFailed: select_third({list})\nYour answer is {selected} and expected answer is {expected}."

# Second Test, for length of list < 3
list = [1, 2]
expected = None
selected = select_third(list)

assert selected == expected, f"\nFailed: select_third({list})\nYour answer is {selected} and expected answer is {expected}."

print("Correct!")