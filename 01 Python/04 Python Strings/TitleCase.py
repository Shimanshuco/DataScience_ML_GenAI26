# Write a python program to convert a string to title case without using the title()

def title_case(s):
    words = s.split()
    title_cased_words = []
    
    for word in words:
        if word:  # Check if the word is not empty
            title_cased_word = word[0].upper() + word[1:].lower() if len(word) > 1 else word.upper()
            title_cased_words.append(title_cased_word)
        else:
            title_cased_words.append(word)  # Preserve empty strings (if any)
    
    return ' '.join(title_cased_words)

# Example usage
input_string = "hello world! this is a test."
result = title_case(input_string)
print(result)  # Output: "Hello World! This Is A Test."
