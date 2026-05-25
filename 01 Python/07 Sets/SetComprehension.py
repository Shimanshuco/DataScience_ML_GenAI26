# Set Comprehension

# Set comprehension is a concise way to create sets in Python. It allows you to generate a new set by applying an expression to each item in an iterable, while optionally filtering items using a condition.

# Basic Syntax:
# {expression for item in iterable if condition}

# Example 1: Creating a set of squares from a list of numbers
numbers = [1, 2, 3, 4, 5]
squares = {x**2 for x in numbers}
print(squares)  # Output: {1, 4, 9, 16, 25}

# Example 2: Creating a set of even numbers from a list
even_numbers = {x for x in numbers if x % 2 == 0}
print(even_numbers)  # Output: {2, 4}

# Example 3: Creating a set of unique characters from a string
text = "hello world"
unique_characters = {char for char in text if char != ' '}
print(unique_characters)  # Output: {'h', 'e', 'l', 'o', 'w', 'r', 'd'}

# Example 4: Creating a set of the first 10 Fibonacci numbers
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

fib_set = {num for num in fibonacci(10)}
print(fib_set)  # Output: {0, 1, 2, 3, 5, 8, 13, 21, 34, 55}

