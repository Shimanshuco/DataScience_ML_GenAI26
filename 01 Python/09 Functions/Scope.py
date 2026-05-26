# Scope in Python refers to the region of a program where a variable is defined and can be accessed. 
# There are four types of scopes in Python:
    # 1. Local Scope: Variables defined within a function are in the local scope and can only be accessed within that function.
    # 2. Enclosing Scope: This is the scope of any enclosing functions. If a function is defined inside another function, the inner function has access to the variables of the outer function.
    # 3. Global Scope: Variables defined at the top level of a script or module are in the global scope and can be accessed anywhere in the code.
    # 4. Built-in Scope: This is the scope of built-in functions and variables provided by Python. These are always available in any part of the code.  

# The LEGB Rule: When you reference a variable, Python follows the LEGB rule to determine which variable to use. It checks in the following order:
    # 1. Local Scope (L)
    # 2. Enclosing Scope (E)
    # 3. Global Scope (G)
    # 4. Built-in Scope (B)

# Example of Scope:
def outer_function():
    x = "Hello from the outer function!"  # Enclosing Scope
    def inner_function():
        print(x)  # Accessing variable from the enclosing scope
    inner_function()

outer_function()  # Output: Hello from the outer function!

# Global Scope Example:
y = "Hello from the global scope!"  # Global Scope
def print_global():
    print(y)  # Accessing variable from the global scope
print_global()  # Output: Hello from the global scope!

# Built-in Scope Example:
print(len("Hello"))  # Output: 5 (len is a built-in function)


# Example : 
def f(x):
    x= x+1
    print('in f(X): x = ',x)
    return x

x= 3
z = f(x)
print('in main program scope x = ',x)
print('in main program scope z = ',z)
