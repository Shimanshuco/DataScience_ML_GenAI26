# Sets : Sets are unordered collections of unique elements. 
# They are mutable, meaning you can add or remove elements from a set after it has been created. 
# Sets are defined using curly braces {} or the set() constructor.
# Sets are mutable but they cannot contain mutable elements like lists or dictionaries.

# Creating a set

# 1. Empty Set
s = {}
print(type(s))  # Output: <class 'dict'> (This is a dictionary, not a set)
# To create an empty set, you need to use the set() constructor
empty_set = set()
print(empty_set)  # Output: set() (This is an empty set)

# 2. Set with elements
my_set = {1, 2, 3, 4, 5}
print(my_set)  # Output: {1, 2, 3, 4, 5}

# Creating a set using the set() constructor
my_set2 = set([1, 2, 3, 4, 5])
print(my_set2)  # Output: {1, 2, 3, 4, 5}

# 3. 1D and 2D Sets
# 1D Set
set_1d = {1, 2, 3, 4, 5}
print(set_1d)  # Output: {1, 2, 3, 4, 5}
# 2D Set (Set of sets)
set_2d = {{1, 2}, {3, 4}, {5, 6}}
print(set_2d)  # Output: {{1, 2}, {3, 4}, {5, 6}}


# 4. Homogeneous and Heterogeneous Sets
# Homogeneous Set (All elements are of the same type)
homogeneous_set = {1, 2, 3, 4, 5}
print(homogeneous_set)  # Output: {1, 2, 3, 4, 5}
# Heterogeneous Set (Elements are of different types)
heterogeneous_set = {1, "Hello", 3.14, (1, 2), frozenset({1, 2})}
print(heterogeneous_set)  # Output: {1, 'Hello', 3.14, (1, 2), frozenset({1, 2})}

# 5. Using type conversion to create sets
# From string
string_set = set("Hello")
print(string_set)  # Output: {'H', 'e', 'l', 'o'} (Note: 'l' appears only once because sets do not allow duplicates)
# From list
list_set = set([1, 2, 3, 4, 5])
print(list_set)  # Output: {1, 2, 3, 4, 5}

# 5. Duplicates in Sets
# When you create a set with duplicate elements, only one instance of each element will be stored in the set.
duplicate_set = {1, 2, 2, 3, 4, 4, 5}
print(duplicate_set)  # Output: {1, 2, 3, 4, 5} (Duplicates are removed)

# 6. Set with mutable elements (This will raise an error)
# mutable_set = {1, 2, [3, 4]}  # This will raise a TypeError because lists are mutable and cannot be added to a set


s3 = {1,2,3,'hello',True};
print(s3)  # Output: {1, 2, 3, 'hello'} (Note: True is treated as 1 in sets, so it will not be added as a separate element)

# Set Comparison
set_a = {1, 2, 3}
set_b = {3, 4, 5}
print(set_a == set_b)  # Output: False (The sets are not equal)
set_c = {1, 2, 3}
print(set_a == set_c)  # Output: True (The sets are equal)


# Accessing Elements in a Set
# Since sets are unordered, you cannot access elements by index. 
# However, you can check for the presence of an element using the 'in' keyword.

my_set = {1, 2, 3, 4, 5}
print(3 in my_set)  # Output: True (3 is present in the set)
print(6 in my_set)  # Output: False (6 is not present in the set)

# Editing a Set
# We cannot edit an element in a set directly because sets do not support indexing.
set_a = {1, 2, 3}
# set_a[0] = 10  # This will raise a TypeError because sets do not support indexing

# Adding Elements to a Set
# 1. Using the add() method to add a single element to the set
my_set = {1, 2, 3}
my_set.add(4)  # Adding a single element to the set
print(my_set)  # Output: {1, 2, 3, 4}

# 2. Using the update() method to add multiple elements to the set
s.update({5, 6, 7})  # Adding multiple elements to the set
print(s)  # Output: {1, 2, 3, 'hello', True, 5, 6, 7} (Note: True is treated as 1 in sets, so it will not be added as a separate element)


# Removing Elements from a Set

# 1. del keyword to delete the entire set
# del my_set  # This will delete the entire set

# 2. Using the remove() method to remove a specific element from the set
my_set = {1, 2, 3, 4, 5}
my_set.remove(3)  # Removing a specific element from the set
print(my_set)  # Output: {1, 2, 4, 5} (3 has been removed from the set)
# my_set.remove(10)  # This will raise a KeyError because 10 is not present in the set

# 3. Using the discard() method to remove a specific element from the set (This will not raise an error if the element is not present)
my_set.discard(4)  # Removing a specific element from the set
print(my_set)  # Output: {1, 2, 5} (4 has been removed from the set)
my_set.discard(10)  # This will not raise an error because 10 is not present in the set
print(my_set)  # Output: {1, 2, 5} (The set remains unchanged because 10 was not present)

# 4. Using the pop() method to remove and return an arbitrary element from the set
removed_element = my_set.pop()  # Removing and returning an arbitrary element from the set
print(removed_element)  # Output: 1 (The removed element may vary each time you run the code because sets are unordered)
print(my_set)  # Output: {2, 5} (The set now contains the remaining elements after the pop operation)   

# 5. Using the clear() method to remove all elements from the set
my_set.clear()  # Removing all elements from the set
print(my_set)  # Output: set() (The set is now empty)



