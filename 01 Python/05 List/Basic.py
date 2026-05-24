# List : List is a collection of items which is ordered and changeable. It allows duplicate members.
# List is defined by having values between square brackets [ ].
# List can contain any type of data and can also contain mixed data types.

# Creating a List
my_list = [1, 2, 3, 4, 5]
print(my_list)

# List using user input
user_list = input("Enter a list of items separated by commas: ").split(",")
print(user_list)

# List with mixed data types
mixed_list = [1, "Hello", 3.14, True]
print(mixed_list)

# List with duplicate items
duplicate_list = [1, 2, 2, 3, 4, 4, 5]
print(duplicate_list)

# List with nested lists
nested_list = [1, 2, [3, 4], 5]
print(nested_list)

# Accessing List Items
print(my_list[0])  # Accessing the first item
print(my_list[2])  # Accessing the third item

# Negative indexing
print(my_list[-1])  # Accessing the last item
print(my_list[-2])  # Accessing the second last item

# Slicing a List
print(my_list[1:4])  # Accessing items from index 1 to
print(my_list[:3])   # Accessing the first three items
print(my_list[3:])   # Accessing items from index 3 to the end

# List Length
print(len(my_list))  # Getting the length of the list

# Looping through a List
for item in my_list:
    print(item)
