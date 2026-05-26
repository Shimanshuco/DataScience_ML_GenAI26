# Lambda Functions in Python
# A lambda function is a small anonymous function that can take any number of arguments, but can only have one expression.
# Syntax: lambda arguments: expression

# Example 1: A simple lambda function that adds 10 to a given number
add_ten = lambda x: x + 10
print(add_ten(5))  # Output: 15

# Example 2: A lambda function that multiplies two numbers
multiply = lambda a, b: a * b
print(multiply(3, 4))  # Output: 12

# Difference between a regular function and a lambda function
# Regular function : Name 
# Lambda function : Anonymous (no name)
# Regular function : Returns a value using the return statement
# Lambda function : Returns the value of the expression automatically
# Regular function : Can contain multiple expressions
# Lambda function : Can only contain one expression
# Regular function : Can be called multiple times
# Lambda function : Typically used for short, simple functions that are not reused elsewhere in the code

# Check if string has 'a' using lambda function
check_a = lambda s: 'a' in s or 'A' in s
print(check_a("Hello"))  # Output: False
print(check_a("Apple"))  # Output: True