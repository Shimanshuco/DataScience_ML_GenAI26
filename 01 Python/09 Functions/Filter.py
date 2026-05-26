# Filter : Filter is a built-in function in Python that allows you to filter elements from an iterable (like a list, tuple, etc.) based on a specified condition. 
# It takes two arguments: a function that defines the condition and an iterable to filter.
# Syntax: filter(function, iterable)

# Example 1: Using filter to get even numbers from a list
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = filter(lambda x: x % 2 == 0, numbers)
print(list(even_numbers))  # Output: [2, 4, 6]

# Example 2: Using filter to get fruits that start with the letter 'a'
fruits = ["apple", "banana", "cherry", "date", "fig", "grape"]
# Filter fruits that start with the letter 'a'
print(list(filter(lambda fruit: fruit.startswith('a'), fruits)))  # Output: ['apple']
