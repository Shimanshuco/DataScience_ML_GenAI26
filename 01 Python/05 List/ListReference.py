# Referential Arrays (Python lists store REFERENCES to objects, not the objects themselves)

list = [1, 2, 3]

print(id(list))      # Memory address of the LIST object itself

# These are memory addresses of the INTEGER OBJECTS referenced by the list
print(id(list[0]))   
print(id(list[1]))
print(id(list[2]))

# Same integer objects are reused by Python (integer interning/caching)
print(id(1))
print(id(2))
print(id(3))


# ---------------------- DOWNSIDE EXPLANATION ----------------------

# Downside of referential storage:
#
# Lists do NOT store actual values directly.
# They store references (memory pointers) to objects.
# That's why we can store mixed data types in a single list.
# This can create unexpected side effects with MUTABLE objects.

a = [1, 2]
b = a          # b now references the SAME list object

b.append(3)

print(a)       # [1, 2, 3]
print(b)       # [1, 2, 3]

# Why?
# Because both 'a' and 'b' point to the SAME memory location.
# Modifying through one reference affects the other.

print(id(a))   # Same memory address
print(id(b))   # Same memory address


# Another downside:
# Extra memory overhead.
#
# A list stores references/pointers instead of raw values.
# Each element requires additional pointer storage.
#
# This is less memory-efficient compared to low-level arrays
# in languages like C where raw values are stored directly.


# Another issue:
# Copying can be confusing.

x = [[1, 2], [3, 4]]
y = x.copy()   # Shallow copy

y[0].append(99)

print(x)       # [[1, 2, 99], [3, 4]]
print(y)       # [[1, 2, 99], [3, 4]]

# Even after copying, inner lists are still shared references.
# This can lead to bugs if you expect a fully independent copy.