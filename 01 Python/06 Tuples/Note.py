a,b,c = (1,2,3)
print(a) # 1
print(b) # 2
print(c) # 3

# This is called unpacking a tuple, we can unpack a tuple into variables. The number of variables must be equal to the number of elements in the tuple.

a= 1
b= 2
c= 3
t6 = (a, b, c)
print(t6) # (1, 2, 3)

# This is called packing a tuple, we can pack variables into a tuple. The number of variables can be less than or equal to the number of elements in the tuple.


# Two variables swap
a = 10
b = 20
a, b = b, a
print(a) # 20
print(b) # 10


# * operator in tuple
a,b, *others = (1,2,3,4,5)
print(a) # 1
print(b) # 2
print(others) # [3, 4, 5]

a, *others, b = (1,2,3,4,5)
print(a) # 1
print(others) # [2, 3, 4]
print(b) # 5