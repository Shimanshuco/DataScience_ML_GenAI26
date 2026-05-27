# Deserialization is the process of converting a byte stream back into a Python object.

import json

# Deserialization using JSON module

# 1. List
with open('list.json', 'r') as f:
    L = json.load(f)
    print(L)

# 2. Dictionary
with open('dict.json', 'r') as f:
    D = json.load(f)
    print(D)

# 3. Tuple
with open('tuple.json', 'r') as f:
    T = json.load(f)
    print(T)

# But JSON does not support tuples, so it will be deserialized as a list. To convert it back to a tuple, we can use the tuple() function.

# 4. Nested Dictionary
with open('nested_dict.json', 'r') as f:
    nested_dict = json.load(f)
    print(nested_dict)

# 5. Custom Object
class Person:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city
with open('person.json', 'r') as f:
    person_dict = json.load(f)
    person = Person(**person_dict)
    print(person.name, person.age, person.city)