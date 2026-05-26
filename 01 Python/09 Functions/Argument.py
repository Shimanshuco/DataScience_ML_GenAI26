# Arguments : Arguments are the actual values that are passed to a function when it is called. They correspond to the parameters defined in the function definition and provide the necessary input for the function to perform its task. Arguments can be of various types, such as numbers, strings, lists, or even other functions.
# When you call a function, you provide arguments that match the parameters defined in the function. The function then uses these arguments to execute its code and produce a result.

# Types of Arguments:
# 1. Positional Arguments: These are the most common type of arguments. They are passed to the function in the same order as the parameters are defined. The first argument corresponds to the first parameter, the second argument to the second parameter, and so on.
# 2. Keyword Arguments: These arguments are passed to the function using the parameter names as keywords. This allows you to specify which argument corresponds to which parameter, regardless of their order in the function definition.
# 3. Default Arguments: These are parameters that have a default value specified in the function definition. If an argument is not provided for a default parameter when the function is called, the default value will be used.
# 4. Variable-length Arguments: These allow you to pass an arbitrary number of arguments to a function. There are two types of variable-length arguments: *args for non-keyword variable-length arguments and **kwargs for keyword variable-length arguments.

# Example of Positional Arguments:
def add(a, b):
    """This function takes two numbers as input and returns their sum."""
    return a + b
result = add(5, 3)
print(result)  # Output: 8

# Example of Keyword Arguments:
def greet(name, greeting="Hello"):
    """This function takes a name and an optional greeting message."""
    return f"{greeting}, {name}!"
message = greet(name="Himanshu", greeting="Hi")
print(message)  # Output: Hi, Himanshu!
print(greet(name="Himanshu"))  # Output: Hello, Himanshu!


# Default Arguments Example:
def power(base, exponent=2):
    """This function takes a base and an optional exponent (default is 2) and returns the result of base raised to the power of exponent."""
    return base ** exponent

print(power(5))  # Output: 25 (5 raised to the power of 2)
print(power(5, 3))  # Output: 125 (5 raised to the power of 3)


# Example of Variable-length Arguments:

# *args allows you to pass a variable number of non-keyword arguments to a function. 
# It collects all the extra positional arguments into a tuple.
def sum_all(*args):
    """This function takes an arbitrary number of arguments and returns their sum."""
    return sum(args)

result = sum_all(1, 2, 3, 4, 5)
print(result)  # Output: 15


# **kwargs allows you to pass a variable number of keyword arguments to a function. 
# It collects all the extra keyword arguments into a dictionary.
def print_info(**kwargs):
    """This function takes an arbitrary number of keyword arguments and prints them."""
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Himanshu", age=21, city="Jaipur")
# Output:
# name: Himanshu
# age: 21
# city: Jaipur


# Note : 
    # 1. Order of arguments matter ( normal-> *args -> **kwargs )
    # 2. The word "args" and "kwargs" are just conventions. You can use any name you like, but it's best to stick to these conventions for readability and consistency.


# Function as a Argument:
def func_a():
    return "Hello from func_a!"

def func_b(func):
    print("Hello from func_b!")
    return func()

result = func_b(func_a)
print(result)  # Output: Hello from func_b! followed by Hello from func_a!