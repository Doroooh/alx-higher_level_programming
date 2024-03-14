#!/usr/bin/python3
if_name_ == "_main_":
# Importing the add function from add_0.py
from add_0 import add 
# Defining my two variables a and b
a = 1
b = 2

# Calling my function to get the expected return for 1 and 2 using the print function
print("{} + {} = {}".format(a, b, add(a, b)))
