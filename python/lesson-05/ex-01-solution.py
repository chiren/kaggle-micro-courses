"""
Use for loop to print out items of fruits 
Function Name: print_fruits
Function Arguments: fruits which is a list of fruits

"""
# define your function here

def print_fruits(fruits):
    for fruit in fruits:
        print(fruit)


fruits = ['apple', 'banana', 'cherry', 'pear', 'orange', 'pineapple', 'watermelon', 'starfruit']
print_fruits(fruits)