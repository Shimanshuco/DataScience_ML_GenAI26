# Built-in Functions for Strings

# 1. len() - Returns the length of a string
my_string = "Hello, World!"
print(len(my_string))  # Output: 13

# 2. max() - Returns the maximum character in a string (based on ASCII value)
print(max(my_string))  # Output: 'r'

# 3. min() - Returns the minimum character in a string (based on ASCII value)
print(min(my_string))  # Output: ' ' (space)

# 4. str() - Converts an object to a string
number = 123
print(str(number))  # Output: '123'

# 5. sorted() - Returns a sorted list of characters in a string
print(sorted(my_string))  # Output: [' ', '!', ',', 'H', 'W', 'd', 'e', 'l', 'l', 'o', 'o', 'r']

# Capitalize/Title/Upper/Lower/Swapcase

# 6. capitalize() - Capitalizes the first character of a string
print(my_string.capitalize())  # Output: 'Hello, world!'

# 7. title() - Capitalizes the first character of each word in a string
print(my_string.title())  # Output: 'Hello, World!'

# 8. upper() - Converts all characters in a string to uppercase
print(my_string.upper())  # Output: 'HELLO, WORLD!'

# 9. lower() - Converts all characters in a string to lowercase
print(my_string.lower())  # Output: 'hello, world!'

# 10. swapcase() - Swaps the case of all characters in a string
print(my_string.swapcase())  # Output: 'hELLO, wORLD!'

# Count/Find/Index

# 11. count() - Returns the number of occurrences of a substring in a string
print(my_string.count('o'))  # Output: 2

# 12. find() - Returns the lowest index of the substring if found, otherwise -1
print(my_string.find('World'))  # Output: 7
print(my_string.find('Python'))  # Output: -1

# 13. index() - Returns the lowest index of the substring if found, otherwise raises a ValueError
print(my_string.index('World'))  # Output: 7
try:
    print(my_string.index('Python'))  # This will raise a ValueError
except ValueError as e:
    print(e)  # Output: substring not found

# endswith/startswith

# 14. endswith() - Returns True if the string ends with the specified suffix, otherwise False
print(my_string.endswith('!'))  # Output: True

# 15. startswith() - Returns True if the string starts with the specified prefix, otherwise False
print(my_string.startswith('Hello'))  # Output: True

# format
# 16. format() - Formats specified values in a string
name = "Himanshu"
age = 21
print("My name is {} and I am {} years old.".format(name, age))  

# isalnum/ isalpha/ isdigit/ isidentifier

# 17. isalnum() - Returns True if all characters in the string are alphanumeric, otherwise False
alphanumeric_string = "Hello123"
print(alphanumeric_string.isalnum())  # Output: True
non_alphanumeric_string = "Hello 123!"
print(non_alphanumeric_string.isalnum())  # Output: False

# 18. isalpha() - Returns True if all characters in the string are alphabetic, otherwise False
alphabetic_string = "Hello"
print(alphabetic_string.isalpha())  # Output: True
non_alphabetic_string = "Hello123"
print(non_alphabetic_string.isalpha())  # Output: False

# 19. isdigit() - Returns True if all characters in the string are digits, otherwise False
digit_string = "12345"
print(digit_string.isdigit())  # Output: True
non_digit_string = "12345a"
print(non_digit_string.isdigit())  # Output: False

# 20. isidentifier() - Returns True if the string is a valid identifier, otherwise False
identifier_string = "my_variable"
print(identifier_string.isidentifier())  # Output: True
non_identifier_string = "123variable"
print(non_identifier_string.isidentifier())  # Output: False

# join/split/strip

# 21. join() - Joins the elements of an iterable (e.g., list) into a string, separated by a specified separator
my_list = ['Hello', 'World']
separator = ' '
print(separator.join(my_list))  # Output: 'Hello World'

# 22. split() - Splits a string into a list of substrings based on a specified separator
my_string = "Hello, World!"
print(my_string.split(', '))  # Output: ['Hello', 'World!']

# 23. strip() - Removes leading and trailing whitespace from a string
my_string = "  Hello, World!  "
print(my_string.strip())  # Output: 'Hello, World!'

    # 32(a). lstrip() - Removes leading whitespace from a string
print(my_string.lstrip())  # Output: 'Hello, World!  '

    # 32(b). rstrip() - Removes trailing whitespace from a string
print(my_string.rstrip())  # Output: '  Hello, World!'

# replace
# 24. replace() - Replaces occurrences of a specified substring with another substring
my_string = "Hello, World!"
print(my_string.replace("World", "Python"))  # Output: 'Hello, Python!'

