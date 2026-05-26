# Nested Functions
# A nested function is a function defined inside another function. The inner function can access the variables and parameters of the outer function, allowing for encapsulation and modularity in code design.
# Nested functions are often used to create closures, which are functions that remember the environment in which they were created. 
# This can be useful for creating functions that have access to certain data without exposing it to the global scope.

def f():
    def g():
        print("Hello from the inner function g!")
    print("Hello from the outer function f!")

f()  # Output: Hello from the outer function f!

def f():
    def g():
        print("Hello from the inner function g!")
    g()  # Calling the inner function within the outer function
    print("Hello from the outer function f!")

f()
# Output:
# Hello from the inner function g!
# Hello from the outer function f!

# g()  # This will raise a NameError because g is not defined in the global scope.


# Example : 
def g(x):
    def h(x):
        x = x + 1
        print('in h(x): x = ', x)
    x = x + 1
    print('in g(x): x = ', x)
    h(x)
    return x

x = 3
z = g(x)
print('in main program scope x = ', x)
print('in main program scope z = ', z)
# Output:
# in g(x): x =  4
# in h(x): x =  5
# in main program scope x =  3
# in main program scope z =  4

