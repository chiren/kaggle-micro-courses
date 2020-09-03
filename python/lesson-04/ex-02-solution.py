"""
Function Name: change_items
Function Arguments: list
After calling this function, the list's last 2 item will be changed to 0
This function does not return anything, so do not use return in the function
"""
# define your function here

def change_items(list):
    list[-1], list[-2] = 0, 0    



# The following codes test your function
list = [1, 2, 3, 4, 5, 6, 7]
original_list = list[:]
expected = [0, 0]
change_items(list)
changed = list[-2:]

assert changed == expected, f"\nFailed: changed_item({original_list})\nYour answer is {changed} and expected answer is {expected}."

print("Correct!")