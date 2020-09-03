"""
Function Name: select_last_3
Function Arguments: list
Return last 3 itmes from the list


"""
# define your function here




# The following codes test your function
scores = [77, 82, 35, 64, 89, 43, 97]
expected = [89, 43, 97]
selected = select_last_3(scores)

assert selected == expected, f"\nFailed: select_last_3({scores})\nYour answer is {selected} and expected answer is {expected}."

print("Correct!")