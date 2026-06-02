# try-except block
# The try block contains code that may raise an exception, while the except block contains code that handles the exception.
# try: try bolock is used to wrap the code that may raise an exception.
# except: except block is used to handle the exception that may occur in the try block.

# Example 1: 
with open('file.txt', 'r') as file:
    file.write("Hello World")  # This will raise an exception because the file is opened in read mode.

# Solution:
try:
    with open('file.txt', 'r') as file:
        file.write("Hello World")  # This will raise an exception because the file is opened in read mode.
except Exception as e:
    print("An error occurred: File not found ! ", e)  # This will print the error message instead of crashing the program
# e is a variable that holds the exception object, which contains information about the error that occurred.

# Example 2: Division by zero error
try:
    result = 10 / 0  # This will raise a ZeroDivisionError
except ZeroDivisionError as e:
    print("An error occurred: Division by zero is not allowed ! ", e)  # This will print the error message instead of crashing the program


