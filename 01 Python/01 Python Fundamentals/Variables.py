#Variables : A variable is a named location in memory that is used to store data. 
# In Python, you can create a variable by assigning a value to it using the assignment operator (=).

a = 10  # This creates a variable named 'a' and assigns it the value of 10
b = "Hello, World!"  # This creates a variable named 'b' and assigns it the value of "Hello, World!"
print(a," ",b)  # This will print the values of 'a' and 'b'

#Rules of Naming Variables :
    # Variable names must start with a letter (a-z, A-Z) or an underscore (_).
    # Variable names cannot start with a number.
    # Variable names can only contain alphanumeric characters (letters and numbers) and underscores.
    # Variable names are case-sensitive (e.g., 'myVariable' and 'myvariable' are different variables).
    # Variable names cannot be the same as Python reserved keywords (e.g., 'if', 'else', 'while', etc.).

# Static vs Dynamic Typing : 
    # Python is a dynamically typed language, which means that you do not need to declare the type of a variable when you create it. 
    # The type of a variable is determined at runtime based on the value assigned to it.
# c/c++/Java : int a = 10; // Static typing (Telling the compiler that 'a' is of type int)
# Python : a = 10 # Dynamic typing (The type of 'a' is determined at runtime based on the value assigned to it, which is an integer in this case)

# Static vs Dynamic Binding :
    # Static binding (also known as early binding) occurs when the method to be called is determined at compile time.
    # Dynamic binding (also known as late binding) occurs when the method to be called is determined at runtime.

a = 10  # 'a' is bound to the value 10
print(a)  # Output: 10
a = "Hello, World!"  # 'a' is now bound to the value "Hello, World!"
print(a)  # Output: Hello, World!

# Stylish declaration of variables :
    # In Python, you can declare multiple variables in a single line using a stylish syntax.
    # Example of variable declaration and assignment

x, y, z = 1, 2, 3  # This creates three variables 'x', 'y', and 'z' and assigns them the values 1, 2, and 3 respectively
print(x, y, z)  # Output: 1 2 3

a, b, c = "Python", "is", "awesome!"  # This creates three variables 'a', 'b', and 'c' and assigns them the values "Python", "is", and "awesome!" respectively
print(a, b, c)  # Output: Python is awesome!

a = b = c = 10  # This creates three variables 'a', 'b', and 'c' and assigns them all the value of 10
print(a, b, c)  # Output: 10 10 10