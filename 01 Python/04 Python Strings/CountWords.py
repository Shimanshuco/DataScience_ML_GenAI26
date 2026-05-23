# Write a program to count the number of words in a string without split()

def count_words(string):
    count = 0
    in_word = False
    
    for char in string:
        if char.isspace():
            in_word = False
        elif not in_word:
            count += 1
            in_word = True
            
    return count

# Example usage
string = input("Enter a string: ")
num_words = count_words(string)
print("Number of words in the string:", num_words)
