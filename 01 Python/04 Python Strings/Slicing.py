# Slicing : Extracting a substring from a string
# Syntax : string[start:stop:step]

s = "Hello World"
# Extracting "Hello"
print(s[0:5])  # Hello
# Extracting "World"
print(s[6:11])  # World

# Negative Indexing
# Extracting "Hello"
print(s[-11:-6])  # Hello
# Extracting "World"
print(s[-5:])  # World

# Step
# Extracting "HloWrd"
print(s[0:11:2])  # HloWrd

# Extracting "el ol"
print(s[1:10:2])  # el ol

# Reversing a String
print(s[::-1])  # dlroW olleH


