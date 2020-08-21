"""
Function Name: is_member
Function Arguments: name, members
If name is in the members, return True and its index
Else return False and -1 


"""
# define your function here


# The following codes test your function
names = ['Ada', 'Bill', 'Chirs', 'Debby', 'Ed', 'Frank', 'Grace', 'Hannah', 'Iris', 'Jen', 'Keith' ]

# First Test
expected = True, 4
person = 'Ed'
answer = is_member(person, names)

assert answer == expected, f"\nFailed: is_member({person}, {names})\nYour answer is {answer}\nExpected answer is {expected}."

# Second Test
expected = False, -1
person = 'Linda'
answer = is_member(person, names)

assert answer == expected, f"\nFailed: is_member({person}, {names})\nYour answer is {answer}\nExpected answer is {expected}."

print("Correct!")