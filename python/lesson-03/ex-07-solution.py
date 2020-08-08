"""
Exercise 07:

Define a function named both_button_pressed which takes 2 argument b1, b2
and return True only when both buttons are True, otherwise return False

Call your both_button_pressed function and print out the results

ex:

a1, a2 = True, True
a3, a4 = True, False
a5, a6 = False, True
a7, a8 = False, False

print(a1, a2, "both pressed:", both_button_pressed(a1, a2))
print(a3, a4, "both pressed:", both_button_pressed(a3, a4))
print(a5, a6, "both pressed:", both_button_pressed(a5, a6))
print(a7, a8, "both pressed:", both_button_pressed(a7, a8))


"""


# define your function here
def both_button_pressed(b1, b2):
    return b1 and b2


# Call your function and print out your results here
a1, a2 = True, True
a3, a4 = True, False
a5, a6 = False, True
a7, a8 = False, False

print(a1, a2, "both pressed:", both_button_pressed(a1, a2))
print(a3, a4, "both pressed:", both_button_pressed(a3, a4))
print(a5, a6, "both pressed:", both_button_pressed(a5, a6))
print(a7, a8, "both pressed:", both_button_pressed(a7, a8))
