# Python list can contain any kind of object in python

# Example : 
list = [1,2,print,type,input]
print(list)   # [1, 2, <built-in function print>, <class 'type'>, <built-in function input>]


# Use Cases :
#  
# 1. Dynamic Function Calling
# We can choose functions at runtime.
operations = [print, abs, str]

print(operations[1](-10))   # 10
print(operations[2](123))   # "123"
# Useful in:
    # calculators
    # menus
    # command systems
    # plugins

# 2. Callback Systems
# Functions can be passed and executed later.
def greet():
    print("Hello")

def bye():
    print("Goodbye")

actions = [greet, bye]

actions[0]()   # Hello
actions[1]()   # Goodbye

# Used heavily in:
    # GUI buttons
    # event systems
    # game engines
    # web frameworks

# 3. Replacing Large if-else Blocks
# Instead of:
choice = "add"

if choice == "add":
    print(2 + 3)
elif choice == "mul":
    print(2 * 3)

# Use a function map:
def add(a, b):
    return a + b

def mul(a, b):
    return a * b

operations = {
    "add": add,
    "mul": mul
}

print(operations["add"](2, 3))   # 5

# 4. Functional Programming
# Python supports higher-order programming.
numbers = [1, 2, 3, 4]

result = list(map(lambda x: x * 2, numbers))

print(result)   # [2, 4, 6, 8]
# map() receives a function object.

# 5. Plugin Architecture

# Applications can load functions dynamically.

# Example idea:

plugins = []
def plugin_a():
    print("Plugin A")
plugins.append(plugin_a)
plugins[0]()

# Used in:
    # VS Code extensions
    # Django middleware
    # Flask routes
    # testing frameworks



# Note : Functions are first-class objects in Python.
# In Python:
# print
# means:
# “the function object itself”

# while
# print()
# means:
# “call/execute the function”