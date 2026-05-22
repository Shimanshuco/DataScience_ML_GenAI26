# Logical Operators
# Logical operators are used to combine conditional statements.
# The logical operators are:
# and
# or
# not

# and
x = 5
y = 10
print(x > 3 and y < 15)  # True
print(x > 3 and y > 15)  # False

# or
print(x > 3 or y < 15)  # True
print(x > 3 or y > 15)  # True
print(x > 10 or y > 15)  # False

# not
print(not(x > 3 and y < 15))  # False
print(not(x > 3 and y > 15))  # True
