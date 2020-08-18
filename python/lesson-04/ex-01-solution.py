"""
Exercise 01:

Define a function named average which take a list as an argument called l

return the average of the list

ex:

numbers = [1, 2, 3, 4, 5, 6]

answer = average(numbers)

print("The average of :", numbers, "is", answer)
"""

# define your function here
def average(l):
	return sum(l)/len(l)

# Use your function here

numbers = [1, 2, 3, 4, 5, 6]

answer = average(numbers)

print("The average of :", numbers, "is", answer)
