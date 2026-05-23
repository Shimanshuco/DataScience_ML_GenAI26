# Identity operators : Identity operators are used to compare the memory locations of two objects.
# The identity operators are "is" and "is not".
# The "is" operator returns True if both operands refer to the same object, and False otherwise.
# The "is not" operator returns True if both operands do not refer to the same object, and False otherwise.

# Example of identity operators
a = [1, 2, 3]
b = a
c = [1, 2, 3]
print(a is b)  # True, because a and b refer to the same object
print(a is c)  # False, because a and c refer to different objects
print(a == c)  # True, because a and c have the same content
print(a is not c)  # True, because a and c do not refer to the same object
# Example of identity operators with immutable objects
x = 10
y = 10
print(x is y)  
