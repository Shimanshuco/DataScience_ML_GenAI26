# Union / Union update
a = {1, 2, 3}
b = {3, 4, 5}
print(a | b)  # Union

a.update(b)  # Update
print(a)
print(b)

# Intersection / Intersection update
a = {1, 2, 3}
b = {3, 4, 5}
print(a & b)  # Intersection
a.intersection_update(b)  # Intersection update
print(a)
print(b)

# Difference / Difference update
a = {1, 2, 3}
b = {3, 4, 5}
print(a - b)  # Difference
a.difference_update(b)  # Difference update
print(a)
print(b)

# Symmetric difference / Symmetric difference update
a = {1, 2, 3}
b = {3, 4, 5}
print(a ^ b)  # Symmetric difference
a.symmetric_difference_update(b)  # Symmetric difference update
print(a)
print(b)
