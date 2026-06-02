# finally
# The finally block is used to execute code that must be executed regardless of whether an exception was raised or not. 
# It is typically used for cleanup actions, such as closing files or releasing resources.

# Example 1:
try:
    with open('file.txt', 'r') as file:
        content = file.read()  # This will read the content of the file if it exists    
except FileNotFoundError as e:
    print("An error occurred: File not found ! ", e)  # This will print the error message if the file is not found
finally:
    print("This will always be executed, regardless of whether an exception was raised or not.")  # This will always be executed

# try-except-else-finally block
try:
    f = open('file.txt', 'r')
    content = f.read()  # This will read the content of the file if it exists
except FileNotFoundError as e:
    print("An error occurred: File not found ! ", e)  # This will print the error message if the file is not found
else:
    print("File content: ", content)  # This will print the content of the file if it was successfully read
finally:
    f.buffer.close()  # This will close the file buffer, ensuring that resources are released
    f.close()  # This will close the file, ensuring that resources are released
    print("This will always be executed, regardless of whether an exception was raised or not.")  # This will always be executed

# So 'finally' is used by programmer to ensure that any type of database connection, file connection, network connection etc. is closed properly, even if an error occurs during the execution of the program.
