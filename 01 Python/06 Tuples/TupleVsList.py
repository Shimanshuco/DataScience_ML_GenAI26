# List vs Tuple : Time
import time

L= list(range(1000000))
T= tuple(range(100000))

start_time = time.time()
for i in L:
    i*5
print("Time taken by list: ", time.time() - start_time)

start_time = time.time()
for i in T:
    i*5
print("Time taken by tuple: ", time.time() - start_time)

# List vs Tuple : Memory
import sys
L= list(range(1000000))
T= tuple(range(100000))

print("Memory taken by list: ", sys.getsizeof(L))
print("Memory taken by tuple: ", sys.getsizeof(T))

# List vs Tuple : Mutability
a = [1, 2, 3, 4, 5]
b=a
a.append(6)
print(a) # [1, 2, 3, 4, 5, 6]
print(b) # [1, 2, 3, 4, 5, 6] 
# b is a reference to a, so when we change a, b also changes.

# But in tuple 
a = (1, 2, 3, 4, 5)
b=a
a = a + (6,)
print(a) # (1, 2, 3, 4, 5, 6)
print(b) # (1, 2, 3, 4, 5)
# b is a reference to a, but when we change a, b does not change because tuples are immutable.