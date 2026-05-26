# Dictionary is a collection of key-value pairs. It is an unordered, mutable, and indexed data structure in Python. Dictionaries are defined using curly braces {} and consist of key-value pairs separated by a colon (:). Each key must be unique, and the values can be of any data type.
# Keys can't be duplicated and must be immutable 


# Creating a dictionary
# 1. Empty dictionary
my_dict = {}
print(my_dict)

# 2. Dictionary with some key-value pairs
my_dict = {
    "name": "Himanshu",
    "age": 20,
    "city": "Jaipur"
}

# 3. With mixed keys
my_dict = {
    "name": "Himanshu",
    1: [1, 2, 3],
    (1, 2): "Tuple as key"
}
print(my_dict)

# 4. 2D Dictionary
my_dict = {
    "person1": {"name": "Himanshu", "age": 21},
    "person2": {"name": "Kapil", "age": 20}
}
print(my_dict)

# 5. Using Sequence and dict function
my_dict = dict([("name", "Himanshu"), ("age", 20), ("city", "Jaipur")])
print(my_dict)

# 6. Duplicate keys
my_dict = {
    "name": "Himanshu",
    "age": 20,
    "name": "Kapil"  # This will overwrite the previous 'name' key
}
print(my_dict)  # Output: {'name': 'Kapil', 'age': 20}




