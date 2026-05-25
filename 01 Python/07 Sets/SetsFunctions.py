# Sets Functions

# 1. len() function to get the number of elements in a set
my_set = {1, 2, 3, 4, 5}
print(len(my_set))  # Output: 5 (Number of elements in the set)

# 2. max() function to get the maximum element in a set
print(max(my_set))  # Output: 5 (Maximum element in the set)

# 3. min() function to get the minimum element in a set
print(min(my_set))  # Output: 1 (Minimum element in the set)

# 4. sum() function to get the sum of all elements in a set
print(sum(my_set))  # Output: 15 (Sum of all elements in the set)

# 5. sorted() function to get a sorted list of elements in a set
print(sorted(my_set))  # Output: [1, 2, 3, 4, 5] (Sorted list of elements in the set)
print(sorted(my_set, reverse=True))  # Output: [5, 4, 3, 2, 1] (Sorted list of elements in the set in reverse order)

# 6. any() function to check if any element in the set is True
print(any(my_set))  # Output: True (Since all elements in the set are non-zero, any() returns True)

# 7. all() function to check if all elements in the set are True
print(all(my_set))  # Output: True (Since all elements in the set are non-zero, all() returns True)

s2 = {0, 1, 2, 3, 4}
print(any(s2))  # Output: True (Since there are non-zero elements in the set, any() returns True)
print(all(s2))  # Output: False (Since there is a zero element in the set, all() returns False)

# isdisjoint() function to check if two sets have no elements in common
a = {1, 2, 3}
b = {4, 5, 6}
c = {3, 4, 5}
print(a.isdisjoint(b))  # Output: True (Since sets a and b have no elements in common)
print(a.isdisjoint(c))  # Output: False (Since sets a and c have the element 3 in common)

# issubset() function to check if one set is a subset of another
a = {1, 2, 3}
b = {1, 2, 3, 4, 5}
print(a.issubset(b))  # Output: True (Since set a is a subset of set b)
print(b.issubset(a))  # Output: False (Since set b is not a subset of set a)

# issuperset() function to check if one set is a superset of another
a = {1, 2, 3}
b = {1, 2}
print(a.issuperset(b))  # Output: True (Since set a is a superset of set b)
print(b.issuperset(a))  # Output: False (Since set b is not a superset of set a)

# copy() function to create a shallow copy of a set
original_set = {1, 2, 3}
copied_set = original_set.copy()
print(copied_set)  # Output: {1, 2, 3} (Copied set is the same as the original set)
print(copied_set is original_set)  # Output: False (Copied set is a different object than the original set)
