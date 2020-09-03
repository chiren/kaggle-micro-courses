"""
Function Name: top_3
Function Arguments: list
Return the highest 3 numbers from the list: [highest_number, second_highest_number, third_highest_number]

** Hint **: use sorted() function

"""
# define your function here


# The following codes test your function
scores = [77, 82, 35, 64, 89, 43, 97]
expected = [97, 89, 82]
top3 = top_3(scores)

assert top3 == expected, f"\nFailed: top_3({scores})\nYour answer is {top3}\nExpected answer is {expected}."

print("Correct!")