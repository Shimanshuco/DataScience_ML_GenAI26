# Reduced : Reduce the number of arguments of a function by using partial functions
# The functools module in Python provides a function called reduce() that allows you to apply a function of two arguments cumulatively to the items of a sequence, from left to right, to reduce the sequence to a single value.
# Syntax: functools.reduce(function, iterable[, initializer])

from functools import reduce

# Example 1: Using reduce to calculate the product of a list of numbers
numbers = [1, 2, 3, 4]
product = reduce(lambda x, y: x * y, numbers)
print(product)  # Output: 24

# Example 2: Using reduce to find the maximum number in a list
numbers = [3, 1, 4, 1, 5, 9]
max_number = reduce(lambda x, y: x if x > y else y, numbers)
print(max_number)  # Output: 9
