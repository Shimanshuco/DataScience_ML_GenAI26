# try-except-else block
# The else block is executed if the try block does not raise an exception.
# The else block is optional and can be used to execute code that should only run if no exceptions were raised in the try block.

# Example 1:
try:
    with open('file.txt', 'r') as file:
        content = file.read()  # This will read the content of the file if it exists
except FileNotFoundError as e:
    print("An error occurred: File not found ! ", e)  # This will print the error message if the file is not found
else:
    print("File content: ", content)  # This will print the content of the file if it was successfully read

# Example 2: Division by zero error
try:
    result = 10 / 0  # This will raise a ZeroDivisionError
except ZeroDivisionError as e:
    print("An error occurred: Division by zero is not allowed ! ", e)  # This will print the error message if division by zero occurs
else:
    print("Result: ", result)  # This will print the result if no exceptions were raised in the try block

