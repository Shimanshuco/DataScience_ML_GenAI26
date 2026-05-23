# Write a program which can remove a particular character from a string.

def remove_character(string, char):
    # Create a new string to store the result
    result = ""
    
    # Iterate through each character in the input string
    for c in string:
        # If the current character is not the one we want to remove, add it to the result
        if c != char:
            result += c
            
    return result

# Example usage
string = input("Enter a string: ")
char = input("Enter the character to remove: ")
new_string = remove_character(string, char)
print("String after removing character:", new_string)