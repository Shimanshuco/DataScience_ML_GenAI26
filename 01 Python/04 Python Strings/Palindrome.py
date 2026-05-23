# Write a program that can check whether a given string is palindrome or not.
# abba
# malayalam

def is_palindrome(string):
    newstr = s[::-1];
    if newstr == s:
        return True
    else:
        return False
    
# Example usage
s = input("Enter a string: ")
if is_palindrome(s):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")