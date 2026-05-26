# Map : Map is a built-in function in Python that applies a given function to each item of an iterable (like a list) and returns an iterator that yields the results.
# Syntax: map(function, iterable, ...)

# Example 1: Using map to square each number in a list
numbers = [1, 2, 3, 4, 5]
squared = map(lambda x: x * x, numbers)
print(list(squared))  # Output: [1, 4, 9, 16, 25]

# Label even/odd of a number in a list using map

L = [1,2,3,4]
list(map(lambda x : "Even" if x%2==0 else "Odd",L))  # Output: ['Odd', 'Even', 'Odd', 'Even']
