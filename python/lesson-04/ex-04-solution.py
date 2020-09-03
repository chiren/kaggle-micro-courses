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

def select_mary(list):
    return list[2][1]
    



# The following codes test your function
names = [
    ["John", "Joan"], 
    ["Adam", "Ada"],
    ["Mike", "Mary"],
    ["Tim", "Tina"],
    ["Chris", "Christina"],
]
expected = "Mary"
selected = select_mary(names)

assert selected == expected, f"\nFailed: select_mary({names})\nYour answer is {selected} and expected answer is {expected}."

print("Correct!")