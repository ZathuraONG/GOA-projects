#task 1
#   SyntaxError - this happens when python can't understand the code because the rules of the language are broken
#   ValueError - this occurs when a function receives an argument of the correct type but an inappropriate value
#   NameError - this happens when you try to use a variable or function name that hasn't been defined yet
#   TypeError - this error occurs when an operation or function is applied to an object of an inappropriate type
#   IndexError -  this error occurs in python when you try to access an index that is out of range for a list, tuple, or any other indexed collection
#task 2

try:
    print (x)
except NameError:
    x = 10
    print(x)

#task 3

my_list = [1, 2, 3]

try:
    print(my_list[5])
except IndexError:
    print(my_list[-1])

#task 4

try:
    number = int("hello")
except ValueError:
    print("cant convert the string to an integer.")
    number = 0

#task 5
# the try/except block in python is useful for handling errors and exceptions that might occur during code execution, allowing your program to continue running instead of crashing
