# Find the length of a string without using the built-in len() function

def string_len(s):
    count = 0
    for char in s:
        count += 1
    return count

my_string = "Hello, World!"
print(string_len(my_string))  # Output: 13
