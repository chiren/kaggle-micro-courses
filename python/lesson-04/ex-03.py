"""
Function Name: select_mary
Function Arguments: list
Return Mary from the list

The list passed to your function will be:
[
    ["John", "Joan"], 
    ["Adam", "Ada"],
    ["Mike", "Mary"],
    ["Tim", "Tina"],
    ["Chris", "Christina"],
]

"""
# define your function here




# The following codes test your function
list = [
    ["John", "Joan"], 
    ["Adam", "Ada"],
    ["Mike", "Mary"],
    ["Tim", "Tina"],
    ["Chris", "Christina"],
]
expected = "Mary"
selected = select_mary(list)

assert selected == expected, f"\nFailed: select_mary({list})\nYour answer is {selected} and expected answer is {expected}."

print("Correct!")