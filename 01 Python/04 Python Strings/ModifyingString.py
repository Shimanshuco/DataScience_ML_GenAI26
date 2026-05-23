# Modifying Strings
# Strings in Python are immutable, which means you cannot change them after they have been created. 
# However, you can create new strings based on existing ones using various methods.

s= "Hello, World!"
# s[0] = 'h'  # This will raise an error because strings are immutable

# To modify a string, you can create a new string by concatenating parts of the original string with new content.
# Example: Changing the first character to lowercase
new_s = 'h' + s[1:]
print(new_s)  # Output: "hello, World!"

y = 'hello world'
del y
# print(y)  # This will raise an error because y has been deleted

z = 'hello world'
# del z[-1:-5:2] # Raise error
print(z)   # 'str' object does not support item deletion 