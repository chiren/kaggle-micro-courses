"""
We have a list of party attendees arranged in the order of their arrival.  
The person arrived first is at index 0 of the list. The second is at index 1, and so on.
We want to find out whether a person arrived earlier than at least half of the attendees, but
not the earliest one.

Function Name: early_but_not_lonely
Function Arguments: arrivals, name
Return True if a person arrived earlier than half of the attendees, but not the earliest.
Else return False

"""
# define your function here


# The following codes test your function
names = ['Ada', 'Bill', 'Chris', 'Debby', 'Ed', 'Frank', 'Grace', 'Hannah', 'Iris', 'Jen', 'Keith' ]

# First Test
person = 'Ada'
answer = early_but_not_lonely(names, person)
expected = False
assert answer == expected, f"\nFailed: early_but_ont_lonely({names}, {person})\nYour answer is {answer}\nExpected answer is {expected}."

# Second Test
person = 'Wonda'
answer = early_but_not_lonely(names, person)
expected = False
assert answer == expected, f"\nFailed: early_but_ont_lonely({names}, {person})\nYour answer is {answer}\nExpected answer is {expected}."

# Third Test
person = 'Grace'
answer = early_but_not_lonely(names, person)
expected = False
assert answer == expected, f"\nFailed: early_but_ont_lonely({names}, {person})\nYour answer is {answer}\nExpected answer is {expected}."

# Fourth Test
person = 'Frank'
answer = early_but_not_lonely(names, person)
expected = True
assert answer == expected, f"\nFailed: early_but_ont_lonely({names}, {person})\nYour answer is {answer}\nExpected answer is {expected}."

# Fifth Test
person = 'Chris'
answer = early_but_not_lonely(names, person)
expected = True
assert answer == expected, f"\nFailed: early_but_ont_lonely({names}, {person})\nYour answer is {answer}\nExpected answer is {expected}."

print("Correct!")