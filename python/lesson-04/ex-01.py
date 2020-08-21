"""
Function Name: first_item
Function Arguments: list
Return: The first item of the list

Function Name: last_item
Function Arguments: list
Return: The last item of the list

"""
# define your function here



# The following codes test your functions
list = [1, 2, 3, 4, 5, 6, 7]
expect_first, expect_last = 1, 7
return_first = first_item(list)
return_last = last_item(list)

assert return_first == expect_first, f"\nFailed first_item({list}):\nYour answer is {return_first} and expected answer is {expect_first}."

assert return_last == expect_last, f"\nFailed last_item({list}):\nYour answer is {return_last} and expected answer is {expect_last}"

print("Correct!")