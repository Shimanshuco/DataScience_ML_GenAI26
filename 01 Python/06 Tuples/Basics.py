# Tuple : Tuples is a immutable list
# Tuple is defined by using () parenthesis
# Tuple is ordered collection of items
# Tuple can contain duplicate items
# Tuple can contain different data types

# 1. Creating a tuple

t1 = (1, 2, 3, 4, 5) # Homogeneous tuple
t2 = (1,"Hello",print,3.14) # Heterogeneous tuple
# Tuple with single element
#Wrong way
t3=(1)
print(type(t3)) # <class 'int'>
#Right way
t3=(1,)
print(type(t3)) # <class 'tuple'>

t4=('Hello',);
print(t4)
t5 = tuple("Hello")
print(t5)

# 2. Accessing elements of a tuple
# a) Indexing
print(t1) # (1, 2, 3, 4, 5)
print(t1[0]) # 1
print(t1[1]) # 2
print(t1[2]) # 3
print(t1[3]) # 4
print(t1[4]) # 5

# b) Slicing
print(t1[0:3]) # (1, 2, 3)
print(t1[2:]) # (3, 4, 5)
print(t1[:3]) # (1, 2, 3)
print(t1[:]) # (1, 2, 3, 4, 5)
print(t1[::-1]) # (5, 4, 3, 2, 1)

# 3. Editing a tuple
# Tuples are immutable, we cannot change the elements of a tuple
# t1[0] = 10 # TypeError: 'tuple' object does not support item assignment


# 4. Deleting a tuple
# We cannot delete a tuple, but we can delete the reference to the tuple
del t1

# 5. Tuple Operations

# a) Concatenation
t6 = t1 + t2
print(t6) # (1, 2, 3, 4, 5, 1, 'Hello', <built-in function print>, 3.14)

# b) Repetition
t7 = t1 * 2
print(t7) # (1, 2, 3, 4, 5, 1, 2, 3, 4, 5)

# c) Membership
print(3 in t1) # True
print(10 in t1) # False

# iterating through a tuple
for i in t1:
    print(i)
