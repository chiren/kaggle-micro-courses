"""
Function Name: to_smash
Function Arguments: list 

Each item in the list represents the numbers of candies each person has.

Return the number of leftover candies that must be smashed after distributing
the candies evenly between all friends.


"""
# define your function here

def to_smash(list):
    return sum(list) % len(list)
    



# The following codes test your function
candies = [77, 82, 35, 64, 89, 43, 97]
expected = 4
smash = to_smash(candies)

assert smash == expected, f"\nFailed: to_smash({candies})\nYour answer is {smash} \nExpected answer is {expected}."

print("Correct!")