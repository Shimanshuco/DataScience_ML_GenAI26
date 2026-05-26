# Functions : Functions are reusable blocks of code that perform a specific task. 
# They help in breaking down complex problems into smaller, manageable pieces, improving code readability and maintainability.
# Functions can take inputs (parameters) and return outputs (results).
    # Abstraction
    # Decomposition 

# Components of a Function:
    # 1. Function Definition: This is where you define the function using the 'def' keyword, followed by the function name and parentheses.
    # 2. Parameters: These are the inputs to the function, specified within the parentheses in the function definition. They allow you to pass data into the function.
    # 3. Function Body: This is the block of code that performs the task defined by the function. It is indented under the function definition.
    # 4. Optional Docstring: This is a string that describes what the function does. It is placed immediately after the function definition and is enclosed in triple quotes (""" """). It serves as documentation for the function, making it easier for others (or yourself in the future) to understand its purpose and usage.
    # 5. Return Statement: This is used to specify the output of the function. It allows the function to send back a result to the caller.

# Syntax of a Function:
# def function_name(parameters):
#     """Docstring: A brief description of what the function does."""
#     # Function body: Code that performs the task
#     return result  # Optional: Return a value to the caller

# Example of a Function:
def greet(name):
    """This function takes a name as input and returns a greeting message."""
    return f"Hello, {name}!"

# Calling the function
message = greet("Himanshu")
print(message)  # Output: Hello, Himanshu!

# Parameters vs Arguments:
# Parameters are the variables defined in the function definition that act as placeholders for the values that will be passed to the function when it is called. They are used to specify what kind of input the function expects.
# Arguments, on the other hand, are the actual values that are passed to the function when it is called. They are the real data that the function will process.

# .__doc__ : The __doc__ attribute of a function contains the docstring that describes what the function does. It can be accessed to understand the purpose and usage of the function.
print(greet.__doc__)  # Output: This function takes a name as input and returns

print(print.__doc__)  # Output: This function takes an arbitrary number of keyword arguments and prints them.


# If a function does not have a return statement, it will return None by default. 
# This means that if you call a function that does not explicitly return a value, it will return None.
# Example:
L = [1, 2, 3]
print(L.append(4))  # Output: None
print(L)  # Output: [1, 2, 3, 4]

# Function are first-class citizens in Python, which means they can be treated like any other object.
# They can be assigned to variables, passed as arguments to other functions, and returned from functions. 
# This allows for a high degree of flexibility and enables functional programming techniques in Python.

def square(x):
    return x * x

type(square)  # Output: <class 'function'>
id(square)  # Output: (some unique identifier for the function object)

# Reassigning the function to a variable
s = square
print(s(5))  # Output: 25 (calling the function through the new variable)

# Deleting the original function name
del square
# print(square(5))  # This will raise a NameError because 'square' is no longer defined, but 's' still holds a reference to the function object.
print(s(5))  # Output: 25 (the function can still be called through the variable 's')

# Storing functions in data structures:
def add(x, y):
    return x + y
def subtract(x, y):
    return x - y

operations = [add, subtract]
print(operations[0](10, 5))  # Output: 15 (calling the 'add' function)
print(operations[1](10, 5))  # Output: 5 (calling the 'subtract' function)

# Returning functions from other functions:
def outer():
    def inner():
        return "Hello from the inner function!"
    return inner

inner_function = outer()  # Calling the outer function returns the inner function
print(inner_function())  # Output: Hello from the inner function! (calling the returned inner function)

# Benefits of Functions:
# 1. Code Modularity
# 2. Code Readability
# 3. Code Reusability