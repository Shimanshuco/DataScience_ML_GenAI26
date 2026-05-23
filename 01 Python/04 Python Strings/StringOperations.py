# Operations on Strings
# 1. Arithmetic Operations
# 2. Relational Operations
# 3. Logical Operations
# 4. Loops on Strings
# 5. Membership Operations


# 1. Arithmetic Operations
str1 = "Hello"
str2 = "World"
# Concatenation
str3 = str1 + " " + str2
print(str3)  # Output: Hello World

# Repetition
str4 = str1 * 3
print(str4)  # Output: HelloHelloHello

# 2. Relational Operations
s = "Hello"
print(s == "Hello")  # Output: True
print(s != "World")  # Output: True
print(s > "Apple")  # Output: True (lexicographical comparison)
print(s < "Zebra")  # Output: True (lexicographical comparison)

# 3. Logical Operations
s1 = "Hello"
s2 = "World"

# Logical AND
print(s1 and s2)  # Output: World (both are non-empty strings)
# Logical OR
print(s1 or s2)  # Output: Hello (s1 is non-empty, so it is returned)
# Logical NOT
print(not s1)  # Output: False (s1 is non-empty, so it is considered True)


# 4. Loops on Strings
s = "Hello"
for i in s:
    print(i)

# 5. Membership Operations
s = "Hello"
print('H' in s)  # Output: True
print('h' in s)  # Output: False (case-sensitive)
print('lo' in s)  # Output: True
print('x' in s)  # Output: False

