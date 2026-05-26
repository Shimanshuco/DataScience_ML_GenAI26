# Higher Order Functions (HOF)
# A higher-order function is a function that takes one or more functions as arguments and/or returns a function as its result.

# Example 1: A higher-order function that takes a function as an argument
def apply_function(func, value):
    return func(value)
# Using the apply_function with a lambda function
result = apply_function(lambda x: x * 2, 5)
print(result)  # Output: 10

# Example 2: A higher-order function that returns a function
def create_multiplier(n):
    return lambda x: x * n
# Using the create_multiplier to create a function that multiplies by 3
multiplier_by_3 = create_multiplier(3)
print(multiplier_by_3(10))  # Output: 30

# Example : 
def square(x):
    return x * x

def transform(f,L):
    output =[]
    for i in L:
        output.append(f(i))
    return output

print(transform(square,[1,2,3,4,5]))  # Output: [1, 4, 9, 16, 25]
