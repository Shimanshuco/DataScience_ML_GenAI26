# Frozen Set
# A frozenset is an immutable version of a set. Once created, you cannot modify a frozenset (i.e., you cannot add or remove elements).
# You can create a frozenset using the frozenset() function, which takes an iterable as an argument.

# Creating a frozenset
my_frozenset = frozenset([1, 2, 3, 4, 5])
print(my_frozenset)  # Output: frozenset({1, 2, 3, 4, 5})

# You can perform set operations on frozensets, such as union, intersection, difference, and symmetric difference.
# Example of set operations with frozensets
frozenset_a = frozenset([1, 2, 3])
frozenset_b = frozenset([3, 4, 5])
# Union
union_set = frozenset_a.union(frozenset_b)
print(union_set)  # Output: frozenset({1, 2, 3, 4, 5})
# Intersection
intersection_set = frozenset_a.intersection(frozenset_b)
print(intersection_set)  # Output: frozenset({3})
# Difference
difference_set = frozenset_a.difference(frozenset_b)
print(difference_set)  # Output: frozenset({1, 2})
# Symmetric Difference
symmetric_difference_set = frozenset_a.symmetric_difference(frozenset_b)
print(symmetric_difference_set)  # Output: frozenset({1, 2, 4, 5})

# When to use frozenset: Read-only applications where you want to ensure that the set of elements cannot be modified. 
# For example, you might use a frozenset as a key in a dictionary or as an element of another set, since regular sets cannot be used in these contexts due to their mutability.

# Is 2D frozenset possible?
fs = frozenset([frozenset([1, 2]), frozenset([3, 4])])
print(fs)  # Output: frozenset({frozenset({1, 2}), frozenset({3, 4})})
