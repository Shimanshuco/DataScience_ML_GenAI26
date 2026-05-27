# Serialization is the process of converting a Python object into a byte stream, which can be saved to a file or transmitted over a network.
# Json : JavaScript Object Notation, is a lightweight data interchange format that is easy for humans to read and write, and easy for machines to parse and generate. It is commonly used for serializing and transmitting structured data over a network connection.

# Serialization using JSON module

# 1. List
import json
L = [1, 2, 3, 4, 5]
with open('list.json', 'w') as f:
    json.dump(L, f)

# 2. Dictionary
D = {'name': 'Himanshu', 'age': 21, 'city': 'Jaipur'}   
with open('dict.json', 'w') as f:
    json.dump(D, f)
    # or json.dump(D, f, indent=4) # for pretty printing

# 3. Tuple
T = (1, 2, 3, 4, 5)
with open('tuple.json', 'w') as f:
    json.dump(T, f)

# But JSON does not support tuples, so it will be serialized as a list. To convert it back to a tuple, we can use the tuple() function.

# 4. Nested Dictionary
nested_dict = {
    'name': 'Himanshu',
    'age': 21,
    'city': 'Jaipur',
    'skills': ['Python', 'Data Science', 'Machine Learning'],
    'education': {
        'degree': 'B.Tech',
        'university': 'Apex University',
        'year': 2023
    }
}

with open('nested_dict.json', 'w') as f:
    json.dump(nested_dict, f, indent=4)

# 5. Custom Object

import json

class Person:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city

person = Person('Himanshu', 21, 'Jaipur')


def show_obj_person(person):
    if isinstance(person, Person):
        return {
            "name": person.name,
            "age": person.age,
            "city": person.city
        }

with open('person.json', 'w') as f:
    json.dump(show_obj_person(person), f, indent=4)

# or 

with open('person.json', 'w') as f:
    json.dump(person.__dict__, f, indent=4) # Syntax : json.dump(object.__dict__, file, indent=4) to serialize a custom object by converting it to a dictionary using the __dict__ attribute.

# object.__dict__ is a built-in attribute of Python objects that returns a dictionary containing the object's attributes and their corresponding values. It is commonly used for serialization and deserialization of custom objects, as it allows us to convert the object's state into a format that can be easily stored or transmitted.