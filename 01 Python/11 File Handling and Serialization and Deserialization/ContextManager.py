# Context Manager (with)
# Context manager is a Python construct that allows you to manage resources efficiently.
# It ensures that resources are properly acquired and released, even in the case of exceptions. The most common use of context managers is with file handling, where you want to ensure that files are closed after they are used.
# The with statement is used to wrap the execution of a block of code with methods defined by a context manager. 
# The syntax is as follows:
# with expression as variable:
#     # code block

# Using context manager to read a file
with open('sample.txt','r') as f: # This will automatically close the file after the block of code is executed.
    s = f.read()
    print(s)

# f.read() # This will raise an error because the file is already closed after the with block.

