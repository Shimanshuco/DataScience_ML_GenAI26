s1 = {1, 2, 3}
s2 = {3, 4, 5}

# Union of two sets (combines all unique elements from both sets) (using the | operator)
union_set = s1 | s2
print(union_set)  # Output: {1, 2, 3, 4, 5}

#  Or 
s3= {1, 2, 3}
s4= {3, 4, 5}
union_set = s3.union(s4)  # Using the union() method
print(union_set)  # Output: {1, 2, 3, 4, 5}

# Intersection of two sets (returns only the elements that are present in both sets) (using the & operator)
intersection_set = s1 & s2
print(intersection_set)  # Output: {3}

# Or
intersection_set = s3.intersection(s4)  # Using the intersection() method
print(intersection_set)  # Output: {3}

# Difference of two sets (returns the elements that are present in the first set but not in the second set) (using the - operator)

difference_set = s1 - s2
print(difference_set)  # Output: {1, 2} (Elements that are in s1 but not in s2)

# Or
difference_set = s3.difference(s4)  # Using the difference() method
print(difference_set)  # Output: {1, 2} (Elements that are in s3 but not in s4)

# Symmetric Difference of two sets (returns the elements that are present in either of the sets but not in both) (using the ^ operator)

symmetric_difference_set = s1 ^ s2
print(symmetric_difference_set)  # Output: {1, 2, 4, 5} (Elements that are in either s1 or s2 but not in both)

#or
symmetric_difference_set = s3.symmetric_difference(s4)  # Using the symmetric_difference() method
print(symmetric_difference_set)  # Output: {1, 2, 4, 5} (Elements that are in either s3 or s4 but not in both)

# Membership Testing
print(2 in s1)  # Output: True (2 is present in s1)
print(4 in s1)  # Output: False (4 is not present in s1)

# Iterating through a set
for element in s1:
    print(element)  # Output: 1 2 3 (Elements of s1 will be printed, order may vary)
