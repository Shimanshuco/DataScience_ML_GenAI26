# Pickling : The process of converting a Python object into a byte stream for storage or transmission.
# Unpickling : The process of converting a byte stream back into a Python object.

class Employee:
    def __init__(self, name, age, department):
        self.name = name
        self.age = age
        self.department = department

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Department: {self.department}")

p = Employee("Himanshu", 21, "Data Scientist")

import pickle
# Pickling the object
with open("employee.pkl", "wb") as file:
    pickle.dump(p, file)

# Unpickling the object
with open("employee.pkl", "rb") as file:
    loaded_employee = pickle.load(file)
    loaded_employee.display_info()

# Pickle vs Json
# Pickle lets the user to store data in binary format.
# Json lets the user to store data in text format.
# Pickle retains the functionality of the original object, while Json only retains the data.