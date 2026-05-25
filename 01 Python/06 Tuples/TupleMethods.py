# Tuple Methods

# 1. len() method
t1 = (1, 2, 3, 4, 5)
print(len(t1)) # 5

# 2. count() method
t2 = (1, 2, 3, 4, 5, 1, 2, 3)
print(t2.count(1)) # 2
print(t2.count(2)) # 2
print(t2.count(9)) # 0

# 3. index() method
print(t2.index(1)) # 0
print(t2.index(9)) # ValueError: tuple.index(x): x not found

# 4. sum() method
t3 = (1, 2, 3, 4, 5)
print(sum(t3)) # 15

# 5. max() method
print(max(t3)) # 5

# 6. min() method
print(min(t3)) # 1

# 7. sorted() method
print(sorted(t3)) # [1, 2, 3, 4, 5]

# 8. reversed() method
print(tuple(reversed(t3))) # (5, 4, 3, 2, 1)

# 9. zip() method
t4 = ('a', 'b', 'c', 'd', 'e')
print(list(zip(t3, t4))) # [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd'), (5, 'e')]

# 10. enumerate() method
print(list(enumerate(t3))) # [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5)]

# 11.unpacking a tuple
t5 = (1, 2, 3)
a, b, c = t5
print(a) # 1
print(b) # 2
print(c) # 3

